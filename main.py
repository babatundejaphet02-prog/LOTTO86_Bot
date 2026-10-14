import asyncio
import html
import logging
import os
import random
import re

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatAction, ParseMode
from telegram.error import BadRequest
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from brain import find, is_football
from knowledge import BY_ID, CATS, FACTS, KB

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("football-bot")

BOT_TOKEN = os.environ["BOT_TOKEN"]  # set this in Railway > Variables

WELCOME = (
    "⚽ <b>Hi, I'm your Football Buddy!</b>\n\n"
    "Ask me anything about football in your own words, for example:\n"
    "• what is offside?\n• explain the 4-3-3\n• who is Pelé?\n\n"
    "Tell me your club (<i>I support Arsenal</i>) and I'll remember it.\n"
    "Or pick a topic below 👇"
)
MENU_TEXT = "⚽ <b>Football topics</b>\n\nPick one, or just type your question 👇"

TEAM_RE = re.compile(
    r"(?:i support|i'm a fan of|i am a fan of|im a fan of|my (?:favou?rite )?(?:team|club) is|i cheer for)\s+(.{2,40})",
    re.IGNORECASE,
)
ASKS_TEAM_RE = re.compile(
    r"\bwho do i support\b|\bwhich team do i support\b|\bwhat team do i support\b"
    r"|\bwhat(?:'s| is) my (?:favou?rite )?(?:team|club)\b",
    re.IGNORECASE,
)
NOT_TEAMS = {"football", "soccer", "the game", "sports", "sport"}

OFF_TOPIC = [
    "I only talk football ⚽ Ask me about rules, tactics, positions, football words or legends 👇",
    "That's outside my pitch 😄 I'm all about football. Try asking about offside, VAR or a legend 👇",
]
UNSURE = [
    "Hmm, I don't know that one yet 🤔 Try asking in a different way, or pick a topic 👇",
    "That one's not in my notebook yet 📓 Rephrase it, or browse the topics 👇",
]


# ---------------------------------------------------------------- keyboards
def main_menu() -> InlineKeyboardMarkup:
    items = list(CATS.items())
    rows = [
        [InlineKeyboardButton(label, callback_data=f"cat:{key}") for key, label in items[i:i + 2]]
        for i in range(0, len(items), 2)
    ]
    rows.append([InlineKeyboardButton("🎲 Random fact", callback_data="fact")])
    return InlineKeyboardMarkup(rows)


def topic_menu(cat: str) -> InlineKeyboardMarkup:
    topics = [e for e in KB if e["cat"] == cat]
    rows = [
        [InlineKeyboardButton(e["title"], callback_data=f"kb:{e['id']}") for e in topics[i:i + 2]]
        for i in range(0, len(topics), 2)
    ]
    rows.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def nav_markup(cat: str) -> InlineKeyboardMarkup:
    rows = []
    if cat in CATS:
        rows.append([InlineKeyboardButton("⬅️ More in this topic", callback_data=f"cat:{cat}")])
    rows.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def fact_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎲 Another fact", callback_data="fact")],
        [InlineKeyboardButton("🏠 Menu", callback_data="menu")],
    ])


# ---------------------------------------------------------------- helpers
def render(entry: dict) -> str:
    ans = entry["answer"]
    if isinstance(ans, list):
        ans = random.choice(ans)
    if entry["cat"] == "chat":
        return ans
    return f"<b>{entry['title']}</b>\n\n{ans}"


def fact_text() -> str:
    return f"🎲 <b>Football fact</b>\n\n{random.choice(FACTS)}"


def extract_team(text: str):
    m = TEAM_RE.search(text)
    if not m:
        return None
    team = m.group(1).strip(" .!?,'\"")
    if not team or team.lower() in NOT_TEAMS:
        return None
    return team.title() if team.islower() else team


async def safe_edit(query, text: str, markup: InlineKeyboardMarkup):
    try:
        await query.edit_message_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
    except BadRequest as exc:  # e.g. "message is not modified"
        log.info("edit skipped: %s", exc)


# ---------------------------------------------------------------- commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, parse_mode=ParseMode.HTML, reply_markup=main_menu())


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU_TEXT, parse_mode=ParseMode.HTML, reply_markup=main_menu())


async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(fact_text(), parse_mode=ParseMode.HTML, reply_markup=fact_markup())


# ---------------------------------------------------------------- buttons
async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "menu":
        await safe_edit(q, MENU_TEXT, main_menu())
    elif data == "fact":
        await safe_edit(q, fact_text(), fact_markup())
    elif data.startswith("cat:"):
        key = data[4:]
        if key in CATS:
            await safe_edit(q, f"<b>{CATS[key]}</b>\n\nPick a topic 👇", topic_menu(key))
    elif data.startswith("kb:"):
        entry = BY_ID.get(data[3:])
        if entry:
            await safe_edit(q, render(entry), nav_markup(entry["cat"]))


# ---------------------------------------------------------------- chat
async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()[:300]
    if not text:
        return

    await update.message.chat.send_action(ChatAction.TYPING)
    await asyncio.sleep(0.5)

    # 1. the user tells us their team
    team = extract_team(text)
    if team:
        context.user_data["team"] = team
        t = html.escape(team)
        reply = random.choice([
            f"<b>{t}</b>! Great choice ⚽ I'll remember that.",
            f"A <b>{t}</b> fan, nice! 🔥 I'll remember that.",
            f"Respect to <b>{t}</b>! 💪 I'll remember that.",
        ])
        await update.message.reply_text(reply, parse_mode=ParseMode.HTML, reply_markup=main_menu())
        return

    # 2. the user asks which team they support
    if ASKS_TEAM_RE.search(text):
        saved = context.user_data.get("team")
        if saved:
            reply = f"You support <b>{html.escape(saved)}</b>! 🔥"
        else:
            reply = "You haven't told me yet! Just type something like <i>I support Arsenal</i> ⚽"
        await update.message.reply_text(reply, parse_mode=ParseMode.HTML)
        return

    # 3. knowledge base
    entry = find(text)
    if entry:
        await update.message.reply_text(
            render(entry), parse_mode=ParseMode.HTML, reply_markup=nav_markup(entry["cat"])
        )
    elif is_football(text):
        await update.message.reply_text(random.choice(UNSURE), reply_markup=main_menu())
    else:
        await update.message.reply_text(random.choice(OFF_TOPIC), reply_markup=main_menu())


async def on_error(update, context: ContextTypes.DEFAULT_TYPE):
    log.error("Error while handling an update", exc_info=context.error)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler(["start", "help"], start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)
    app.run_polling()


if __name__ == "__main__":
    main()
