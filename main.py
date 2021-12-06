#!/bin/python

import players as p
import deck as d
import game_management as gm
import sys

def main(argv):
    n = int(input("How many players will play? "))
    if len(argv) > 1:
        players = p.initPlayers(n, int(argv[1]))
    else:
        players = p.initPlayers(n)
    playing = True
    while playing:
        deck = d.initStack(n)
        gm.completeGame(players, deck)
        playing = input("replay? [y/N] ").lower() in ["yes", "y"]
        if playing and players == {}:
            print("No players have money anymore, exiting.")
            return
    
    form = f"┤ Recap for players that didn't go broke ├"
    print(f"{form:{'─'}^80s}" + "\b╮\r╭")
    for name, player in players.items():
        form = f"│{name} won {player['wins']} game{'' if player['wins'] == 1 else 's'} out of {len(player['score'])} with a final balance of ${player['balance']:.2f}"
        print(f"{form:{' '}<80s}" + "\b│")
    print(f"{'':{'─'}^80s}" + "\b╯\r╰")



if __name__ == "__main__":
    main(sys.argv)
