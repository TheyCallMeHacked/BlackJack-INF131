from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep

def hit(*arg):
    global action
    action = "h"

def stand(*arg):
    global action
    action = "s"

def double(*arg):
    global action
    action = "d"

def getAction():
    global action
    out = action
    action = ""
    return out

def generateGUI():
    # Generates the main window
    root = Tk()
    root.title("[INF131] Black Jack")
    #root.resizable(FALSE, FALSE)

    # Adds a frame for themed UI (tries to follow system theme, somewhat broken on Linux with the Xfce desktop environment)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)   # setup the frame to scale with the window horizontally
    root.rowconfigure(0, weight=1)      # setup the frame to scale with the window vertically

    # Creates the canvas for the Casino Table
    casinoTable = Canvas(mainframe, bg="green", width=1000, height=600)
    casinoTable.grid(column=0, row=0, sticky=(N, E, S, W))

    # Sets the user information panel up
    userinfo = ttk.Frame(mainframe)
    userinfo.grid(column=1, row=0, sticky=(N, E))
    uname = StringVar(value="<Username>")   # setup the string placeholder for the username
    bal = StringVar(value="<bal>")          # setup the string placeholder for the balance
    score = StringVar(value="<score>")      # setup the string placeholder for the score
    bet = StringVar(value="<bet>")          # setup the string placeholder for the bet
    # Adds the different labels
    ttk.Label(userinfo, font=25, textvariable=uname).grid(column=0, row=0, sticky=N, columnspan=2)
    ttk.Label(userinfo, text="Balance: ").grid(column=0, row=1, sticky=W)
    ttk.Label(userinfo, text="Score: ").grid(column=0, row=2, sticky=W)
    ttk.Label(userinfo, text="Bet: ").grid(column=0, row=3, sticky=W)
    ttk.Label(userinfo, textvariable=bal).grid(column=1, row=1, sticky=E)
    ttk.Label(userinfo, textvariable=score).grid(column=1, row=2, sticky=E)
    ttk.Label(userinfo, textvariable=bet).grid(column=1, row=3, sticky=E)

    # Creates the buttons for the player actions
    playerActions = ttk.Frame(mainframe)
    playerActions.grid(column=0, row=1, sticky=(E, W), columnspan=2)
    hitButton = ttk.Button(playerActions, text="Hit", command=hit)
    standButton = ttk.Button(playerActions, text="Stand", command=stand)
    global doubleButton # has to be global to be able to deactivate it
    doubleButton = ttk.Button(playerActions, text="Double Down", command=double)
    hitButton.pack(side=LEFT, fill=BOTH, expand=True)
    standButton.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
    doubleButton.pack(side=LEFT, fill=BOTH, expand=True)
    # Add a string that stores the last button press
    global action
    action = ""


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    return root, casinoTable, uname, bal, score, bet

#r,_,_,_,_,_ = generateGUI()
#r.mainloop()

