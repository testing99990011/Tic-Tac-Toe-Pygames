import pygame
from box import Box

class GameBackground:
    """Background for the game itself"""

    def __init__(self, background_main, MainInstance):
        """Instances and variables used"""
        self.maininstance = MainInstance
        self.settings = MainInstance.settings
        self.screen = MainInstance.screen
        self.dictt = MainInstance.dictt
        self.background_parent = background_main

        # Fonts
        self.font = self.settings.font_normal_game
        self.text_color = self.settings.text_color_normal_game
        self.font_big = self.settings.font_big_game
        self.text_color_line = self.settings.text_color_line_game
        self.text_color_red = self.settings.text_color_red_game
        self.text_color_green = self.settings.text_color_green_game

        self._create_background_()

    def _create_background_(self):
        # Create text for if player wins
        self.player_wins_text = self.font_big.render("Player Wins", True, self.text_color_green)
        self.player_wins_text_rect = self.player_wins_text.get_rect()
        self.player_wins_text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height - self.settings.info_height//2)

        # Create text for if AI wins
        self.ai_wins_text = self.font_big.render("Computer Wins", True, self.text_color_red)
        self.ai_wins_text_rect = self.ai_wins_text.get_rect()
        self.ai_wins_text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height - self.settings.info_height//2)

        # Create the text if tie
        self.tie_wins_text = self.font_big.render('TIE', True, self.text_color)
        self.tie_wins_text_rect = self.tie_wins_text.get_rect()
        self.tie_wins_text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height - self.settings.info_height//2)

        # Fill the dict with the corresponding boxes
        for y in range(1,4):
            for x in range(1,4):
                y_cord = (y*self.settings.screen_gap+self.settings.box_height/2) +\
                         (self.settings.box_height*(y-1))
                x_cord = (x*self.settings.screen_gap+self.settings.box_width/2) +\
                         (self.settings.box_width*(x-1))
                temp_box = Box(self, x_cord, y_cord)
                self.dictt[int(str(y)+str(x))]['Decal'] = temp_box

        # Create the info at the bottom of screen. Time
        self.turn_timer_text = self.font.render('Time: ', True, self.text_color)
        self.turn_timer_text_rect = self.turn_timer_text.get_rect()
        self.turn_timer_text_rect.bottom = self.settings.screen_height - self.settings.text_gap_game * 2
        self.turn_timer_text_rect.left = self.settings.text_gap_game

        # Create the info at the bottom of screen. Moves
        self.current_move_text = self.font.render('Moves: ', True, self.text_color)
        self.current_move_text_rect = self.current_move_text.get_rect()
        self.current_move_text_rect.bottom = self.settings.screen_height - self.settings.text_gap_game * 2
        self.current_move_text_rect.right = self.settings.screen_width - self.settings.text_gap_game * 2

        # Create the info at the bottom of screen. Difficulty text
        self.difficulty_text = self.font.render("Game difficulty: ", True, self.text_color)
        self.difficulty_text_rect = self.difficulty_text.get_rect()
        self.difficulty_text_rect.center = (round(self.settings.screen_width/2) - self.settings.text_gap_game, self.turn_timer_text_rect.bottom - self.difficulty_text_rect.height - self.settings.text_gap_game)

        # Create the info at the bottom of screen. Player symbol
        self.you_are_text = self.font.render("You are: ", True, self.text_color)
        self.you_are_text_rect = self.you_are_text.get_rect()
        self.you_are_text_rect.center = (round(self.settings.screen_width/2), self.turn_timer_text_rect.bottom + self.you_are_text_rect.height)


    def _update_info_background(self):
        # Update the info background after every turn

        # Print ai difficulty (updates every time)
        self.difficulty_data = self.font.render(self.settings.game_difficulty, True, self.text_color)
        self.difficulty_data_rect = self.difficulty_data.get_rect()
        self.difficulty_data_rect.left = self.difficulty_text_rect.right + self.settings.text_gap_game//2
        self.difficulty_data_rect.bottom = self.difficulty_text_rect.bottom

        # Print player symbol (updates every time)
        self.you_are_data = self.font.render(\
         self.settings.player_symbols[self.maininstance.player_symbol], True, self.text_color)
        self.you_are_data_rect = self.you_are_data.get_rect()
        self.you_are_data_rect.bottom = self.you_are_text_rect.bottom
        self.you_are_data_rect.left = self.you_are_text_rect.right + self.settings.text_gap_game//2

        # Update the turns
        self.current_move_data = self.font.render(str(self.settings.moves), True, self.text_color)
        self.current_move_data_rect = self.current_move_data.get_rect()
        self.current_move_data_rect.bottom = self.current_move_text_rect.bottom
        self.current_move_data_rect.left = self.current_move_text_rect.right + self.settings.text_gap_game//2

        # Update the timer
        self.turn_timer_data = (pygame.time.get_ticks()-self.background_parent.start_ticks)/1000
        self.settings.game_timer = self.turn_timer_data
        self.turn_timer_data = self.font.render(str(self.turn_timer_data), True, self.text_color)
        self.turn_timer_data_rect = self.turn_timer_data.get_rect()
        self.turn_timer_data_rect.bottom = self.turn_timer_text_rect.bottom
        self.turn_timer_data_rect.left = self.turn_timer_text_rect.right + self.settings.text_gap_game//2

    def _draw_boxes(self):
        for y in range(1,4):
            for x in range(1,4):
                self.dictt[int(str(y)+str(x))]['Decal'].draw_box(self.dictt[int(str(y)+str(x))]['val'])

    def _draw_info(self):
        # Update the info
        self._update_info_background()

        # Draw Info at bottom of screen
        # Timer enabled/disabled in settings
        if self.settings.timer_option:
            self.screen.blit(self.turn_timer_text, self.turn_timer_text_rect)
            self.screen.blit(self.turn_timer_data, self.turn_timer_data_rect)

        # Moves enabled/disabled in settings
        if self.settings.move_option:
            self.screen.blit(self.current_move_text, self.current_move_text_rect)
            self.screen.blit(self.current_move_data, self.current_move_data_rect)

        self.screen.blit(self.you_are_text, self.you_are_text_rect)
        self.screen.blit(self.you_are_data, self.you_are_data_rect)
        self.screen.blit(self.difficulty_text, self.difficulty_text_rect)
        self.screen.blit(self.difficulty_data, self.difficulty_data_rect)

    def _draw_boxes(self):
        # Draw the actual boxes
        for y in range(1,4):
            for x in range(1,4):
                self.dictt[int(str(y)+str(x))]['Decal'].draw_box(self.dictt[int(str(y)+str(x))]['val'])

    def _winning_sections(self, board):
        # Flash the winning combination

        # Check if a tie
        new_lst = []
        for row in range(1, 4):
            for col in range(1, 4):
                new_lst.append(board[int(str(row) + str(col))]['val'])
        if None not in new_lst:
            winner = "Tie"

        # Check the rows
        for row in range(1, 4):
            if board[int(str(row) + "1")]['val'] == board[int(str(row) + "2")]['val'] == board[int(str(row) + "3")]['val'] and board[int(str(row) + "1")]['val'] != None:
                winner = board[int(str(row) + "1")]['val']
                pos_start = board[int(str(row) + "1")]['Decal'].box_rect.center
                pos_end = board[int(str(row) + "3")]['Decal'].box_rect.center

        # Check the columns
        for col in range(1, 4):
            if board[int("1" + str(col))]['val'] == board[int("2" + str(col))]['val'] == board[int("3" + str(col))]['val'] and board[int("1" + str(col))]['val'] != None:
                winner = board[int("1" + str(col))]['val']
                pos_start = board[int("1" + str(col))]['Decal'].box_rect.center
                pos_end = board[int("3" + str(col))]['Decal'].box_rect.center

        # Check the diagonals top left across
        if board[11]['val'] == board[22]['val'] == board[33]['val'] and board[11]['val'] != None:
            winner = board[11]['val']
            pos_start = board[11]['Decal'].box_rect.center
            pos_end = board[33]['Decal'].box_rect.center

        # Check the diagonals top right across
        if board[13]['val'] == board[22]['val'] == board[31]['val'] and board[13]['val'] != None:
            winner = board[13]['val']
            pos_start = board[13]['Decal'].box_rect.center
            pos_end = board[31]['Decal'].box_rect.center

        if self.maininstance.player_symbol == winner:
            self.settings.winner = "You"    # 'Player' is too long of string for screen
            pygame.draw.line(self.screen, self.text_color_line, pos_start, pos_end, self.settings.win_line_width)
            self.screen.blit(self.player_wins_text, self.player_wins_text_rect)
        elif self.maininstance.ai_symbol == winner:
            self.settings.winner = "AI"
            pygame.draw.line(self.screen, self.text_color_line, pos_start, pos_end, self.settings.win_line_width)
            self.screen.blit(self.ai_wins_text, self.ai_wins_text_rect)
        else:
            self.screen.blit(self.tie_wins_text, self.tie_wins_text_rect)
            self.settings.winner = "Tie"

    def _draw_winning_screen(self):
        # Draw all the boxes
        self._draw_boxes()

        # Draw the winning boxes (changes their color)
        self._winning_sections(self.settings.main_dictt)

    def draw_game_screen(self):
        # Draw the rectangular box
        pygame.draw.rect(self.screen, self.text_color, \
         pygame.Rect(0,\
         0,\
         self.settings.screen_width,\
         self.settings.screen_height-self.settings.info_height),\
         self.settings.box_thickness)

        # Draw the info boxes and actual game boxes
        self._draw_info()
        self._draw_boxes()
