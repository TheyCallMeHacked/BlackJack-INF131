# A2 - Players and scores

import deck as d

# The players'scores are already given by initPlayer function so defining a "initScores" \
# function is not necessary 

def initPlayers(n, bal = 0):
    players = {}
    for i in range(n):
        name = input("Name of player " + str(i + 1) + ": ")
        players[name] = {
            'score'        : [],
            'wins'         : 0,
            'balance'      : bal,
            'stillPlaying' : True,
            'bet'          : [0]
        }
    return players

# By default the players' scores are initialized as null by "initPlayers" function
def firstTurn(players, deck):
    flag = True
    for name, player in players.items():
        print("─"*5 + "┤", "Round 1", "; Player:", name, "├" + "─"*5)
        c = d.drawCard(deck, 2)
        print(name + "'s", "first draw:", c[0], c[1])
        s = d.valueCard(c[0])
        s = 11 if s == 1 else s
        t = d.valueCard(c[1])
        t = 11 if (s > 10 and t == 1) else t
        player["score"][-1] = s + t
        flag = flag or (s + t == 21)
    return not(flag)

def winner(players):
    maxScore = 0
    maxPlayer = []
    for n, p in players.items():
        if 21 >= p["score"][-1] > maxScore:
            maxScore = p["score"][-1]
            maxPlayer = [n]
        elif p["score"][-1] == maxScore:
            maxPlayer.append(n)
    
    return maxScore, maxPlayer



