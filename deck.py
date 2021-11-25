import random

# A1 - Cards deck
def deck():
    fig = ["A"] + [str(i+1) for i in range(1,10)] + ["J", "Q", "K"]
    colours = ["♥", "♦", "♣", "♠"]
    out = []
    for i in colours:
        for j in fig:
            out.append(i+j)
    return out

def valueCard(card):
    if card[0] not in "♥♦♣♠" or type(card) != str:
        raise ValueError("Invalid card format")
    try:
        if 2 <= int(card[1:]) <= 10:
            return int(card[1:])
        else:
            raise ValueError
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
    random.shuffle(d)
    return d

def drawCard(deck_, n, x=1):
    drawn = []
    for i in range(x):
        if len(deck_) == 0:
            deck_ = initStack(n)
        drawn.append(deck_.pop(0))
    return drawn
    
