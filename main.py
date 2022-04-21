import pygame
import sys
import random
from settings import Settings
from background import Background
from ai_logic import GameLogic
from data_loading import Datahandling


class TicTacToeMain:
    """Main class instance for the game."""

    def __init__(self):
        """Initialize the basic info"""

        # Start he pygames instance and create the settings instance
        pygame.init()
        self.settings = Settings()
        self.gamelogic = GameLogic()
        self.datahandling = Datahandling(self)
        self.loaded_data = self.datahandling.load_game_data()

        # Load the default values for screen
        self.screen_width, self.screen_height = self.settings.screen_width, self.settings.screen_height
        self.screen = pygame.display.set_mode(size=(self.screen_width, self.screen_height))
        self.fps = 30

        # Default values for data
        self.dictt = self.settings.main_dictt
        self._reset_game()

        # Load the background instance
        self.background = Background(self)

        # Flags for background
        self.start_screen = True
        self.match_running = False
        self.settings_screen = False
        self.scores_screen = False

        # Flags for the delay after match ends
        self.match_end_delay = False

    def main_loop(self):
        # Main loop that runs the entire time
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.fps)
            self._check_events()
            if self.match_running:
                self.main_ai_logic()
            self._update_display()

    def main_ai_logic(self):
        # Main logic section for AI turn
        if self.player_turn:
            mouse = pygame.mouse.get_pos()
            for col in range(1, 4):
                for row in range(1, 4):
                    if self.dictt[int(str(col) + str(row))]['Decal'].box_rect.collidepoint(mouse):
                        self.dictt[int(str(col) + str(row))]['Decal'].VALUE = self.settings.player_symbols[self.player_symbol]
        else:
            if self.settings.game_difficulty == 'Easy':
                self.dictt[self.gamelogic.AI_easy_turn(self.dictt)]['val'] = self.ai_symbol
            elif self.settings.game_difficulty == 'Medium':
                self.dictt[self.gamelogic.AI_medium_turn(self.dictt, self.ai_symbol)]['val'] = self.ai_symbol
            elif self.settings.game_difficulty == 'Hard':
                self.dictt[self.gamelogic.AI_hard_turn(self.dictt, self.ai_symbol, self.player_symbol)]['val'] = self.ai_symbol
            if self.gamelogic.check_game_over(self.dictt) == self.ai_symbol:
                self.match_running = False
                self.start_screen = True
                self.match_end_delay = True
            elif self.gamelogic.check_game_over(self.dictt) == 'Tie':
                self.match_running = False
                self.start_screen = True
                self.match_end_delay = True
            self.player_turn = True

    def _check_events(self):
        # Check for events such as button clicks
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():

            # Check if game ends
            if event.type == pygame.QUIT:
                self.datahandling.save_game_data()
                pygame.quit()
                sys.exit()
            # Check if there is a mouseclick

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Run if click is on start screen
                if self.start_screen:
                    # Check if player is starting the game
                    if self.background.start_background.start_button_rect.collidepoint(mouse):
                        self.start_screen = False
                        self.match_running = True
                    # Check if player is trying to get to settings screen
                    elif self.background.start_background.settings_button_rect.collidepoint(mouse):
                        self.start_screen = False
                        self.settings_screen = True
                    # Check if player is trying to get to score screen
                    elif self.background.start_background.score_button_rect.collidepoint(mouse):
                        self.start_screen = False
                        self.scores_screen = True
                # Check if click is on settings screen
                elif self.settings_screen:
                    # Check if player is leaving the settings screen
                    if self.background.settings_background.done_button_rect.collidepoint(mouse):
                        self.settings_screen = False
                        self.start_screen = True
                    # Check if player is changing game difficulty. If player selects Easy
                    if self.background.settings_background.button_rect_easy.collidepoint(mouse) and self.settings.game_difficulty_face != "Easy":
                        self.settings.game_difficulty = 'Easy'
                        self.settings.game_difficulty_face = 'Easy'
                    # Check if player is changing game difficulty. If player selects Medium
                    elif self.background.settings_background.button_rect_medium.collidepoint(mouse) and self.settings.game_difficulty_face != "Medium":
                        self.settings.game_difficulty = 'Medium'
                        self.settings.game_difficulty_face = 'Medium'
                    # Check if player is changing game difficulty. If player selects Hard
                    elif self.background.settings_background.button_rect_hard.collidepoint(mouse) and self.settings.game_difficulty_face != "Hard":
                        self.settings.game_difficulty = 'Hard'
                        self.settings.game_difficulty_face = 'Hard'
                    # Check if player is changing game difficulty. If player selects Random
                    elif self.background.settings_background.button_rect_random.collidepoint(mouse) and self.settings.game_difficulty_face != "Random":
                        self.settings.game_difficulty_face = 'Random'
                    # Check if the player is changing the player symbol. X
                    if self.background.settings_background.x_symbol_rect.collidepoint(mouse) and self.settings.player_symbol_actual != "X":
                        self.settings.player_symbol_actual = 'X'
                    # Check if the player is changing player symbol. O
                    elif self.background.settings_background.o_symbol_rect.collidepoint(mouse) and self.settings.player_symbol_actual != "O":
                        self.settings.player_symbol_actual = 'O'
                    # Check if the player is changing player symbol. Random
                    elif self.background.settings_background.rand_symbol_rect.collidepoint(mouse) and self.settings.player_symbol_actual != "Random":
                        self.settings.player_symbol_actual = 'Random'
                    # Check if player enabled always start option
                    if self.background.settings_background.player_always_start_option_button_rect.collidepoint(mouse):
                        if not self.settings.player_always_start_option:
                            self.settings.player_always_start_option = True
                        elif self.settings.player_always_start_option:
                            self.settings.player_always_start_option = False
                    # Check if the player enabled timer option
                    if self.background.settings_background.timer_button_rect.collidepoint(mouse):
                        if not self.settings.timer_option:
                            self.settings.timer_option = True
                        elif self.settings.timer_option:
                            self.settings.timer_option = False
                    # Check if the player enabled move option
                    if self.background.settings_background.moves_button_rect.collidepoint(mouse):
                        if not self.settings.move_option:
                            self.settings.move_option = True
                        elif self.settings.move_option:
                            self.settings.move_option = False
                    # Check if player enabled data saving
                    if self.background.settings_background.save_option_button_rect.collidepoint(mouse):
                        if not self.settings.save_game_option:
                            self.settings.save_game_option = True
                        elif self.settings.save_game_option:
                            self.settings.save_game_option = False
                    # Check if the player resets the game stats
                    if self.background.settings_background.reset_button_rect.collidepoint(mouse):
                        self.loaded_data = self.datahandling.load_game_data(True)
                        self.settings.draw_check = True
                        self.check_settings_ticks=pygame.time.get_ticks()
                    # Reset game so changes can be applied to symbol and to game difficulty
                    self._reset_game()

                elif self.scores_screen:
                    # Check if the player is leaving the score screen
                    if self.background.scores_background.done_button_rect.collidepoint(mouse):
                        self.scores_screen = False
                        self.start_screen = True

                # Check if the click is a game click (Match is running, player turn)
                elif self.match_running and self.player_turn:
                    self.settings.moves += 1
                    for col in range(1, 4):
                            for row in range(1, 4):
                                if self.dictt[int(str(col) + str(row))]['Decal'].box_rect.collidepoint(mouse) and self.dictt[int(str(col) + str(row))]['val'] == None:
                                    self.dictt[int(str(col) + str(row))]['val'] = self.player_symbol
                                    if self.gamelogic.check_game_over(self.dictt) == self.player_symbol:
                                        self.match_running = False
                                        self.start_screen = True
                                        self.match_end_delay = True
                                    elif self.gamelogic.check_game_over(self.dictt) == "Tie":
                                        self.match_running = False
                                        self.start_screen = True
                                        self.match_end_delay = True
                                    self.player_turn = False

    def _update_display(self):
        # Update the main screen
        self.screen.fill((40, 159, 250))
        self.background.main_background_logic()
        pygame.display.flip()

    def _reset_game(self):
        # Reset the board
        for row in range(1, 4):
            for col in range(1, 4):
                self.dictt[int(str(row) + str(col))]['val'] = None

        # Reset the info screen
        self.settings.game_timer = 0
        self.settings.moves = 0
        self.settings.winner = None

        # Find out who plays
        if self.settings.player_symbol_actual == 'Random':
            self.random_integer = random.randint(0, 1)
            if self.random_integer == 0:
                self.player_symbol = 0
                self.ai_symbol = 1
                self.player_turn = True
            else:
                self.player_symbol = 1
                self.ai_symbol = 0
                self.player_turn = False
        elif self.settings.player_symbol_actual == 'X':
            self.player_symbol = 0
            self.ai_symbol = 1
            self.player_turn = True
        elif self.settings.player_symbol_actual == 'O':
            self.player_symbol = 1
            self.ai_symbol = 0
            self.player_turn = False
        if self.settings.player_always_start_option:
            self.player_turn = True

        # Find a new difficulty if the face_value of difficulty is random
        if self.settings.game_difficulty_face == 'Random':
            choice = random.choice(['Easy', 'Medium', 'Hard'])
            self.settings.game_difficulty = choice



if __name__ == "__main__":
    main_instance = TicTacToeMain()
    main_instance.main_loop()





