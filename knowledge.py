# Football knowledge base. Add or edit entries freely.
#   keywords: words or phrases people might type (lowercase, accents not needed)
#   answer:   the reply. HTML allowed (<b>, <i>). A list = random variety.
# Football entries come first, small-talk entries ("chat") come last.

CATS = {
    "rules": "📘 Rules",
    "tactics": "🧠 Tactics",
    "positions": "🧍 Positions",
    "terms": "🗣 Football words",
    "legends": "🏆 Legends & History",
}

KB = []


def add(id, cat, title, keywords, answer):
    KB.append({"id": id, "cat": cat, "title": title, "keywords": keywords, "answer": answer})


# ------------------------------------------------------------------ RULES
add("basics", "rules", "Football basics",
    ["basics", "basic rules", "rules of football", "football rules", "how to play football",
     "how is football played", "how does football work", "how many players", "players on the pitch",
     "how long is a match", "match length", "how long is a game", "90 minutes"],
    "⚽ Two teams of 11 players (one of them the goalkeeper) try to score by putting the ball in the other team's goal.\n\n"
    "A match has two halves of 45 minutes, plus added time. The team with more goals wins. "
    "Only the goalkeeper may use their hands, and only inside their own penalty area.\n\n"
    "Want details? Ask about offside, penalty, cards, VAR and more.")

add("offside", "rules", "Offside",
    ["offside", "off side", "offside rule"],
    "A player is <b>offside</b> if, at the moment a teammate passes the ball to them, they are closer to the opponents' "
    "goal line than both the ball and the second-last opponent (usually the last defender, because the goalkeeper counts as one).\n\n"
    "Simple version: don't stand behind the last defender when the pass is played. Being level with the defender is fine.\n\n"
    "✅ You can't be offside in your own half, or from a goal kick, throw-in or corner.\n"
    "⚠️ Standing in an offside position is not a foul by itself. It only counts if you join the play "
    "(touch the ball, block the keeper's view or challenge a defender). The result is a free kick for the other team.")

add("penalty", "rules", "Penalty kick",
    ["penalty", "penalty kick", "spot kick", "penalty area", "penalty box"],
    "A <b>penalty kick</b> is given when a defender commits a foul (like tripping, pushing or handball) inside their own penalty area.\n\n"
    "🥅 The ball is placed on the penalty spot, 11 metres (12 yards) from goal. One player shoots against the goalkeeper only. "
    "Everyone else must stay outside the box and the arc. The keeper must keep at least one foot on the goal line until the ball is kicked.\n\n"
    "Most penalties are scored, so winning one is a big moment!")

add("yellow", "rules", "Yellow card",
    ["yellow card", "booking", "booked", "caution"],
    "A <b>yellow card</b> is an official warning from the referee. It is shown for things like a bad foul, time wasting, "
    "arguing with the referee or stopping a promising attack unfairly.\n\n"
    "Two yellow cards in the same match = a red card, and the player is sent off. "
    "Yellow cards can also pile up over several matches and lead to a ban (the number depends on the competition).")

add("red", "rules", "Red card",
    ["red card", "sent off", "sending off", "send off", "dismissed"],
    "A <b>red card</b> means the player is sent off immediately and cannot be replaced, so the team plays with one player fewer.\n\n"
    "It is shown for: serious foul play, violent conduct (like punching or spitting), stopping an obvious goal-scoring chance "
    "with a foul or handball, abusive language, or a second yellow card.\n\n"
    "The player usually misses at least the next match as well.")

add("var", "rules", "VAR",
    ["var", "video assistant referee", "video referee", "video review"],
    "<b>VAR</b> means Video Assistant Referee. A team of officials watches TV replays and helps the referee with big decisions.\n\n"
    "They can only check four things:\n"
    "1. Goals (was there a foul or offside before it?)\n"
    "2. Penalty decisions\n"
    "3. Direct red cards\n"
    "4. Mistaken identity (the wrong player punished)\n\n"
    "The referee makes the final decision, sometimes by watching the replay on a pitch-side screen. "
    "VAR does not check everything, like normal fouls or corners.")

