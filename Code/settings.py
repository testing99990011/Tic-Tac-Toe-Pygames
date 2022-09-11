import pygame

class Settings:
    """Settings for tic-tac-toe"""

    def __init__(self):
        """Basic setting values"""
        # Screen values for creating the pygame screen
        self.info_height = 100
        self.screen_width = 550 - self.info_height
        self.screen_height = 550
        self.screen_gap = 20

        # Values for buttons used in game
        self.button_width = 100
        self.button_height = 50
        self.button_gap = 20
        self.button_highlight_scale = 0.2
        self.reset_button_width = 50
        self.reset_button_height = 25

        # For the game_background
        self.text_gap_game = 20
        self.font_normal_game = pygame.font.Font('freesansbold.ttf', 16)
        self.text_color_normal_game = (0, 0, 0)
        self.font_big_game = pygame.font.Font('freesansbold.ttf', 40)
        self.text_color_line_game = (255, 51, 153)
        self.text_color_red_game = (255, 0, 0)
        self.text_color_green_game = (0, 255, 0)

        # For the settings background
        self.text_gap_settings = 20
        self.font_normal_settings = pygame.font.Font('freesansbold.ttf', 16)
        self.text_color_normal_settings = (0, 0, 0)
        self.text_color_normal_highlight = (0, 100, 0)
        self.circle_thickness = 1
        self.check_mark_width_settings = 25
        self.check_mark_height_settings = 25
        self.draw_check = False
        self.check_mark_time = 0.1 # In seconds

        # For the score background
        self.text_gap_scores = 20
        self.font_normal_scores = pygame.font.Font('freesansbold.ttf', 16)
        self.font_matches_scores = pygame.font.Font('freesansbold.ttf', 20)
        self.font_title_scores = pygame.font.Font('freesansbold.ttf', 24)
        self.font_title_scores.set_underline(True)
        self.text_color_normal_scores = (0, 0, 0)
        self.text_color_red_scores = (255, 0, 0)
        self.text_color_green_scores = (0, 255, 0)
        self.line_thickness_scores = 2

        # For the individual box and X's and O's scaling
        self.box_width = round((self.screen_width - self.screen_gap * 4) / 3)
        self.box_height = self.box_width
        self.box_color = (255, 255, 255)
        self.scale_factor = 0.1  # 10%
        self.symbol_factor = 0.05 # 5%
        self.symbol_color = (255,0,0)

        # For the info section of game screen and win line
        self.box_thickness = 16
        self.win_line_width = 4

        # For the settings screen
        self.circle_color_outline = (0, 0, 0)
        self.circle_color_fill = (0, 255, 0)
        self.circle_thickness = 1

        # For the dictionary. Val is 0 or 1 and Decal is object instance for corresponding position
        # Also player symbol dictionary
        self.main_dictt = {11: {'val': None, 'Decal': None},
             12: {'val': None, 'Decal': None},
             13: {'val': None, 'Decal': None},
             21: {'val': None, 'Decal': None},
             22: {'val': None, 'Decal': None},
             23: {'val': None, 'Decal': None},
             31: {'val': None, 'Decal': None},
             32: {'val': None, 'Decal': None},
             33: {'val': None, 'Decal': None}}
        self.player_symbols = {0: 'X', 1: 'O'}

        # Player flags and values for the game
        self.player_symbol_actual = "Random"    # Player_symbol defined in main() during reset game
        self.game_difficulty = 'Easy'           # Actual difficulty flag
        self.game_difficulty_face = 'Easy'      # Face value created because of random. Used in printing
        self.moves = 0
        self.game_timer = 0
        self.winner = None
        self.match_delay = 2

        # Actual player settings
        self.player_always_start_option = False
        self.timer_option = True
        self.move_option = True
        self.save_game_option = True

        # Flag used to completely game data. Note: Data is updated in display update section
        self.number_saves = 6   # 5 total saves (for value of 4) ; 7 saves total. Start at 0
        self.current_save =  0
        self.save_location = r'C:\Users\lkjh2\Desktop\Leson\Books\Python Crash Course Code\PART 2 PROJECTS\Project 1 PyGames\Try it Yourself\Tic-Tac-Toe version 3\Data\Game_Data.json'

