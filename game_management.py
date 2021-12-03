import deck as d
import players as p
import croupier as c

def playerAction(bet, canDouble): # Renamed continue() to playerAction() because continue is a key-word. Also added 
    prompt = "│Your action [hit, stand" + (", double down" if canDouble else "") + "]: "
    noDoubleString = "│Your balance is too low to double down."
    action = input(f"{' ':{' '}<80s}" + "\b│\r" + prompt).lower()
    if action in ["double", "double down", "d"] and not canDouble:
        print(f"{noDoubleString:{' '}<80s}" + "\b│")
        action = ""
    while action not in ["hit", "h",                    # Hit = Croupier draws a new card for that player
                         "stand", "s",                  # Stand = The player takes no more cards
                         "double", "double down", "d"]: # Double Down = The player's bet is doubled and the croupier draws an other card for that player
        action = input(f"{' ':{' '}<80s}" + "\b│\r" + prompt).lower()
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
        c = d.drawCard(deck, nPlayers)[0]
        drawText = f"│{playerName}'s draw: {c}"
        print(f"{drawText:<80s}" + "\b│")
        player["hand"].append(c)
        player["score"][-1] = d.calcScore(player["hand"])
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
    croupier = c.initCroupier()
    for name,player in players.items():
        player["score"].append(0)
        player["stillPlaying"] = True
        sanitised = False
        while not sanitised:
            bal = player["balance"]
            bet = input(f"{name}'s bet (balance: ${bal:.2f}): ").split('.')     # splitting the input in integer and decimal part
            if len(bet) > 2 or len(bet) < 0:                                    # if there are more than two elements in the list, the input was not a valid real number
                print("Invalid value")
            else:                                                               # otherwise, the input sanitisation can continue
                flag = True                                                     # test if all the inputed characters (excluding the decimal point) were digits
                for i in ''.join(bet):
                    if i not in "0123456789":
                        flag = False
                if flag:                                                        # if it's the case, the input is finally sanitised and can be processed
                    bet = float('.'.join(bet))
                    if bet > bal or bet < 5:                                    # cannot bet more than you own or less than $5
                        print("Invalid value")
                    else:
                        player["bet"] = [bet]
                        sanitised = True
                else:                                                           # otherwise the input was not a valid number
                    print("Invalid value")

    blackJack = False
    if p.firstTurn(players, deck):
        blackJack = True
        for _,player in players.items():
            player["stillPlaying"] = False
    c.firstTurn(croupier, deck, len(players))

    i = 2
    while not gameOver(players):
        gameTurn(players, i, deck)
        i += 1
    if not blackJack:
        c.play(croupier, deck, len(players)) # when every player has standed or busted, it's the croupier's turn

    winners = p.winner(players, croupier)

    broke = []
    for name, player in players.items():
        if name in winners:
            player["wins"] += 1
            player["balance"] += player["bet"][0] + blackJack*0.5*player["bet"][0]
        else:
            player["balance"] -= player["bet"][0]
            if player["balance"] == 0:
                broke.append(name)
    for name in broke:
        del players[name]

    if len(winners):
        form = f"┤ Game Over ; {', '.join(winners)} won the game {'with a Black Jack ' if blackJack else ''}against the house ├"
    else:
        form = f"┤ Game Over ; All players lost to the house ├"

    print(f"{form:{'─'}^80s}" + "\b╯\r╰")