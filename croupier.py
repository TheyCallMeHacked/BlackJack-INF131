import deck as d
import gui as g
from time import sleep

def initCroupier():
    croupier = {
        "up"    : [],
        "down"  : "",
        "score" : 0,
        "hard"  : False
    }
    return croupier

def firstTurn(croupier, deck, nPlayers, table):
    cards = d.drawCard(deck, nPlayers, 2)
    croupier["up"].append(cards[0])
    croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)
    croupier["down"] = cards[1]
    form = f"┤ Round 1 ; Croupier ├"
    g.addCard(table, 0, nPlayers, "back", 1)
    g.addCard(table, 0, nPlayers, cards[0])

def play(croupier, deck, nPlayers, table, root):
    stillPlaying = True

    g.addCard(table, 0, nPlayers, croupier["down"], 1)                           # showing the croupier's down card
    croupier["up"].append(croupier["down"])                                      # adding it to the up cards
    croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)      # adding it to the score

    root.update()
    sleep(1)
    while stillPlaying:

        # Following Croupier Basic Strategy, as described in most croupier guides (only stand on hard 17 or higher):
        
        if croupier["score"] < 17:                                                       # if croupier's hand below 17, hit
            card = d.drawCard(deck, nPlayers)[0]
            croupier["up"].append(card)
            croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)
            if croupier["score"] >= 21:
                stillPlaying = False
        elif croupier["score"] == 17:                                                    # if croupier's hand at 17, check if hard or soft 17 
            if not croupier["hard"]:                                                     # if soft 17, hit
                card = d.drawCard(deck, nPlayers)[0]
                croupier["up"].append(card)
                croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)
                if croupier["score"] >= 21:
                    stillPlaying = False
            else:                                                                        # if hard 17, stand
                stillPlaying = False
        else:                                                                            # if dealer's hand above 17, stand
            stillPlaying = False


    for i, card in enumerate(croupier["up"][2:]):                           # showing the croupier's hand
        g.addCard(table, 0, nPlayers, card, i+2)