# A2 - Players and scores

import deck as d
from tkinter import *
from tkinter import ttk

# The players'scores are already given by initPlayer function so defining a "initScores" \
# function is not necessary 

def initPlayers(n, nogui = False, root = [], bal = 100):
    players = {}

    def dismiss():
            dlg.grab_release()
            dlg.destroy()

    name_var = [""]
    def retrieve(*arg):
        try:
            name_var[0] = name_player.get()
        except:
            pass
        else:
            dismiss()


    for i in range(n):
        if nogui:
            name = input("Name of player " + str(i + 1) + ": ")
        else:
            dlg = Toplevel(root)
            ttk.Label(dlg, text="Name of player " + str(i + 1) + ":").grid(column=0, row=0, padx=5, pady=5)
            name_player = StringVar()
            name_entry = ttk.Entry(dlg, textvariable=name_player)
            name_entry.grid(column=1, row=0, padx=5, pady=5)
            ttk.Button(dlg, text="Submit", command=retrieve).grid(column=0, row=1, columnspan=2, padx=5, pady=5)
            dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
            dlg.transient(root)   # dialog window is related to main
            dlg.wait_visibility() # can't grab until window appears, so we wait
            dlg.grab_set()        # ensure all input goes to our window
            name_entry.focus()
            dlg.bind("<Return>", retrieve)
            dlg.wait_window()     # block until window is destroyed

            name = name_var[0]

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



