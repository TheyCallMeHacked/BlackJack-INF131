# A2 - Players and scores

import deck as d
from tkinter import *
from tkinter import ttk

# The players'scores are already given by initPlayer function so defining a "initScores" \
# function is not necessary 

# The CLI initPlayers still takes a(n unused) root parameter to make main.py shorter and easier to read

def initPlayers(n, root = [], bal = 100):
    players = {}

    for i in range(n):
        name = input("Name of player " + str(i + 1) + ": ")

        players[name] = {
            'score'        : [],
            'wins'         : 0,
            'balance'      : bal,
            'stillPlaying' : True,
            'bet'          : [0],
            'hand'         : []
        }
    return players

# By default the players' scores are initialized as null by "initPlayers" function
def firstTurn(players, deck):
    flag = False
    for i, (name, player) in enumerate(players.items()):
        form = f"┤ Round 1 ; Player: {name} ├"
        if i == 0:
            print(f"{form:{'─'}^80s}" + "\b╮\r╭")
        else:
            print(f"{form:{'─'}^80s}" + "\b┤\r├")
        c = d.drawCard(deck, len(players), 2)
        drawText = f"│{name}'s fist draw: {c[0]} {c[1]}"
        print(f"{drawText:<80s}" + "\b│")
        player["hand"] = c
        player["score"][-1] = d.calcScore(player["hand"])
        flag = flag or (player["score"][-1] == 21)
    return flag

def winner(players, croupier, blackJack):
    winners = []
    for n, p in players.items():
        if blackJack:
            if p["score"][-1] == 21:
                winners.append(n)
        else:
            if 21 >= p["score"][-1] and (p["score"][-1] >= croupier["score"] or croupier["score"] > 21):
                winners.append(n)
    
    return winners



