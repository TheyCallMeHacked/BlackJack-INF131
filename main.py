import players as p
import deck as d
import game_management as gm
import sys

def main(argv):
    n = int(input("How many players will play? "))
    if len(argv) > 1:
        players = p.initPlayers(n, argv[1])
    else:
        players = p.initPlayers(n)
    playing = True
    while playing:
        deck = d.initStack(n)
        gm.completeGame(players, deck)
        playing = input("replay? [y/N] ").lower() in ["yes", "y"]

if __name__ == "__main__":
    main(sys.argv)
