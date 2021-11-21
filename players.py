# A2 - Players and scores

import deck as d

# The players'scores are already given by initPlayer function so defining a "initScores" \
# function is not necessary 

def initPlayers(n, bal = 0):
    players = {}
    for i in range(n):
        name = input("Name of player " + str(i + 1) + ':')
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
    for player in players:
        s = d.valueCard(d.drawCard(deck))
        s = 11 if s == 1 else s
        t = d.valueCard(d.drawCard(deck))
        t = 11 if s > 10 and t == 1 else s
        player.score[0] = s + t

def winner(players):
    maxScore = 0
    maxPlayer = ""
    for n, p in players.items():
        if 21 >= p.score[-1] > maxScore:
            maxScore = p.score[-1]
            maxPlayer = n
    
    return maxScore, maxPlayer



