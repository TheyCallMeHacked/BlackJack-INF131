# Black Jack

## Dependencies
This game depends on `tkinter` and `pillow`. In order to run it, either double click _main.py_ from a file explorer (you might have to set it to run with Python), or run `./main.py` from a shell.

## Project Organization
### Overview
We started the project by following the given instructions up to the end of Part B. However, after starting Part C and the following, we made significant changes to the rules in order to better follow the standard Blackjack rules. To organize our code share and workflow, we used tools such as git and GitHub. The project has its own repository at the following url : [here](https://github.com/TheyCallMeHacked/BlackJack-INF131)
Moreover we made two versions of the game : a CLI one, which plays inside the shell and which can be started with the `--no-gui` command line argument, and one with a GUI made with `tkinter`.

### File organisation
The project code is divided in nine files, which contain each a given portion of how the game plays out.
1. deck.py handles the deck intialization and cards values (Part A1)
2. players.py handles the players, humans as well as bots, behaviour (Parts A2 and B)
3. croupier.py contains the specific functions for the croupier behaviour (Part C1 and C2)
4. game_management.py handles the round logic. (Part B2-B4 and C3-C4)
5. gui.py handles the gui logic and display. (Part D)
6. main.py handles the main game loop and displays end statistics for the players.
Additionally, there are three files that handle the CLI version : _croupier_no_gui.py_, game_management_nogui.py, and player_no_gui.py.

