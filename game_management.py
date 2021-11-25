import deck as d
import players as p

def playerAction(bet, canDouble): # Renamed continue() to playerAction() because continue is a key-word. Also added 
    prompt = "│Your action [hit, stand" + (", double down" if canDouble else "") + "]: "
    noDoubleString = "│Your balance is too low to double down."
    action = input(f"{prompt:{' '}<80s}" + "\b│\r\t\t\t\t" + ("\t" if canDouble else "")).lower()
    if action in ["double", "double down", "d"] and not canDouble:
        print(f"{noDoubleString:{' '}<80s}" + "\b│")
        action = ""
    while action not in ["hit", "h",                    # Hit = Croupier draws a new card for that player
                         "stand", "s",                  # Stand = The player takes no more cards
                         "double", "double down", "d"]: # Double Down = The player's bet is doubled and the croupier draws an other card for that player
        action = ininput(f"{prompt:{' '}<80s}" + "\b│\r\t\t\t\t" + ("\t" if canDouble else "")).lower()
        if action in ["double", "double down", "d"] and not canDouble:
            print(f"{noDoubleString:{' '}<80s}" + "\b│")
            action = ""
    
    if action in ["stand", "s"]:
        return False
    if action in ["double", "double down", "d"]:
        bet[0] *= 2
    return True

# @ param
# player: the player object
# playerName: the player's name
# turnNumber: current turn number to be printed
# deck: the deck of cards
def playerTurn(player, playerName, turnNumber, deck, nPlayers):
    score = player["score"][-1]
    form = f"┤ Round {turnNumber} ; Player: {playerName} ; Score: {score} ├"
    print(f"{form:{'─'}^80s}" + "\b┤\r├")
    canDouble = (player["bet"][0]*2) <= player["balance"]
    con = playerAction(player["bet"], canDouble)
    if con:
        c = d.drawCard(deck, nPlayers)
        drawText = f"│{playerName}'s fist draw: {c[0]}"
        print(f"{drawText:<80s}" + "\b│")
        v = d.valueCard(c[0])
        v = 11 if (v == 1 and player["score"][-1] > 10) else v
        player["score"][-1] += v
        if player["score"][-1] >= 21:
            player["stillPlaying"] = False
        return
    player["stillPlaying"] = False

# @ param
# player: the player object
# turnNumber: current turn number to be printed
# deck: the deck of cards   
def gameTurn(players, turnNumber, deck):
    for name, player in players.items():
        if player["stillPlaying"]:
            playerTurn(player, name, turnNumber, deck, len(players))

def gameOver(players):
    flag = True
    for _,player in players.items():
        flag = flag and not(player["stillPlaying"])
    return flag

# @param
# d: the deck of cards
def completeGame(players, deck):
    for name,player in players.items():
        player["score"].append(0)
        player["stillPlaying"] = True
        sanitized = False
        while not sanitized:
            try:
                bal = player["balance"]
                bet = float(input(f"{name}'s bet (balance: ${bal:.2f}): "))
                if bet <= 0:
                    raise ValueError
                player["bet"] = [bet]
                sanitized = True
            except:
                print("Invalid value")


    if p.firstTurn(players, deck):
        for _,player in players.items():
            player["stillPlaying"] = False
    i = 2
    while not gameOver(players):
        gameTurn(players, i, deck)
        i += 1
    score, winners = p.winner(players)

    for name, player in players.items():
        if name in winners:
            player["wins"] += 1
            player["balance"] += player["bet"][0]
        else:
            player["balance"] -= player["bet"][0]
    
    if score:
        form = f"┤ Game Over ; {' '.join(winners)} won the game with {score} points ├"
    else:
        form = f"┤ Game Over ; Nobody won ├"

    print(f"{form:{'─'}^80s}" + "\b┘\r└")