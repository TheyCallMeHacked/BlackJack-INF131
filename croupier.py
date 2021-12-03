import deck as d

def initCroupier():
    croupier = {
        "up"    : [],
        "down"  : "",
        "score" : 0,
        "hard"  : False
    }
    return croupier

def firstTurn(croupier, deck, nPlayers):
    cards = d.drawCard(deck, nPlayers, 2)
    croupier["up"].append(cards[0])
    croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)
    croupier["down"] = cards[1]
    form = f"┤ Round 1 ; Croupier ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")
    drawText = f"│Croupier's first draw: {cards[0]} █"
    print(f"{drawText:<80s}" + "\b│")

def play(croupier, deck, nPlayers):
    stillPlaying = True
    form = f"┤ Croupier's turn ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")    

    drawText = f"│Croupier's down card: {croupier['down']}"                              # showing the croupier's down card
    print(f"{drawText:<80s}" + "\b│")
    croupier["up"].append(croupier["down"])                                              # adding it to the up cards

    croupier["score"], croupier["hard"] = d.calcScore(croupier["up"], True)              # adding it to the score

    
    while stillPlaying:
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


    drawText = f"│Croupier's hand: {' '.join(croupier['up'])}"                           # showing the croupier's hand
    print(f"{drawText:<80s}" + "\b│") 