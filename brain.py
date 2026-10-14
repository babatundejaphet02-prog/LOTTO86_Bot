import difflib
import re
import unicodedata

from knowledge import KB


def _singular(t: str) -> str:
    if t.endswith("ies") and len(t) > 4:
        return t[:-3] + "y"
    if t.endswith("s") and not t.endswith("ss") and len(t) > 3:
        return t[:-1]
    return t


def norm(text: str) -> list:
    """Lowercase, strip accents, join '4-3-3' into '433', split into singular words."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"(?<=\d)[\s\-](?=\d)", "", text)
    return [_singular(t) for t in re.findall(r"[a-z0-9]+", text)]


# Pre-compute keyword indexes once at start-up
INDEX = []
for entry in KB:
    singles, phrases = set(), []
    for kw in entry["keywords"]:
        toks = norm(kw)
        if len(toks) == 1:
            singles.add(toks[0])
        elif toks:
            phrases.append(" ".join(toks))
    INDEX.append((entry, singles, phrases))


def find(text: str):
    """Return the best matching knowledge-base entry, or None."""
    toks = norm(text)
    if not toks:
        return None
    tokset = set(toks)
    joined = " " + " ".join(toks) + " "

    best, best_score = None, 0
    for entry, singles, phrases in INDEX:
        score = 0
        for s in singles:
            if s in tokset:
                score += 2
            elif len(s) >= 5 and difflib.get_close_matches(s, toks, n=1, cutoff=0.84):
                score += 1  # typo-tolerant match
        for p in phrases:
            if f" {p} " in joined:
                score += 3
        if score > best_score:  # ties keep the earlier entry (football beats small talk)
            best, best_score = entry, score
    return best


FOOTBALL_WORDS = {
    "football", "soccer", "goal", "match", "team", "player", "referee", "league", "cup", "club",
    "coach", "manager", "striker", "keeper", "stadium", "fifa", "uefa", "pitch", "ball", "tournament",
    "fan", "premier", "laliga", "bundesliga", "champion", "win", "won", "score", "scored", "lose",
    "lost", "draw", "season", "kick", "pass", "defender", "midfielder", "winger", "trophy", "final",
}


def is_football(text: str) -> bool:
    return any(t in FOOTBALL_WORDS for t in norm(text))