add("handball", "rules", "Handball",
    ["handball", "hand ball", "hand in football", "touched with hand"],
    "<b>Handball</b> is when a player touches the ball with their hand or arm.\n\n"
    "It is usually a foul if the touch is deliberate, or if the arm is out making the body bigger and the ball hits it. "
    "Not every touch is a foul: a ball hitting an arm that is close to the body is often fine.\n\n"
    "⚠️ A goal scored with the hand or arm doesn't count, even by accident. "
    "Goalkeepers can use their hands, but only inside their own penalty area.")

add("foul", "rules", "Fouls",
    ["foul", "fouls", "tackle", "tripping", "dangerous play"],
    "A <b>foul</b> is an unfair act by a player, like tripping, pushing, holding, kicking or a dangerous tackle.\n\n"
    "• Foul outside the penalty area → free kick to the other team\n"
    "• Foul by a defender inside their own penalty area → penalty kick\n\n"
    "The referee can also show a yellow or red card, depending on how bad it was.")

add("corner", "rules", "Corner kick",
    ["corner", "corner kick", "corner flag"],
    "A <b>corner kick</b> is given to the attacking team when the defending team was the last to touch the ball before it "
    "fully crosses their own goal line (and it's not a goal).\n\n"
    "The ball is placed in the corner arc on the side where it went out. You can score directly from a corner, "
    "and you can't be offside from one.")

add("freekick", "rules", "Free kick",
    ["free kick", "freekick", "direct free kick", "indirect free kick"],
    "A <b>free kick</b> is given to a team after the other team commits a foul. The ball is placed where the foul happened, "
    "and defenders must stand at least 9.15 metres (10 yards) away.\n\n"
    "• <b>Direct free kick:</b> you can score straight away (for fouls like tripping or handball).\n"
    "• <b>Indirect free kick:</b> another player must touch the ball before a goal can count (for things like dangerous play).")

add("throwin", "rules", "Throw-in",
    ["throw in", "throwin", "touchline", "sideline"],
    "A <b>throw-in</b> restarts play when the ball completely crosses the sideline (touchline). "
    "The team that did NOT touch it last gets the throw.\n\n"
    "The thrower must face the pitch, keep both feet on the ground and throw with both hands from behind and over the head. "
    "You can't score directly from a throw-in, and you can't be offside from one.")

add("goalkick", "rules", "Goal kick",
    ["goal kick", "goalkick"],
    "A <b>goal kick</b> restarts play when the attacking team kicks the ball over the goal line (outside the goal).\n\n"
    "The defending team places the ball inside the small goal area and kicks it back into play. "
    "Opponents must stay outside the penalty area until the ball is kicked. You can't be offside from a goal kick.")

add("advantage", "rules", "Advantage",
    ["advantage", "play on", "referee advantage"],
    "<b>Advantage</b> is when the referee sees a foul but lets play continue because the fouled team still has a good chance to attack. "
    "The referee usually stretches both arms forward to show it.\n\n"
    "If the advantage doesn't work out within a few seconds, the referee can bring play back and give the free kick.")

add("addedtime", "rules", "Added time",
    ["added time", "injury time", "stoppage time", "extra minutes", "additional time"],
    "<b>Added time</b> (also called injury time or stoppage time) is extra time at the end of each half to make up for time lost "
    "during the match, for things like injuries, substitutions, VAR checks and goal celebrations.\n\n"
    "The referee decides, and the fourth official shows the minimum number of minutes on a board. "
    "The referee can still play longer if there are more stoppages.")

add("extratime", "rules", "Extra time",
    ["extra time", "overtime", "knockout draw", "level after 90"],
    "<b>Extra time</b> is used in knockout matches (where someone must win) when the score is level after 90 minutes.\n\n"
    "Two more halves of 15 minutes are played. If it's still level afterwards, the match goes to a penalty shootout.")

