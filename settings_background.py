import pygame

class SettingsBackground:
    """Background for the settings window"""

    def __init__(self, MainInstance):
        """Create the instances and variables"""
        self.maininstance = MainInstance
        self.screen = MainInstance.screen
        self.settings = MainInstance.settings

        # Fonts
        self.font = self.settings.font_normal_settings
        self.text_color = self.settings.text_color_normal_settings
        self.text_color_green = self.settings.text_color_normal_highlight

        # Create the background
        self._create_background_()

    def _create_background_(self):
        # Load the button and create rects
        self.done_button = pygame.image.load('Drawings/done_button.PNG').convert()
        self.done_button.set_colorkey((255, 255, 255))
        self.done_button = pygame.transform.scale(self.done_button, \
         (self.settings.button_width, self.settings.button_height))
        self.done_button_rect = self.done_button.get_rect()
        self.done_button_rect.bottom = self.settings.screen_height - self.settings.button_height // 2
        self.done_button_rect.center = (self.settings.screen_width // 2, self.done_button_rect.center[1])

        # Load the highlighted done button
        self.done_button_highlight = pygame.image.load('Drawings/done_button.PNG').convert()
        self.done_button_highlight.set_colorkey((255, 255, 255))
        self.done_button_highlight = pygame.transform.scale(self.done_button_highlight, \
         (round(self.settings.button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.button_height * (1+self.settings.button_highlight_scale))))
        self.done_button_highlight_rect = self.done_button_highlight.get_rect()
        self.done_button_highlight_rect.center = self.done_button_rect.center

        # Load the reset button
        self.reset_button = pygame.image.load('Drawings/Reset_button.PNG').convert()
        self.reset_button.set_colorkey((255, 255, 255))
        self.reset_button = pygame.transform.scale(self.reset_button, (self.settings.reset_button_width, self.settings.reset_button_height))
        self.reset_button_rect = self.reset_button.get_rect()
        self.reset_button_rect.right = self.settings.screen_width - self.settings.text_gap_settings
        self.reset_button_rect.center = (self.reset_button_rect[0], self.done_button_rect.center[1])

        # Load the highlighted reset button
        self.reset_button_highlight = pygame.image.load('Drawings/Reset_button.PNG').convert()
        self.reset_button_highlight.set_colorkey((255, 255, 255))
        self.reset_button_highlight = pygame.transform.scale(self.reset_button_highlight, \
         (round(self.settings.reset_button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.reset_button_height * (1+self.settings.button_highlight_scale))))
        self.reset_button_highlight_rect = self.reset_button_highlight.get_rect()
        # Remember cant copy centers because tuple
        self.reset_button_highlight_rect.center = self.reset_button_rect.center

        # Load the check mark. Displays after reset is complete
        self.check_mark = pygame.image.load('Drawings/Check_mark.PNG').convert()
        self.check_mark.set_colorkey((255, 255, 255))
        self.check_mark = pygame.transform.scale(self.check_mark, (self.settings.check_mark_width_settings, self.settings.check_mark_height_settings))
        self.check_mark_rect = self.check_mark.get_rect()
        self.check_mark_rect.left = self.reset_button_rect.right + self.settings.text_gap_settings//2
        self.check_mark_rect.center = (self.check_mark_rect.center[0], self.reset_button_rect.center[1])

        '''On and Off Buttons Section'''
        # Load the on button
        self.reference_height = self.font.render("O", True, self.text_color)
        self.reference_height_rect = self.reference_height.get_rect().height
        self.circle_center = (self.reference_height_rect//2, self.reference_height_rect//2)
        self.circle_radius = self.reference_height_rect//2
        self.circle_width = self.settings.circle_thickness

        self.on_button = pygame.Surface((self.reference_height_rect, self.reference_height_rect), \
         pygame.SRCALPHA, 32)
        self.on_button = self.on_button.convert_alpha()
        pygame.draw.circle(self.on_button, self.text_color, \
         self.circle_center, self.circle_radius, self.circle_width)
        pygame.draw.circle(self.on_button, self.text_color_green, \
         self.circle_center, self.circle_radius - self.circle_width * 3)

        # Load the off button
        self.off_button = pygame.Surface((self.reference_height_rect, self.reference_height_rect), \
         pygame.SRCALPHA, 32)
        self.off_button = self.off_button.convert_alpha()
        pygame.draw.circle(self.off_button, self.text_color, \
         self.circle_center, self.circle_radius, self.circle_width)

        self.button_rect = self.on_button.get_rect()


        '''Difficulty Section'''
        # Load difficulty text
        self.difficulty_text = self.font.render("Difficulty Settings:", True, self.text_color)
        self.difficulty_text_rect = self.difficulty_text.get_rect()
        self.difficulty_text_rect.top = self.settings.text_gap_settings
        self.difficulty_text_rect.left = self.settings.text_gap_settings

        # Load the difficulty option easy
        self.easy_text = self.font.render("EASY", True, self.text_color)
        self.easy_text_rect = self.easy_text.get_rect()
        self.easy_text_rect.left = self.difficulty_text_rect.right + self.settings.text_gap_settings * 2
        self.easy_text_rect.bottom = self.difficulty_text_rect.bottom
        self.button_rect_easy = self.button_rect.copy()
        self.button_rect_easy.left = self.easy_text_rect.right + self.settings.text_gap_settings
        self.button_rect_easy.bottom = self.easy_text_rect.bottom

        # Load the difficulty option medium
        self.medium_text = self.font.render("MEDIUM", True, self.text_color)
        self.medium_text_rect = self.medium_text.get_rect()
        self.medium_text_rect.right = self.easy_text_rect.right
        self.medium_text_rect.top = self.easy_text_rect.bottom + self.settings.text_gap_settings
        self.button_rect_medium = self.button_rect.copy()
        self.button_rect_medium.left = self.medium_text_rect.right + self.settings.text_gap_settings
        self.button_rect_medium.bottom = self.medium_text_rect.bottom

        # Load the difficulty option hard
        self.hard_text = self.font.render("HARD", True, self.text_color)
        self.hard_text_rect = self.hard_text.get_rect()
        self.hard_text_rect.right = self.easy_text_rect.right
        self.hard_text_rect.top = self.medium_text_rect.bottom + self.settings.text_gap_settings
        self.button_rect_hard = self.button_rect.copy()
        self.button_rect_hard.left = self.hard_text_rect.right + self.settings.text_gap_settings
        self.button_rect_hard.bottom = self.hard_text_rect.bottom

        # Load the difficulty option random
        self.random_text = self.font.render("RANDOM", True, self.text_color)
        self.random_text_rect = self.random_text.get_rect()
        self.random_text_rect.right = self.easy_text_rect.right
        self.random_text_rect.top  = self.hard_text_rect.bottom + self.settings.text_gap_settings
        self.button_rect_random = self.button_rect.copy()
        self.button_rect_random.left = self.random_text_rect.right + self.settings.text_gap_settings
        self.button_rect_random.bottom = self.random_text_rect.bottom

        # Create dictionary for difficulty
        self.diff_dictt = {"Easy": self.button_rect_easy, \
         "Medium": self.button_rect_medium, \
         "Hard": self.button_rect_hard, "Random": self.button_rect_random}


        '''Symbol Section'''
        # Load the symbol text
        self.player_symbol_text = self.font.render("Player Symbol:", True, self.text_color)
        self.player_symbol_text_rect = self.player_symbol_text.get_rect()
        self.player_symbol_text_rect.right = self.difficulty_text_rect.right
        self.player_symbol_text_rect.top = self.button_rect_random.bottom + self.settings.text_gap_settings * 2

        # Load the symbol text symbols
        self.x_symbol_off = self.font.render("X", True, self.text_color)
        self.o_symbol_off = self.font.render("O", True, self.text_color)
        self.rand_symbol_off = self.font.render("RAND", True, self.text_color)
        self.x_symbol_on = self.font.render("X", True, self.text_color_green)
        self.o_symbol_on = self.font.render("O", True, self.text_color_green)
        self.rand_symbol_on = self.font.render("RAND", True, self.text_color_green)

        # Configure the X symbol
        self.x_symbol_rect = self.x_symbol_off.get_rect()
        self.x_symbol_rect.left = self.player_symbol_text_rect.right + self.settings.text_gap_settings * 2
        self.x_symbol_rect.bottom = self.player_symbol_text_rect.bottom

        # Configure the O symbol
        self.o_symbol_rect = self.o_symbol_off.get_rect()
        self.o_symbol_rect.left = self.x_symbol_rect.right + self.settings.text_gap_settings
        self.o_symbol_rect.bottom = self.x_symbol_rect.bottom

        # Configure the RAND symbol
        self.rand_symbol_rect = self.rand_symbol_off.get_rect()
        self.rand_symbol_rect.left = self.o_symbol_rect.right + self.settings.text_gap_settings
        self.rand_symbol_rect.bottom = self.o_symbol_rect.bottom

        # Create the dictionary for symbols
        self.symbol_select_dictt = \
         {"X": {"off": self.x_symbol_off, "on": self.x_symbol_on, "rect": self.x_symbol_rect}, \
         "O": {"off": self.o_symbol_off, "on": self.o_symbol_on, "rect": self.o_symbol_rect}, \
         "Random": {"off": self.rand_symbol_off, "on": self.rand_symbol_on, "rect": self.rand_symbol_rect}}


        '''Player Always Start Section'''
        # Load the player always start text
        self.player_always_start_option_text = self.font.render("Player Starts:", True, self.text_color)
        self.player_always_start_option_text_rect = self.player_always_start_option_text.get_rect()
        self.player_always_start_option_text_rect.right = self.difficulty_text_rect.right
        self.player_always_start_option_text_rect.top = self.rand_symbol_rect.bottom + self.settings.text_gap_settings * 2

        # Load the button
        self.player_always_start_option_button_rect = self.button_rect.copy()
        self.player_always_start_option_button_rect.x = self.player_always_start_option_text_rect.right + self.settings.text_gap_settings * 2
        self.player_always_start_option_button_rect.bottom = self.player_always_start_option_text_rect.bottom


        '''Timer Section'''
        # Load the timer text
        self.timer_text = self.font.render("Enable Timer:", True, self.text_color)
        self.timer_text_rect = self.timer_text.get_rect()
        self.timer_text_rect.right = self.difficulty_text_rect.right
        self.timer_text_rect.top = self.player_always_start_option_text_rect.bottom + self.settings.text_gap_settings * 2

        # Load the button
        self.timer_button_rect = self.button_rect.copy()
        self.timer_button_rect.x = self.timer_text_rect.right + self.settings.text_gap_settings * 2
        self.timer_button_rect.bottom = self.timer_text_rect.bottom


        '''Moves Section'''
        # Load the moves text
        self.moves_text = self.font.render("Move Counter:", True, self.text_color)
        self.moves_text_rect = self.moves_text.get_rect()
        self.moves_text_rect.right = self.difficulty_text_rect.right
        self.moves_text_rect.top = self.timer_text_rect.bottom + self.settings.text_gap_settings * 2

        # Load the button
        self.moves_button_rect = self.button_rect.copy()
        self.moves_button_rect.x = self.moves_text_rect.right + self.settings.text_gap_settings * 2
        self.moves_button_rect.bottom = self.moves_text_rect.bottom


        '''Saving Section'''
        # Load the saving text
        self.save_option_text = self.font.render("Enable Saving:", True, self.text_color)
        self.save_option_text_rect = self.save_option_text.get_rect()
        self.save_option_text_rect.right = self.difficulty_text_rect.right
        self.save_option_text_rect.top = self.moves_text_rect.bottom + self.settings.text_gap_settings * 2

        # Load the button
        self.save_option_button_rect = self.button_rect.copy()
        self.save_option_button_rect.x = self.save_option_text_rect.right + self.settings.text_gap_settings * 2
        self.save_option_button_rect.bottom = self.save_option_text_rect.bottom


    def _draw_text(self):

        '''Difficulty Section Draw'''
        # Draw the difficulty
        self.screen.blit(self.difficulty_text, self.difficulty_text_rect)
        self.screen.blit(self.easy_text, self.easy_text_rect)
        self.screen.blit(self.medium_text, self.medium_text_rect)
        self.screen.blit(self.hard_text, self.hard_text_rect)
        self.screen.blit(self.random_text, self.random_text_rect)

        # Draw the actual difficulty values
        for key in self.diff_dictt.keys():
            if key == self.settings.game_difficulty_face:
                self.screen.blit(self.on_button, self.diff_dictt[key])
            else:
                self.screen.blit(self.off_button, self.diff_dictt[key])


        '''Symbol Section Draw'''
        self.screen.blit(self.player_symbol_text, self.player_symbol_text_rect)
        for key in self.symbol_select_dictt.keys():
            if key == self.settings.player_symbol_actual:
                self.screen.blit(self.symbol_select_dictt[key]["on"], self.symbol_select_dictt[key]["rect"])
            else:
                self.screen.blit(self.symbol_select_dictt[key]["off"], self.symbol_select_dictt[key]["rect"])

        '''Player Always Start Section Draw'''
        self.screen.blit(self.player_always_start_option_text, self.player_always_start_option_text_rect)
        if self.settings.player_always_start_option:
            self.screen.blit(self.on_button, self.player_always_start_option_button_rect)
        else:
            self.screen.blit(self.off_button, self.player_always_start_option_button_rect)

        '''Timer Section Draw'''
        # Draw the timer option
        self.screen.blit(self.timer_text, self.timer_text_rect)
        if self.settings.timer_option:
            self.screen.blit(self.on_button, self.timer_button_rect)
        else:
            self.screen.blit(self.off_button, self.timer_button_rect)

        '''Move Counter Section Draw'''
        # Draw the move timer option
        self.screen.blit(self.moves_text, self.moves_text_rect)
        if self.settings.move_option:
            self.screen.blit(self.on_button, self.moves_button_rect)
        else:
            self.screen.blit(self.off_button, self.moves_button_rect)

        '''Save Game Section Draw'''
        # Draw the save option
        self.screen.blit(self.save_option_text, self.save_option_text_rect)
        if self.settings.save_game_option:
            self.screen.blit(self.on_button, self.save_option_button_rect)
        else:
            self.screen.blit(self.off_button, self.save_option_button_rect)

        '''Draw The Check Mark'''
        if self.settings.draw_check:
            self.screen.blit(self.check_mark, self.check_mark_rect)
            now_time = pygame.time.get_ticks()
            if now_time/1000 > self.maininstance.check_settings_ticks/1000 + self.settings.check_mark_time:
                self.settings.draw_check = False

    def draw_highlight(self):
        # Draw the highlight
        mouse = pygame.mouse.get_pos()
        if self.done_button_rect.collidepoint(mouse):
            self.screen.blit(self.done_button_highlight, self.done_button_highlight_rect)
        if self.reset_button_rect.collidepoint(mouse):
            self.screen.blit(self.reset_button_highlight, self.reset_button_highlight_rect)

    def draw_settings_screen(self):
        # Draw the settings screen
        self._draw_text()
        self.screen.blit(self.done_button, self.done_button_rect)
        self.screen.blit(self.reset_button, self.reset_button_rect)
        self.draw_highlight()

