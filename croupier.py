import deck as d

def initCroupier():
    croupier = {
        "up"    : [],
        "down"  : "",
        "score" : 0
    }
    return croupier

def firstTurn(croupier, deck, nPlayers):
    cards = d.drawCard(deck, nPlayers, 2)
    val = d.valueCard(cards[0])
    croupier["score"] = 11 if val == 1 else val
    croupier["up"].append(cards[0])
    croupier["down"] = cards[1]
    form = f"┤ Round 1 ; Croupier ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")
    drawText = f"│Croupier's first draw: {cards[0]} ██"
    print(f"{drawText:<80s}" + "\b│")

def play(croupier, deck):
    stillPlaying = True
    form = f"┤ Croupier's turn ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")

    value = d.valueCard(croupier["down"])
    croupier["score"] += 11 if (value == 1 and croupier["score"] < 11) else value # adding croupier's down card to score    

    drawText = f"│Croupier's down card: {croupier['down']}"                       # showing the croupier's down card
    print(f"{drawText:<80s}" + "\b│")
    croupier["up"].append(croupier["down"])                                       # adding it to the up cards

    
    while stillPlaying:
        if croupier["score"] < 17:                                                              # if croupier's hand below 17, hit
            card = d.drawCard(deck, nPlayers)[0]
            value = d.valueCard(card)
            croupier["score"] += 11 if (value == 1 and croupier["score"] < 11) else value
            if croupier["score"] >= 21:
                stillPlaying = False
            croupier["up"].append(card)
        elif croupier["score"] == 17:                                                           # if croupier's hand at 17, check if hard or soft 17 
            if croupier["up"] in ["♥A", "♦A", "♣A", "♠A"]:                                      # if soft 17, hit
                card = d.drawCard(deck, nPlayers)[0]
                value = d.valueCard(card)
                croupier["score"] += 11 if (value == 1 and croupier["score"] < 11) else value
                if croupier["score"] >= 21:
                    stillPlaying = False
                croupier["up"].append(card)
            else:                                                                               # if hard 17, stand
                stillPlaying = False
        else:                                                                                   # if dealer's hand above 17, stand
            stillPlaying = False


    drawText = f"│Croupier's hand: {' '.join(croupier['up'])}"                       # showing the croupier's hand
    print(f"{drawText:<80s}" + "\b│") 