add("shootout", "rules", "Penalty shootout",
    ["shootout", "shoot out", "penalty shootout", "penalties shootout", "sudden death"],
    "A <b>penalty shootout</b> decides a knockout match that is still level after extra time.\n\n"
    "Each team takes 5 penalty kicks, one after the other. The team that scores more wins. "
    "If it's still level after 5 each, it goes to sudden death: one kick each, and the first team that scores while the other misses wins.")

add("substitution", "rules", "Substitutions",
    ["substitution", "substitute", "sub", "bench", "replace player", "change player"],
    "<b>Substitutions</b> let a team swap tired or injured players for fresh ones from the bench.\n\n"
    "Many competitions today allow up to five substitutions (the rules vary by league and cup). "
    "A player who has been substituted off can't come back on, and swaps only happen when play is stopped, with the referee's permission.")

add("goal", "rules", "What counts as a goal",
    ["goal line", "goal line technology", "does the goal count", "what counts as a goal", "ball crossed the line"],
    "A <b>goal</b> counts when the whole ball crosses the goal line, between the posts and under the crossbar.\n\n"
    "In big competitions, goal-line technology tells the referee instantly if the ball was fully over the line. "
    "A goal can still be cancelled if there was a foul or offside before it.")

add("referee", "rules", "Referee and officials",
    ["referee", "ref", "linesman", "assistant referee", "fourth official", "officials"],
    "The <b>referee</b> is in charge of the match: he or she applies the rules, uses the whistle, shows cards and keeps the time.\n\n"
    "• <b>Assistant referees</b> (linesmen) help with offside, throw-ins and corners.\n"
    "• The <b>fourth official</b> handles substitutions and shows the added-time board.\n"
    "• The <b>VAR team</b> watches replays on big decisions.")

# ---------------------------------------------------------------- TACTICS
add("formation", "tactics", "Formations",
    ["formation", "formations", "line up", "lineup", "starting eleven", "starting xi"],
    "A <b>formation</b> shows how a team lines up. The numbers are read from defence to attack, and the goalkeeper isn't counted.\n\n"
    "So <b>4-4-2</b> means 4 defenders, 4 midfielders and 2 strikers. Other common ones: 4-3-3, 4-2-3-1 and 3-5-2. "
    "Managers change the formation to suit their players and the opponent.")

add("f442", "tactics", "4-4-2",
    ["442"],
    "<b>4-4-2</b>: four defenders, four midfielders and two strikers.\n\n"
    "It's simple and balanced, with two lines of four that are hard to play through. The two strikers work as a pair "
    "(for example one tall target man and one quick runner).\n\n"
    "Weakness: it can be outnumbered in midfield by teams that play with three there.")

add("f433", "tactics", "4-3-3",
    ["433"],
    "<b>4-3-3</b>: four defenders, three midfielders and a front three (two wingers and a centre-forward).\n\n"
    "It's an attacking shape: the wingers stretch the pitch and the team can press high.\n\n"
    "Weakness: the full-backs and midfielders must work hard to cover the space the wingers leave behind.")

add("f352", "tactics", "3-5-2",
    ["352", "wing back", "wingback", "wing backs"],
    "<b>3-5-2</b>: three centre-backs, five midfielders (including two wing-backs who run up and down the sides) and two strikers.\n\n"
    "It's strong in the middle and gives width through the wing-backs.\n\n"
    "Weakness: there is space behind the wing-backs when they go forward.")

add("pressing", "tactics", "Pressing",
    ["pressing", "press", "high press", "gegenpressing", "counter pressing"],
    "<b>Pressing</b> means chasing the opponents quickly to win the ball back high up the pitch, close to their goal.\n\n"
    "<b>Gegenpressing</b> (German for counter-pressing) means pressing straight away after losing the ball, within seconds, "
    "before the other team can organise. It's tiring, but it can create goals from turnovers.")

add("tikitaka", "tactics", "Tiki-taka",
    ["tiki taka", "tikitaka", "possession football", "passing football"],
    "<b>Tiki-taka</b> is a style based on short, quick passes and constant movement to keep the ball. "
    "The idea: if you have the ball, the opponent can't score.\n\n"
    "It became famous with Barcelona and the Spain national team in the late 2000s and early 2010s.")

