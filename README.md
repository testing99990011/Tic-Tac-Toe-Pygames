# Tic-Tac-Toe-Pygames

Classic Tic-Tac-Toe game using Pygame. 
Includes a menu screen which allows the user to select difficulty, symbol, and GUI options, a score screen to see past matches, and the game screen where the player can interact with the board. 

## How To Play ##
Run the 'main.py' file. Click the 'Start Game' button to start a match. The match will start with the given settings in the settings menu. By default, the player is given the symbol X or O. X's start first in the match although this can be changed in settings. The first person to have their symbol connect in a sequence of 3, such as 3 across, down, or diagonal, wins the game. 

## Screens In The Game ##
- __Start Screen:__ Start screen contains the home page where the user can select what action they want to do. Start game to start a tic-tac-toe game. Scores to access the last 7 scores. Settings to access the GUI options, difficulty options, and symbol options. Also allows for a data reset. 
- __Game Screen:__ Game screen is the actual screen where the game is played. This is where the player interacts with the board. The info section at the bottom of the screen shows the game time, player moves, game difficulty, and player symbol. 
- __Score Screen:__ Score screen shows the last 7 matches played by the user, with 1 being the most recent. Below the most recent matches is a a overview of most common difficulty, average winner, average time, and average moves. Clicking the 'Done' button at the bottom of the page sends the use back to the start menu.
- __Settings Screen:__ Settings screen shows the settings the user can change. Difficulty: Allows the user to change the AI difficulty. Player Symbols: X, O, and Random (Random: chooses between X and O for the user). Player starts: Option to make the player always start first in the match, regardless of symbol. Enable timer: Enables the game timer at the bottom of the game screen. Move counter: Enables the move counter at the bottom of the game screen. Enable saving: allows the user to save their matches played. Reset button: Resets the scores screen and corresponding data. 

## File Overview ##
__main.py__ is the main driver code for the game. When run, the driver code will check events and run the main loop. __background.py__ manages the backgrounds for the game. This includes the files __start_background.py__, __game_background.py__, __settings_background.py__, and __scores_background.py__. __box.py__ is used to create the individual boxes that are used in the game and instances of this class are stored in the board dictionary. __ai_logic.py__ is used to determine the move AI will make in __main.py__ and __data_handling.py__ is used to load and store data (used in __main.py__). Finally, __settings.py__ is used to store critical variables like screenwidth, moves, and fonts. 
