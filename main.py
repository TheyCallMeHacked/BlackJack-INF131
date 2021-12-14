#!/bin/python

import deck as d
import gui
from tkinter import *
from tkinter import ttk, messagebox

import sys
from threading import Thread
from time import sleep

def main(argv, nogui=False):
    if nogui:
        n = ""
        while type(n) != int:
            try:
                inp = int(input("How many players will play? "))
            except ValueError:
                pass
            else:
                if 0 < inp <= 5:
                    n = inp
    else:
        root, casinoTable, uname, bal, score, bet = gui.generateGUI()

        def dismiss():
            dlg.grab_release()
            dlg.destroy()

        n = [1]
        def retrieve(*arg):
            try:
                n[0] = int(n_player.get())
            except:
                pass
            else:
                if 0 < n[0] <= 5:
                    dismiss()

        dlg = Toplevel(root)
        ttk.Label(dlg, text="Number of players:").grid(column=0, row=0, padx=5, pady=5)
        n_player = StringVar()
        n_entry = ttk.Entry(dlg, textvariable=n_player)
        n_entry.grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(dlg, text="Submit", command=retrieve).grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(root)   # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set()        # ensure all input goes to our window
        n_entry.focus()
        dlg.bind("<Return>", retrieve)
        dlg.wait_window()     # block until window is destroyed

        n = n[0]
    
    if len(argv) > 1:
        players = p.initPlayers(n, root, int(argv[1]))
    else:
        players = p.initPlayers(n, root)
    deck = d.initStack(n)
    
    if nogui:
        playing = True
        while playing:
            gm.completeGame(players, deck)
            playing = input("replay? [y/N] ").lower() in ["yes", "y"]
            if playing and players == {}:
                print("No players have got money anymore, exiting.")
                playing = False


        form = f"┤ Recap for players that didn't go broke ├"
        print(f"{form:{'─'}^80s}" + "\b╮\r╭")
        for name, player in players.items():
            form = f"│{name} won {player['wins']} game{'' if player['wins'] == 1 else 's'} out of {len(player['score'])} with a final balance of ${player['balance']:.2f}"
            print(f"{form:{' '}<80s}" + "\b│")
        print(f"{'':{'─'}^80s}" + "\b╯\r╰")
    else:
        t = Thread(target=game, args=(players, deck, root, casinoTable, uname, bal, score, bet), daemon=True)
        t.start()
        root.mainloop()
        t.join(timeout=1)
        sys.exit()

    
def game(players, deck, root, casinoTable, uname, bal, score, bet):
    playing = True
    while playing:
        winners, blackJack = gm.completeGame(players, deck, {'root': root, 'table': casinoTable, 'uname': uname, 'bal':bal, 'score':score, 'bet':bet})
        if len(winners):
            form = f"Game Over : {', '.join(winners)} won the game {'with a Black Jack ' if blackJack else ''}against the house"
        else:
            form = f"Game Over : All players lost to the house"
        form += "\nReplay ?"
        playing = messagebox.askyesno(title="Replay?", message=form)
        if playing and players == {}:
            print("No players have got money anymore, exiting.")
            playing = False
    gui.recap(players, root)
    sleep(0.1)
    root.destroy()
    return

if __name__ == "__main__":
    nogui = "--no-gui" in sys.argv
    argv = sys.argv
    if nogui:
        for i,a in enumerate(sys.argv):
            if a == "--no-gui":
                argv.pop(i)
        import game_management_nogui as gm
        import players_no_gui as p
    else:
        import game_management as gm
        import players as p

    main(argv, nogui)
