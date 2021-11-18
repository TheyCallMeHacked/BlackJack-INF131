import deck

def playerAction(bet, canDouble): # Renamed continue() to playerAction() because continue is a key-word. Also added 
    action = input("Your action [hit, stand" + (", double down" if canDouble else "") + "]: ").lower()
    if action in ["double", "double down", "d"] and not canDouble:
        print("Your balance is too low to double down.")
        action = ""
    while action not in ["hit", "h",                    # Hit = Croupier draws a new card for that player
                         "stand", "s",                  # Stand = The player takes no more cards
                         "double", "double down", "d"]: # Double Down = The player's bet is doubled and the croupier draws an other card for that player
        action = input("Your action [hit, stand" + (", double down" if canDouble else "") + "]: ").lower()
        if action in ["double", "double down", "d"] and not canDouble:
            print("Your balance is too low to double down.")
            action = ""
    
    if action in ["stand", "s"]:
        return False
    if action in ["double", "double down", "d"]:
        bet[0] *= 2
    return True

def playerTurn(player, playerName, turnNumber, d):
    print("-"*5 + "|", "Round", turnNumber, "; Player:", playerName, "; Score:", player["score"][-1], "|" + "-"*5)
    canDouble = (player["bet"][0]*2) <= player["balance"]
    con = playerAction(player["bet"], canDouble)
    if con:
        c = deck.valueCard(deck.drawCard(d))
        c = 11 if c == 1 and player["score"][-1] > 10 else c
        player["score"][-1] += c
        if player["score"][-1] >= 21:
            player["stillPlaying"] = False
        return
    player["stillPlaying"] = False

    
    