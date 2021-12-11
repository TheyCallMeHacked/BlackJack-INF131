from tkinter import *
from tkinter import ttk

def generateGUI():
    # Generates the main window
    root = Tk()
    root.title("[INF131] Black Jack")
    root.resizable(FALSE, FALSE)

    # Adds a frame for themed UI (tries to follow system theme, somewhat broken on Linux with the Xfce desktop environment)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)   # setup the frame to scale with the window horizontally
    root.rowconfigure(0, weight=1)      # setup the frame to scale with the window vertically

    # Creates the canvas for the Casino Table
    casinoTable = Canvas(mainframe, bg="green")
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
    hit = ttk.Button(playerActions, text="Hit")
    stand = ttk.Button(playerActions, text="Stand")
    double = ttk.Button(playerActions, text="Double Down")
    hit.pack(side=LEFT, fill=BOTH, expand=True)
    stand.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
    double.pack(side=LEFT, fill=BOTH, expand=True)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    return root, casinoTable, uname, bal, score, bet

#r,_,_,_,_,_ = generateGUI()
#r.mainloop()