add("counter", "tactics", "Counter-attack",
    ["counter attack", "counterattack", "counter attacking", "on the break", "fast break"],
    "A <b>counter-attack</b> is when a team wins the ball and attacks very fast while the opponent is still out of position.\n\n"
    "Teams that defend deep and have quick forwards often play this way.")

add("offsidetrap", "tactics", "Offside trap",
    ["offside trap", "step up defence"],
    "The <b>offside trap</b> is when defenders step forward together, in a line, just before a pass is played, "
    "so the attacker is caught offside.\n\n"
    "It needs perfect timing and teamwork. If one defender stays back, the trap fails and the attacker can run through on goal.")

add("false9", "tactics", "False 9",
    ["false 9", "false nine", "false striker"],
    "A <b>false 9</b> is a centre-forward who drops deep into midfield instead of staying up front.\n\n"
    "This pulls the opponent's centre-backs out of position and creates space for teammates to run into. "
    "A famous example is Lionel Messi at Barcelona.")

add("parkbus", "tactics", "Parking the bus",
    ["park the bus", "parking the bus", "defensive football", "ultra defensive"],
    "<b>Parking the bus</b> is slang for defending with almost every player behind the ball, usually to protect a lead "
    "or get a draw against a stronger team. It makes it hard for the other side to find space.")

add("setpiece", "tactics", "Set pieces",
    ["set piece", "set pieces", "set play", "dead ball"],
    "<b>Set pieces</b> are restarts where the ball is dead and teams use planned moves: corners, free kicks, throw-ins and penalties.\n\n"
    "Many goals come from them, so teams practise routines like blocking defenders or short passes before the cross.")

# -------------------------------------------------------------- POSITIONS
add("positions", "positions", "Positions overview",
    ["positions", "player positions", "who plays where", "football positions"],
    "The main positions are:\n"
    "🧤 Goalkeeper\n🛡 Defenders (centre-backs and full-backs)\n⚙️ Midfielders\n⚡ Forwards (wingers and strikers)\n\n"
    "Ask about one, for example <i>what does a winger do?</i>")

add("goalkeeper", "positions", "Goalkeeper",
    ["goalkeeper", "keeper", "goalie", "goal keeper"],
    "The <b>goalkeeper</b> is the last line of defence and the only player allowed to use hands (inside their own penalty area).\n\n"
    "They stop shots, catch crosses, organise the defence and start attacks with throws and kicks. "
    "They wear a different-coloured kit so everyone can tell them apart.")

add("centreback", "positions", "Centre-back",
    ["centre back", "center back", "centreback", "defender", "central defender"],
    "<b>Centre-backs</b> play in the middle of the defence, in front of the goalkeeper.\n\n"
    "Their job is to stop strikers, win headers, block shots and clear the danger. Modern centre-backs also pass the ball out from the back.")

add("fullback", "positions", "Full-back",
    ["full back", "fullback", "left back", "right back"],
    "<b>Full-backs</b> defend on the left or right side of the pitch. They stop the opposing wingers and also run forward "
    "to help the attack. They need lots of stamina.")

add("midfielder", "positions", "Midfielder",
    ["midfielder", "midfield", "playmaker", "defensive midfielder", "attacking midfielder"],
    "<b>Midfielders</b> link defence and attack.\n\n"
    "• Defensive midfielders protect the defence and win the ball.\n"
    "• Central midfielders pass the ball and keep the team balanced.\n"
    "• Attacking midfielders create chances near the opponent's goal.\n\n"
    "The midfield is often called the 'engine room'.")

add("winger", "positions", "Winger",
    ["winger", "wing", "wide player"],
    "<b>Wingers</b> play wide on the left or right. They dribble past defenders, cross the ball for the strikers "
    "and sometimes cut inside to shoot. Speed and skill matter most.")

