#A2 - Players and scores

import deck

# The players'scores are already given by initPlayer function so defining a "initScores" \
# function is not necessary 

def initPlayers(n, v = 0):
    players = {}
    for i in range(n):
        name = input("Name of player " + str(i + 1) + ':')
        players[name] = {
            'score' : [],
            'wins' : 0,
            'balance' : v
        }
    return players

# By default the players' scores are initialized as null by "initPlayers" function
def firstTurn(players):
    for p in players:
        