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

def play(croupier):
    stillPlaying = True
    form = f"┤ Croupier's turn ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")

    value = d.valueCard(croupier["down"])
    croupier["score"] += 11 if (value == 1 and croupier["score"] < 11) else value # adding croupier's down card to score    

    drawText = f"│Croupier's down card: {croupier['down']}"                       # showing the croupier's down card
    print(f"{drawText:<80s}" + "\b│")
    croupier["up"].append(croupier["down"])                                       # adding it to the up cards

    
    while stillPlaying:
        stillPlaying = False