add("striker", "positions", "Striker",
    ["striker", "centre forward", "center forward", "forward", "number 9", "attacker"],
    "<b>Strikers</b> (centre-forwards) play at the front. Their main job is to score goals: finishing chances, "
    "holding the ball up for teammates and running behind defenders.")

# ------------------------------------------------------------------ TERMS
add("cleansheet", "terms", "Clean sheet",
    ["clean sheet", "cleansheet", "shutout"],
    "A <b>clean sheet</b> means a team finished a match without conceding a goal. It's a big achievement for the goalkeeper and defence.")

add("hattrick", "terms", "Hat-trick",
    ["hat trick", "hattrick"],
    "A <b>hat-trick</b> is when one player scores three goals in a single match. The word comes from cricket.")

add("brace", "terms", "Brace",
    ["brace", "double", "scored twice"],
    "A <b>brace</b> is two goals scored by one player in a match.")

add("assist", "terms", "Assist",
    ["assist", "assists"],
    "An <b>assist</b> is the final pass or action that directly leads to a goal.")

add("nutmeg", "terms", "Nutmeg",
    ["nutmeg", "megs", "through the legs"],
    "A <b>nutmeg</b> is when you kick the ball through an opponent's legs and collect it on the other side. "
    "It's a skill move that fans love (and a bit embarrassing for the player it's done to 😄).")

add("derby", "terms", "Derby",
    ["derby", "local derby", "rivalry", "rivals", "el clasico", "clasico"],
    "A <b>derby</b> is a match between two local rival teams, often from the same city or area, like the Manchester derby or the Milan derby.\n\n"
    "Fans care a lot about these games, and form often goes out of the window.")

add("transferwindow", "terms", "Transfer window",
    ["transfer window", "transfer", "transfers", "signing", "buy player"],
    "The <b>transfer window</b> is the period when clubs can buy and sell players. Most leagues have two windows a year: "
    "a longer one in the summer and a shorter one in January. The exact dates vary by country.")

add("loan", "terms", "Loan",
    ["loan", "on loan", "loan deal"],
    "A <b>loan</b> is when a club lets a player play for another club for a set time (like one season) while still owning the player. "
    "It helps young players get regular matches.")

add("relegation", "terms", "Relegation and promotion",
    ["relegation", "relegated", "promotion", "promoted", "go down", "go up"],
    "<b>Relegation</b> means the worst teams in a league are moved down to a lower division at the end of the season. "
    "<b>Promotion</b> is the opposite: the best teams from the lower division move up.\n\n"
    "How many teams go up or down depends on the league.")

add("aggregate", "terms", "Aggregate",
    ["aggregate", "two legs", "two leg", "away goals", "first leg", "second leg"],
    "<b>Aggregate</b> means the total score over two matches (two legs) in a knockout tie, one at each team's home. "
    "The team with the higher total goes through.\n\n"
    "The away goals rule, which used to break ties, has not been used in UEFA competitions since 2021.")

add("owngoal", "terms", "Own goal",
    ["own goal", "owngoal"],
    "An <b>own goal</b> is when a player accidentally puts the ball into their own team's net. The goal counts for the other team.")

add("goldenboot", "terms", "Golden Boot",
    ["golden boot", "golden shoe", "top scorer", "top goalscorer"],
    "The <b>Golden Boot</b> is the award for the top goalscorer in a league or tournament.")

add("captain", "terms", "Captain",
    ["captain", "armband", "skipper"],
    "The <b>captain</b> wears an armband, leads the team on the pitch and is the player who normally talks to the referee on the team's behalf.")

add("bicycle", "terms", "Bicycle kick",
    ["bicycle kick", "overhead kick", "scissor kick"],
    "A <b>bicycle kick</b> (overhead kick) is when a player jumps, leans back and kicks the ball over their own head. "
    "It's one of the most spectacular ways to score.")

add("panenka", "terms", "Panenka",
    ["panenka", "chipped penalty"],
    "A <b>Panenka</b> is a penalty where the taker chips the ball softly down the middle, hoping the goalkeeper has already dived.\n\n"
    "It's named after Antonin Panenka, who scored one this way in the shootout of the Euro 1976 final.")

