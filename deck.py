import random

# A1 - Cards deck
def deck():
    fig = ["A"] + [str(i+1) for i in range(10)] + ["J", "Q", "K"]
    colours = ["♥", "♦", "♣", "♠"]
    out = []
    for i in colours:
        for j in fig:
            out.append(i+j)
    return out

def valueCard(card):
    if card[0] not in "♥♦♣♠" or type(card) != str or int(card[1:]) < 2 or int(card[1:]) > 10:
        raise ValueError("Invalid card format")
    try:
        return int(card[1:])
    except ValueError:
        if card[1:] == "A":
            return 1
        if card[1:] in ["J","Q","K"]:
            return 10
    raise ValueError("Invalid card format")

def initStack(n):
    d = []
    for _ in range(n):
        d += deck()
    return random.shuffle(d)

def drawCard(deck,x=1):
    return [deck.pop[i] for i in range(x)]
    
