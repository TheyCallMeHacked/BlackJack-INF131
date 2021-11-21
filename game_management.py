import deck as d
import players as p

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

# @ param
# player: the player object
# playerName: the player's name
# turnNumber: current turn number to be printed
# deck: the deck of cards
def playerTurn(player, playerName, turnNumber, deck):
    print("─"*5 + "┤", "Round", turnNumber, "; Player:", playerName, "; Score:", player["score"][-1], "├" + "─"*5)
    canDouble = (player["bet"][0]*2) <= player["balance"]
    con = playerAction(player["bet"], canDouble)
    if con:
        c = deck.valueCard(d.drawCard(deck))
        c = 11 if c == 1 and player["score"][-1] > 10 else c
        player["score"][-1] += c
        if player["score"][-1] >= 21:
            player["stillPlaying"] = False
        return
    player["stillPlaying"] = False

# @ param
# player: the player object
# turnNumber: current turn number to be printed
# d: the deck of cards   
def gameTurn(players, turnNumber, deck):
    for name, player in players.items():
        if player["stillPLaying"]:
            playerTurn(player, name, turnNumber, deck)

def gameOver(players):
    flag = True
    for player in players:
        flag = flag or not(player["stillPlaying"])
    return flag
# @param
# d: the deck of cards
def completeGame(players, deck):
    for _,player in players.items():
        players["score"].append(0)
    i = 0
    while not gameOver(players):
        gameTurn(players, i, deck)
        i += 1
    score, win = p.winner(players)
    print("─"*5 + "┤", "Game Over ;", win, "won the game with a score of", score, "├" + "─"*5)
    players[win]["wins"] += 1