add("rabona", "terms", "Rabona",
    ["rabona"],
    "A <b>rabona</b> is a kick where the player wraps their kicking leg behind their standing leg to pass, cross or shoot. It looks very stylish.")

# --------------------------------------------------------------- LEGENDS
add("worldcup", "legends", "The World Cup",
    ["world cup", "worldcup", "fifa world cup"],
    "The <b>World Cup</b> is the biggest football tournament, for national teams, held every four years.\n\n"
    "The first one was in 1930 in Uruguay, and Uruguay won it. The 2026 tournament was the first with 48 teams, "
    "hosted by the USA, Canada and Mexico. Brazil, Germany, Italy and Argentina are among the most successful nations.")

add("pele", "legends", "Pelé",
    ["pele", "edson arantes"],
    "<b>Pelé</b> (Brazil) is one of the greatest players ever. He won the World Cup three times (1958, 1962 and 1970), "
    "which no other player has done. He was famous for his goals, skill and joyful style.")

add("maradona", "legends", "Diego Maradona",
    ["maradona", "diego maradona", "hand of god"],
    "<b>Diego Maradona</b> (Argentina) captained his country to the 1986 World Cup title.\n\n"
    "In the quarter-final against England he scored two of the most famous goals ever: the controversial 'Hand of God' "
    "and, minutes later, the 'Goal of the Century', a solo run past most of the England team.")

add("messi", "legends", "Lionel Messi",
    ["messi", "lionel messi", "leo messi"],
    "<b>Lionel Messi</b> (Argentina) spent most of his career at Barcelona and has won a record eight Ballon d'Or awards.\n\n"
    "In 2022 he finally won the World Cup with Argentina, beating France in a thrilling final that went to penalties.")

add("ronaldo", "legends", "Ronaldo",
    ["ronaldo", "cr7", "cristiano", "r9", "ronaldo nazario"],
    "There are two famous Ronaldos:\n\n"
    "<b>Cristiano Ronaldo</b> (Portugal) has won five Ballon d'Or awards, plays with great power and heading ability, "
    "and is the record scorer in men's international football and in the Champions League.\n\n"
    "<b>Ronaldo Nazario 'R9'</b> (Brazil) was a lightning-fast striker who won the World Cup in 2002 and finished as its top scorer.")

add("goat", "legends", "Greatest of all time",
    ["goat", "greatest of all time", "best player", "best player ever", "greatest player",
     "messi vs ronaldo", "ronaldo vs messi", "messi or ronaldo", "ronaldo or messi"],
    "Who's the greatest of all time? It's the biggest debate in football 😄\n\n"
    "Fans argue for <b>Pelé</b> (three World Cups), <b>Maradona</b> (carried Argentina to the 1986 title), "
    "<b>Messi</b> (eight Ballon d'Ors and the 2022 World Cup) and <b>Cristiano Ronaldo</b> (goals and trophies in several countries).\n\n"
    "There's no official answer. Who's your pick?")

add("ucl", "legends", "Champions League",
    ["champions league", "ucl", "european cup"],
    "The <b>UEFA Champions League</b> is Europe's top club competition. The best teams from European leagues play in a "
    "league phase and then knockout rounds, and the winner lifts the famous trophy nicknamed 'Big Ears'.\n\n"
    "Real Madrid have won it more times than any other club.")

add("premierleague", "legends", "Premier League",
    ["premier league", "epl", "english league", "england league"],
    "The <b>Premier League</b> is England's top division, started in 1992. It has 20 clubs and is watched all over the world. "
    "The bottom three clubs are relegated at the end of each season.")

add("ballondor", "legends", "Ballon d'Or",
    ["ballon", "ballon d or", "ballondor", "player of the year"],
    "The <b>Ballon d'Or</b> is the yearly award for the best player in the world, started by France Football magazine in 1956. "
    "Lionel Messi has won it the most times (eight).")

