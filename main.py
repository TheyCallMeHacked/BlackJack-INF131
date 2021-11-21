import players as p
import deck as d
import game_management as gm

def main():
    n = int(input("How many players will play? "))
    players = p.initPlayers(n)
    playing = True
    while playing:
        deck = d.deck()
        gm.completeGame(players, deck)
        playing = input("replay? [y/N] ").lower() in ["yes", "y"]



if __name__ == "__main__":
    main()
