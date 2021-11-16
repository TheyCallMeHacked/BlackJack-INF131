import random

# A1 - Cards deck
def deck():
    fig = ["A"] + [str(i+1) for i in range(10)] + ["J", "Q", "K"]
    colours = ["♥", "♦", "♣", "♠"]
    out = []
    for i in fig:
        for j in colours:
            out.append(i+j)
    return out

def valueCard(card):
    if card[1] not in "♥♦♣♠" or len(card) != 2 or type(card) != str or int(card[0]) < 2:
        raise ValueError("Invalid card format")
    try:
        return int(card[0])
    except ValueError:
        if card[0] == "A":
            return 1,11
        if card[0] in "JQK":
            return 10
    raise ValueError("Invalid card format")

def initStack(n):
    d = []
    for _ in range(n):
        d += deck()
    return random.shuffle(d)

def drawCard(p,x=1):
    return [p.pop[i] for i in range(x)]
    
