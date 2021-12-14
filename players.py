# A2 - Players and scores

import deck as d

def initPlayers(n, bal = 100):
    players = {}
    for i in range(n):
        name = input("Name of player " + str(i + 1) + ": ")
        players[name] = {
            'score'        : [],
            'wins'         : 0,
            'balance'      : bal,
            'stillPlaying' : True,
            'bet'          : [0],
            'hand'         : [],
            'isBot'        : False
        }
        isBot = input("Is " + name + " a human or a bot [h/B]? ").lower() in ["b", "bot"]
        players[name]['isBot'] = isBot
        if players[name]['isBot'] == True:
            playfullness = False
            while type(playfullness) != float:
                try:
                    inp = float(input("Enter the bot risk-averse scale (enter a percentage between 0 and 100) : "))
                except ValueError:
                    print("The value should be a real number between 0 and 100")
                else :
                    if 0 <= inp <= 100:
                        playfullness = inp
                    else:
                        print("The value should be a real number between 0 and 100")
                    
            players[name]['strategy'] = playfullness

    return players

# By default the players' scores are initialized as null by "initPlayers" function
def firstTurn(players, deck):
    flag = False
    print()
    for i, (name, player) in enumerate(players.items()):
        botString = " ; Bot"
        humanString = " ; Human"
        form = f"┤ Round 1 ; Player: {name}{botString if players[name]['isBot'] == True else humanString} ├"
        if i == 0:
            print(f"{form:{'─'}^80s}" + "\b╮\r╭")
        else:
            print(f"{form:{'─'}^80s}" + "\b┤\r├")                                   
        c = d.drawCard(deck, len(players), 2)
        drawText = f"│{name}'s first draw: {c[0]} {c[1]}"
        print(f"{drawText:<80s}" + "\b│")
        player["hand"] = c
        player["score"][-1] = d.calcScore(player["hand"])
        flag = flag or (player["score"][-1] == 21)
    return flag

def winner(players, croupier):
    winners = []
    for n, p in players.items():
        if 21 >= p["score"][-1] and (p["score"][-1] >= croupier["score"] or croupier["score"] > 21):
            winners.append(n)
    
    return winners



