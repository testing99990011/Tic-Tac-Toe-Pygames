import pygame

class StartBackground:
    '''Start game background'''

    def __init__(self, MainInstance):
        """Create the instances and variables"""
        self.maininstance = MainInstance
        self.settings = MainInstance.settings
        self.screen = MainInstance.screen
        self.dictt = self.maininstance.dictt

        # Load the background
        self._create_background_()

    def _create_background_(self):

        # Load the start screen buttons
        self.start_button = pygame.image.load('Drawings/Start_button.PNG').convert()
        self.start_button.set_colorkey((255, 255, 255))
        self.settings_button = pygame.image.load('Drawings/Settings_button.PNG').convert()
        self.settings_button.set_colorkey((255, 255, 255))
        self.score_button = pygame.image.load('Drawings/Score_button.PNG').convert()
        self.score_button.set_colorkey((255, 255, 255))
        self.start_button = pygame.transform.scale(self.start_button, (self.settings.button_width, self.settings.button_height))
        self.settings_button = pygame.transform.scale(self.settings_button, (self.settings.button_width, self.settings.button_height))
        self.score_button = pygame.transform.scale(self.score_button, (self.settings.button_width, self.settings.button_height))

        # Set the rect's for all the buttons
        self.start_button_rect = self.start_button.get_rect()
        self.settings_button_rect = self.settings_button.get_rect()
        self.score_button_rect = self.score_button.get_rect()
        self.start_button_rect.center = \
        (round(self.settings.screen_width/2 - self.settings.button_width/2 - self.settings.button_gap), \
        round(self.settings.screen_height/2))
        self.settings_button_rect.center = \
        (round(self.settings.screen_width/2 + self.settings.button_width/2 + self.settings.button_gap), \
        round(self.settings.screen_height/2))
        self.score_button_rect.center = \
        (round(self.settings.screen_width/2), self.settings_button_rect.bottom + self.settings.button_height/2 + self.settings.button_gap)

        # Load and start screen buttons highlights and resize
        self.start_button_highlight = pygame.image.load('Drawings/Start_button.PNG').convert()
        self.start_button_highlight.set_colorkey((255, 255, 255))
        self.settings_button_highlight = pygame.image.load('Drawings/Settings_button.PNG').convert()
        self.settings_button_highlight.set_colorkey((255, 255, 255))
        self.score_button_highlight = pygame.image.load('Drawings/Score_button.PNG').convert()
        self.score_button_highlight.set_colorkey((255, 255, 255))
        self.start_button_highlight = pygame.transform.scale(self.start_button_highlight, \
         (round(self.settings.button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.button_height * (1+self.settings.button_highlight_scale))))
        self.settings_button_highlight = pygame.transform.scale(self.settings_button_highlight, \
         (round(self.settings.button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.button_height * (1+self.settings.button_highlight_scale))))
        self.score_button_highlight = pygame.transform.scale(self.score_button_highlight, \
         (round(self.settings.button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.button_height * (1+self.settings.button_highlight_scale))))

        # Set the rect's for the highlight buttons
        self.start_button_highlight_rect = self.start_button_highlight.get_rect()
        self.start_button_highlight_rect.center = self.start_button_rect.center
        self.settings_button_highlight_rect = self.settings_button_highlight.get_rect()
        self.settings_button_highlight_rect.center = self.settings_button_rect.center
        self.score_button_highlight_rect = self.score_button_highlight.get_rect()
        self.score_button_highlight_rect.center = self.score_button_rect.center

    def draw_start_screen(self):
        # Draw the buttons to screen
        self.screen.blit(self.start_button, self.start_button_rect)
        self.screen.blit(self.settings_button, self.settings_button_rect)
        self.screen.blit(self.score_button, self.score_button_rect)
        self.draw_highlights()

    def draw_highlights(self):
        # Draw the buttons highlighted
        mouse = pygame.mouse.get_pos()
        if self.start_button_rect.collidepoint(mouse):
            self.screen.blit(self.start_button_highlight, self.start_button_highlight_rect)
        elif self.settings_button_rect.collidepoint(mouse):
            self.screen.blit(self.settings_button_highlight, self.settings_button_highlight_rect)
        elif self.score_button_rect.collidepoint(mouse):
            self.screen.blit(self.score_button_highlight, self.score_button_highlight_rect)
