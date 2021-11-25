import deck as d
import players as p

def playerAction(): # Renamed continue() to playerAction() because continue is a key-word. Also added 
    action = input("Your action [hit, stand]: ").lower()
    while action not in ["hit", "h",                    # Hit = Croupier draws a new card for that player
                         "stand", "s"]:                 # Stand = The player takes no more cards
        action = input("Your action [hit, stand]: ").lower()
    
    if action in ["stand", "s"]:
        return False
    return True

# @ param
# player: the player object
# playerName: the player's name
# turnNumber: current turn number to be printed
# deck: the deck of cards
def playerTurn(player, playerName, turnNumber, deck):
    print("─"*5 + "┤", "Round", turnNumber, "; Player:", playerName, "; Score:", player["score"][-1], "├" + "─"*5)
    con = playerAction()
    if con:
        c = d.drawCard(deck)
        print(playerName+"'s", "draw:", c[0])
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
# d: the deck of cards   
def gameTurn(players, turnNumber, deck):
    for name, player in players.items():
        if player["stillPlaying"]:
            playerTurn(player, name, turnNumber, deck)

def gameOver(players):
    flag = True
    for _,player in players.items():
        flag = flag and not(player["stillPlaying"])
    return flag

# @param
# d: the deck of cards
def completeGame(players, deck):
    for _,player in players.items():
        player["score"].append(0)
    if p.firstTurn(players, deck):
        for _,player in players.items():
            player["stillPlaying"] = False
    i = 0
    while not gameOver(players):
        gameTurn(players, i, deck)
        i += 1
    score, win = p.winner(players)
    print("─"*5 + "┤", "Game Over ;", end=' ')
    if score:
        for w in win:
            print(w, end=", ")
        print("\b\b won the game with a score of", score, end=' ')
    else:
        print("Nobody won this game", end=' ')
    print("├" + "─"*5)