def addCard(canvas, playerNum, totalPlayers, card, cardNum = 0):
    
    color = {"♥": "H", "♦": "D", "♣": "C", "♠": "S"}
    global cards # has to be a global variable to not get garbage-collected (Damn you, Python!)

    if not card == "back":
        cardImage = Image.open('Cards/' + color[card[0]] + card[1:] + '.png')
    else:
        cardImage = Image.open('Cards/back.png')
    cardWidth, cardHeight = cardImage.size
    cardWidth, cardHeight = cardWidth//5, cardHeight//5
    cardSize = (cardWidth, cardHeight)

    # The position of the cards depends on the how-manieth player is playing and the total number of players. Player 0 is the croupier
    canvasWidth, canvasHeight = canvas.winfo_width(), canvas.winfo_height()
    placement = [[(canvasWidth//2 + cardNum*cardWidth//6, 10), (canvasWidth//2 + cardNum*cardWidth//6, canvasHeight-10)],
                 [(canvasWidth//2 + cardNum*cardWidth//6, 10), (10 + cardNum*cardWidth//6, canvasHeight-10),  (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight-10)],
                 [(canvasWidth//2 + cardNum*cardWidth//6, 10), (10 + cardNum*cardWidth//6, canvasHeight-10),  (canvasWidth//2 + cardNum*cardWidth//6, canvasHeight-10),  (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight-10)],
                 [(canvasWidth//2 + cardNum*cardWidth//6, 10), (10 + cardNum*cardWidth//6, canvasHeight//2),  (10 + cardNum*cardWidth//6, canvasHeight-10),              (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight-10),    (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight//2)],
                 [(canvasWidth//2 + cardNum*cardWidth//6, 10), (10 + cardNum*cardWidth//6, canvasHeight//2),  (10 + cardNum*cardWidth//6, canvasHeight-10),              (canvasWidth//2 + cardNum*cardWidth//6, canvasHeight-10),      (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight-10), (canvasWidth - cardNum*cardWidth//6 - 10, canvasHeight//2)]]
    anchors = [["n", "s"],
               ["n", "sw", "se"],
               ["n", "sw", "s",  "se"],
               ["n", "w",  "sw", "se", "e"],
               ["n", "w",  "sw", "s",  "se", "e"]]
    x, y = placement[totalPlayers - 1][playerNum]
    anch = anchors[totalPlayers - 1][playerNum]

    cards.append(ImageTk.PhotoImage(cardImage.resize(cardSize, Image.ANTIALIAS)))
    canvas.create_image(x, y, image=cards[-1], anchor=anch)

def resetTable():
    global cards
    cards = []


def setCannotDouble():
    doubleButton["state"] = "disabled"

def setCanDouble():
    doubleButton["state"] = "normal"


def recap(players, root):
    def dismiss ():
        dlg.grab_release()
        dlg.destroy()

    dlg = Toplevel(root)
    ttk.Label(dlg, font=25, text="Recap (only players who didn't go broke):").pack(side=TOP, pady=5)
    for name, player in players.items():
        ttk.Label(dlg, text=f"{name} won {player['wins']} game{'' if player['wins'] == 1 else 's'} out of {len(player['score'])} with a final balance of ${player['balance']:.2f}").pack(padx=10, pady=5)
    ttk.Button(dlg, text="OK", command=dismiss).pack(pady=5)
    dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
    dlg.transient(root)   # dialog window is related to main
    sleep(0.1)#dlg.wait_visibility() # can't grab until window appears, so we wait
    dlg.grab_set()        # ensure all input goes to our window
    dlg.wait_window()     # block until window is destroyed

def placeNames(players, canvas):
    # Positionning of names is similar to cards, except croupier has no name shown.
    nPlayers = len(players)
    canvasWidth, canvasHeight = canvas.winfo_width(), canvas.winfo_height()
    placement = [[(canvasWidth//2, canvasHeight-10-120)],
                 [(10, canvasHeight-10-120),  (canvasWidth - 10, canvasHeight-10-120)],
                 [(10, canvasHeight-10-120),  (canvasWidth//2, canvasHeight-10-120),  (canvasWidth - 10, canvasHeight-10-120)],
                 [(10, canvasHeight//2-70),  (10, canvasHeight-10-120),              (canvasWidth - 10, canvasHeight-10-120),    (canvasWidth - 10, canvasHeight//2-70)],
                 [(10, canvasHeight//2-70),  (10, canvasHeight-10-120),              (canvasWidth//2, canvasHeight-10-120),      (canvasWidth - 10, canvasHeight-10-120), (canvasWidth - 10, canvasHeight//2-70)]]
    anchors = [["s"],
               ["sw", "se"],
               ["sw", "s",  "se"],
               ["w",  "sw", "se", "e"],
               ["w",  "sw", "s",  "se", "e"]]
    
    for i, (name, player) in enumerate(players.items()):
        x, y = placement[nPlayers - 1][i]
        anch = anchors[nPlayers - 1][i]
        player["name"] = canvas.create_text(x, y, anchor=anch, text=name, fill="white", font=25)
