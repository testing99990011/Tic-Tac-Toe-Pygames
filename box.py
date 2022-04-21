import pygame

class Box:
    """Individual box used in game background"""

    def __init__(self, MainInstance, x, y):
        """Instances and values for box"""
        self.maininstance = MainInstance
        self.settings = MainInstance.settings
        self.screen = MainInstance.screen

        # Values for creating the X's and O's
        self.font_normal = pygame.font.Font('freesansbold.ttf', 120)
        self.font_big = pygame.font.Font('freesansbold.ttf', 260)

        # Load the background for box and transfrom
        self.box = pygame.Surface((self.settings.box_width, self.settings.box_height))
        self.box.fill(self.settings.box_color)

        # Get the rect
        self.box_rect = self.box.get_rect()
        self.box_rect.center = (x, y)

        # Load highlighted box (Background)
        self.highlighted_box_width = round(self.settings.box_width + self.settings.scale_factor*self.settings.box_width)
        self.highlighted_box_height = self.highlighted_box_width
        self.highlighted_box = pygame.Surface((self.highlighted_box_width, self.highlighted_box_height))
        self.highlighted_box.fill(self.settings.box_color)

        # Set the highlighted box rects
        self.highlighted_box_rect = self.box_rect.copy()
        self.highlighted_box_rect.x -= round((self.settings.scale_factor*self.settings.box_width)/2)
        self.highlighted_box_rect.y -= round((self.settings.scale_factor*self.settings.box_width)/2)

        # Load the filled in boxes
        self.x_decal = self.font_normal.render('X', True, self.settings.symbol_color)
        self.o_decal = self.font_normal.render('O', True, self.settings.symbol_color)
        self.x_decal_highlight = self.font_big.render('X', True, self.settings.symbol_color)
        self.o_decal_highlight = self.font_big.render('O', True, self.settings.symbol_color)

        # Resize the normal filled in boxes
        self.symbol_normal_width = self.settings.box_width
        self.symbol_normal_height = self.symbol_normal_width
        self.x_decal_normal = pygame.transform.scale(self.x_decal,  (self.symbol_normal_width, self.symbol_normal_height))
        self.o_decal_normal = pygame.transform.scale(self.o_decal, (self.symbol_normal_width, self.symbol_normal_height))

        # Resize the highlight boxes
        self.symbol_highlight_width = round(self.settings.box_width + self.settings.box_width * self.settings.symbol_factor)
        self.symbol_highlight_height = self.symbol_highlight_width
        self.x_decal_highlight = pygame.transform.scale(self.x_decal_highlight, (self.symbol_highlight_width, self.symbol_highlight_height))
        self.o_decal_highlight = pygame.transform.scale(self.o_decal_highlight, (self.symbol_highlight_width, self.symbol_highlight_height))

        # Find the rects for highlighted and normal
        self.x_decal_normal_rect = self.box_rect.copy()
        self.o_decal_normal_rect = self.box_rect.copy()
        self.x_decal_highlight_rect = self.box_rect.copy()
        self.o_decal_highlight_rect = self.box_rect.copy()

        # Highlighted dict for box (used for highlighting)
        self.VALUE = None

    def _detect_mouse_highlight(self):
        # Highlight the box if mouse over it. Paste highlighted box over the main box
        mouse = pygame.mouse.get_pos()
        if self.box_rect.collidepoint(mouse):
            self.screen.blit(self.highlighted_box, self.highlighted_box_rect)
            if self.VALUE == 'X':
                self.screen.blit(self.x_decal_highlight, self.x_decal_highlight_rect)
            elif self.VALUE == 'O':
                self.screen.blit(self.o_decal_highlight, self.o_decal_highlight_rect)

    def draw_box(self, value=None):
        # Draw the individual box
        self.screen.blit(self.box, self.box_rect)
        if value == 0:
            self.screen.blit(self.x_decal_normal, self.x_decal_normal_rect)
        elif value == 1:
            self.screen.blit(self.o_decal_normal, self.o_decal_normal_rect)

        # Check if player turn and the box does not have a value
        if value == None and self.maininstance.maininstance.player_turn:
            self._detect_mouse_highlight()
            self.VALUE = None   # Reset value back to None