add("afcon", "legends", "Africa Cup of Nations",
    ["afcon", "africa cup of nations", "african cup of nations", "super eagles", "african football"],
    "The <b>Africa Cup of Nations (AFCON)</b> is the biggest tournament for African national teams. "
    "Egypt has won it more times than any other country, and Nigeria's Super Eagles lifted the trophy in 1980, 1994 and 2013.")

add("euros", "legends", "The Euros",
    ["euro", "euros", "european championship", "uefa euro"],
    "The <b>European Championship (the Euros)</b> is a tournament for European national teams held every four years. "
    "Spain has won it more times than any other country.")

# ------------------------------------------------------------ SMALL TALK
add("greet", "chat", "Hello",
    ["hi", "hello", "hey", "yo", "hola", "howdy", "good morning", "good afternoon", "good evening", "sup"],
    ["Hey there! ⚽ Ask me anything about football, or pick a topic below.",
     "Hello! 👋 Ready to talk football? Ask about rules, tactics or legends.",
     "Hi! ⚽ What do you want to know about football today?"])

add("thanks", "chat", "Thanks",
    ["thanks", "thank you", "thx", "cheers", "ty", "appreciate"],
    ["You're welcome! ⚽ Got another football question?",
     "Anytime! 🙌 Ask me more about football.",
     "Happy to help! What's next?"])

add("bye", "chat", "Bye",
    ["bye", "goodbye", "cya", "see you", "good night"],
    "See you later! ⚽ Come back anytime for more football talk.")

add("howareyou", "chat", "How are you",
    ["how are you", "how you doing", "how is it going", "whats up", "how r u"],
    "I'm in top form, like a striker on a hot streak! 🔥 What football question do you have?")

add("about", "chat", "About",
    ["who are you", "what are you", "your name", "what can you do", "help", "how do you work", "what do you know"],
    "I'm your <b>Football Buddy</b> ⚽ I only talk football!\n\n"
    "Ask me in your own words, for example:\n"
    "• what is offside?\n• explain the 4-3-3\n• who is Pelé?\n• what does a winger do?\n\n"
    "Tell me your club (<i>I support Arsenal</i>) and I'll remember it. Type /fact for a random fact or /menu for topics.")

add("joke", "chat", "Joke",
    ["joke", "funny", "make me laugh", "banter"],
    ["Why are football stadiums always cool? Because every seat has a fan! 🌀",
     "Why did the footballer bring a ladder to the match? He wanted to reach the top of the league! 🪜",
     "Why can't Cinderella play football? She keeps running away from the ball! 👠"])

add("live", "chat", "Live info",
    ["live score", "live scores", "score tonight", "fixture", "fixtures", "results", "standings", "league table",
     "who will win", "predict", "prediction", "transfer news", "latest news", "news", "tonight"],
    "I don't have live scores, fixtures or news, I'm a football knowledge bot 📚\n\n"
    "But I can explain rules, tactics, positions, football words and legends. Pick a topic below!")

# ------------------------------------------------------------------ FACTS
FACTS = [
    "A standard football goal is 7.32 metres wide and 2.44 metres high.",
    "The first World Cup was played in 1930 in Uruguay.",
    "Pelé is the only player to win the World Cup three times.",
    "Yellow and red cards were first used at the 1970 World Cup. They were invented by English referee Ken Aston.",
    "A goal scored directly from a corner kick is nicknamed an 'Olimpico'.",
    "The word 'hat-trick' comes from cricket, where a bowler taking three wickets in a row was rewarded with a new hat.",
    "A penalty spot is 11 metres (12 yards) from the goal line.",
    "A size-5 match ball is about 68 to 70 centimetres around.",
    "Goal-line technology was first used at the World Cup in 2014.",
    "The Laws of the Game are looked after by a body called IFAB.",
    "International match pitches are between 100 and 110 metres long.",
    "The goalkeeper wears a different colour so the referee and players can spot them quickly.",
]

BY_ID = {e["id"]: e for e in KB}
