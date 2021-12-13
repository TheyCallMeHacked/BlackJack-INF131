import deck as d
import players as p
import croupier as c
import gui as g
from tkinter import *
from tkinter import ttk

def playerAction(bet, canDouble, root): # Renamed continue() to playerAction() because continue is a key-word. Also added possibility to double down
    if not canDouble:
        g.setCannotDouble()
    else:
        g.setCanDouble()
    
    root.update()

    action = ""
    while action == "":
        action = g.getAction()
    
    if action in ["stand", "s"]:
        return False
    if action in ["double", "double down", "d"]:
        bet[0] *= 2
    return True

# @ param
# player: the player object
# playerName: the player's name
# turnNumber: current turn number to be printed
# deck: the deck of cards
def playerTurn(player, playerName, playerNum, turnNumber, deck, nPlayers, gui):
    score = player["score"][-1]

    root, casinoTable, uname, balText, scoreText, betText = gui.values()
    uname.set(playerName)
    balText.set(f"${player['balance']:.2f}")
    scoreText.set(score)
    betText.set(f"${player['bet'][0]:.2f}")
    
    canDouble = (player["bet"][0]*2) <= player["balance"]
    con = playerAction(player["bet"], canDouble, root)
    if con:
        c = d.drawCard(deck, nPlayers)[0]
        g.addCard(casinoTable, playerNum, nPlayers, c, turnNumber)
        player["hand"].append(c)
        player["score"][-1] = d.calcScore(player["hand"])
        if player["score"][-1] >= 21:
            player["stillPlaying"] = False
        return
    player["stillPlaying"] = False

# @ param
# player: the player object
# turnNumber: current turn number to be printed
# deck: the deck of cards   
def gameTurn(players, turnNumber, deck, gui):
    for i, (name, player) in enumerate(players.items()):
        if player["stillPlaying"]:
            playerTurn(player, name, i+1, turnNumber, deck, len(players), gui)

def gameOver(players):
    flag = True
    for _,player in players.items():
        flag = flag and not(player["stillPlaying"])
    return flag

# @param
# d: the deck of cards
def completeGame(players, deck, gui):
    root, table, _,_,_,_ = list(gui.values())
    g.resetTable()

    croupier = c.initCroupier()
    for name,player in players.items():
        player["score"].append(0)
        player["stillPlaying"] = True
        bal = player["balance"]
        
        def dismiss():
            dlg.grab_release()
            dlg.destroy()

        bet = [5]
        def retrieve(*arg):
            try:
                bet[0] = float(bet_player.get())
            except:
                pass
            else:
                if 0 < bet[0] <= bal:
                    dismiss()

        dlg = Toplevel(root)
        ttk.Label(dlg, text=f"{name}'s bet (balance: ${bal:.2f}): ").grid(column=0, row=0, padx=5, pady=5)
        bet_player = StringVar()
        bet_entry = ttk.Entry(dlg, textvariable=bet_player)
        bet_entry.grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(dlg, text="Submit", command=retrieve).grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(root)   # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set()        # ensure all input goes to our window
        bet_entry.focus()
        dlg.bind("<Return>", retrieve)
        dlg.wait_window()     # block until window is destroyed

        player["bet"] = [bet[0]]

    blackJack = p.firstTurn(players, deck, table)
    if blackJack:
        for _,player in players.items():
            player["stillPlaying"] = False
    c.firstTurn(croupier, deck, len(players), table)

    i = 2
    while not gameOver(players):
        gameTurn(players, i, deck, gui)
        i += 1
    if not blackJack:
        c.play(croupier, deck, len(players), table, root) # when every player has standed or busted, it's the croupier's turn

    winners = p.winner(players, croupier, blackJack)

    broke = []
    for name, player in players.items():
        if name in winners:
            player["wins"] += 1
            player["balance"] += player["bet"][0] + blackJack*0.5*player["bet"][0]
        else:
            player["balance"] -= player["bet"][0]
            if player["balance"] == 0:
                broke.append(name)
    for name in broke:
        del players[name]

    if len(winners):
        form = f"┤ Game Over ; {', '.join(winners)} won the game {'with a Black Jack ' if blackJack else ''}against the house ├"
    else:
        form = f"┤ Game Over ; All players lost to the house ├"

    print(f"{form:{'─'}^80s}" + "\b╯\r╰")