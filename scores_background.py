import pygame
import json

class ScoreScreen:
    """Score screen for game. Record the past 5 matches for the player"""

    def __init__(self, MainInstance):
        """Load instances and variables"""
        self.MainInstance = MainInstance
        self.settings = MainInstance.settings
        self.screen = MainInstance.screen

        # Load variables
        self.font = self.settings.font_normal_scores
        self.font_matches = self.settings.font_matches_scores
        self.font_title = self.settings.font_title_scores
        self.text_color_normal = self.settings.text_color_normal_scores
        self.text_color_red = self.settings.text_color_red_scores
        self.text_color_green = self.settings.text_color_green_scores

        self._create_background()

    def _create_background(self):
        # Load the button and create rects
        self.done_button = pygame.image.load('Drawings/done_button.PNG').convert()
        self.done_button.set_colorkey((255, 255, 255))
        self.done_button = pygame.transform.scale(self.done_button, \
         (self.settings.button_width, self.settings.button_height))
        self.done_button_rect = self.done_button.get_rect()
        self.done_button_rect.bottom = self.settings.screen_height - self.settings.button_height // 2
        self.done_button_rect.center = (self.settings.screen_width // 2, self.done_button_rect.center[1])

        # Load the highlighted button
        self.done_button_highlight = pygame.image.load('Drawings/done_button.PNG').convert()
        self.done_button_highlight.set_colorkey((255, 255, 255))
        self.done_button_highlight = pygame.transform.scale(self.done_button_highlight, \
         (round(self.settings.button_width * (1+self.settings.button_highlight_scale)), \
         round(self.settings.button_height * (1+self.settings.button_highlight_scale))))
        self.done_button_highlight_rect = self.done_button_highlight.get_rect()
        self.done_button_highlight_rect.center = self.done_button_rect.center

        # Load the averages for the bottom. Average Time
        self.average_time_text = self.font.render("Average Time:", True, self.text_color_normal)
        self.average_time_text_rect = self.average_time_text.get_rect()
        self.average_time_text_rect.bottom = self.done_button_highlight_rect.top - self.settings.text_gap_scores * 2
        self.average_time_text_rect.left = self.settings.text_gap_scores * 3

        # Load the averages for the bottom. Average Moves
        self.average_moves_text = self.font.render("Average Moves:", True, self.text_color_normal)
        self.average_moves_text_rect = self.average_moves_text.get_rect()
        self.average_moves_text_rect.bottom = self.done_button_highlight_rect.top - self.settings.text_gap_scores * 2
        self.average_moves_text_rect.left = self.average_time_text_rect.right + (5 * self.settings.text_gap_scores)

        # Load the most frequent difficulty (last 5).
        self.most_common_diff_text = self.font.render("Frequent Difficulty:", True, self.text_color_normal)
        self.most_common_diff_text_rect = self.most_common_diff_text.get_rect()
        self.most_common_diff_text_rect.bottom = self.average_time_text_rect.top - self.settings.text_gap_scores * 2
        self.most_common_diff_text_rect.right = self.average_time_text_rect.right

        # Load the average winner (last 5).
        self.most_common_winner_text = self.font.render('Average Winner:', True, self.text_color_normal)
        self.most_common_winner_text_rect = self.most_common_winner_text.get_rect()
        self.most_common_winner_text_rect.bottom = self.average_moves_text_rect.top - self.settings.text_gap_scores * 2
        self.most_common_winner_text_rect.right = self.average_moves_text_rect.right

        # For the line seperating matches from averages
        self.line_start_pos = (0, self.most_common_diff_text_rect.top - self.settings.text_gap_scores)
        self.line_end_pos = (self.settings.screen_width, self.most_common_diff_text_rect.top - self.settings.text_gap_scores)

        # For the title
        text = f"Past {self.settings.number_saves + 1} Matches"
        self.title_text = self.font_title.render(text, True, self.text_color_normal)
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.top = 0
        self.title_text_rect.center = (self.settings.screen_width//2, self.title_text_rect.center[1])

    def update_info(self):
        # Print the averages at the bottom of the screen

        # For the average time
        self.average_time_data = self.font.render(str(self.MainInstance.loaded_data['Avg_Time']) + 's', True, self.text_color_normal)
        self.average_time_data_rect = self.average_time_data.get_rect()
        self.average_time_data_rect.bottom = self.average_time_text_rect.bottom
        self.average_time_data_rect.left = self.average_time_text_rect.right + self.settings.text_gap_scores

        # For the average moves
        self.average_moves_data = self.font.render(str(self.MainInstance.loaded_data['Avg_Moves']), True, self.text_color_normal)
        self.average_moves_data_rect = self.average_moves_data.get_rect()
        self.average_moves_data_rect.bottom = self.average_moves_text_rect.bottom
        self.average_moves_data_rect.left = self.average_moves_text_rect.right + self.settings.text_gap_scores

        # For the most frequent difficulty
        self.most_common_diff_data = self.font.render(str(self.MainInstance.loaded_data['Avg_Diff']), True, self.text_color_normal)
        self.most_common_diff_data_rect = self.most_common_diff_data.get_rect()
        self.most_common_diff_data_rect.bottom = self.most_common_diff_text_rect.bottom
        self.most_common_diff_data_rect.left = self.most_common_diff_text_rect.right + self.settings.text_gap_scores

        # For the most frequent winner
        self.most_common_winner_data = self.font.render(str(self.MainInstance.loaded_data['Avg_Winner']), True, self.text_color_normal)
        self.most_common_winner_data_rect = self.most_common_winner_data.get_rect()
        self.most_common_winner_data_rect.bottom = self.most_common_winner_text_rect.bottom
        self.most_common_winner_data_rect.left = self.most_common_winner_text_rect.right + self.settings.text_gap_scores

        # Draw the 5 most recent matches
        for match in range(0, self.settings.number_saves + 1):
            if self.MainInstance.loaded_data[match]['Winner'] != None:
                # Load the number
                match_number_text = self.font_matches.render(str(match+1) + ')', True, self.text_color_normal)
                match_number_text_rect = match_number_text.get_rect()
                match_number_text_rect.x = self.settings.text_gap_scores
                match_number_text_rect.top = self.settings.text_gap_scores * 2 * (match + 1)

                # Load the winner data
                winner = self.MainInstance.loaded_data[match]['Winner']
                if winner == 'AI':
                    winner_text = self.font_matches.render(winner, True, self.text_color_red)
                elif winner == 'You':
                    winner_text = self.font_matches.render(winner, True, self.text_color_green)
                else:
                    winner_text = self.font_matches.render(winner, True, self.text_color_normal)

                # Load the winner text
                winner_text_rect = winner_text.get_rect()
                winner_text_rect.x = match_number_text_rect.right + self.settings.text_gap_scores
                winner_text_rect.bottom = match_number_text_rect.bottom

                # Load the difficulty
                difficulty = self.MainInstance.loaded_data[match]['Difficulty']
                difficulty_text = self.font_matches.render(difficulty, True, self.text_color_normal)
                difficulty_text_rect = difficulty_text.get_rect()
                difficulty_text_rect.x = winner_text_rect.right + self.settings.text_gap_scores
                difficulty_text_rect.bottom = winner_text_rect.bottom

                # Load the moves
                moves = self.MainInstance.loaded_data[match]['Moves']
                moves_text = self.font_matches.render(str(moves), True, self.text_color_normal)
                moves_text_rect = moves_text.get_rect()
                moves_text_rect.x = difficulty_text_rect.right + self.settings.text_gap_scores
                moves_text_rect.bottom = difficulty_text_rect.bottom

                # Load the time
                time = self.MainInstance.loaded_data[match]['Time']
                time_text = self.font_matches.render(str(time), True, self.text_color_normal)
                time_text_rect = time_text.get_rect()
                time_text_rect.x = moves_text_rect.right + self.settings.text_gap_scores
                time_text_rect.bottom = moves_text_rect.bottom

                # Load the date
                date = self.MainInstance.loaded_data[match]['Date']
                date_text = self.font_matches.render(date, True, self.text_color_normal)
                date_text_rect = date_text.get_rect()
                date_text_rect.x = time_text_rect.right + self.settings.text_gap_scores
                date_text_rect.bottom = time_text_rect.bottom

                # Draw all the values
                self.screen.blit(match_number_text, match_number_text_rect)
                self.screen.blit(winner_text, winner_text_rect)
                self.screen.blit(difficulty_text, difficulty_text_rect)
                self.screen.blit(moves_text, moves_text_rect)
                self.screen.blit(time_text, time_text_rect)
                self.screen.blit(date_text, date_text_rect)


    def draw_highlights(self):
        # Draw the buttons highlighted
        mouse = pygame.mouse.get_pos()
        if self.done_button_rect.collidepoint(mouse):
            self.screen.blit(self.done_button_highlight, self.done_button_highlight_rect)


    def draw_scores_screen(self):
        # Update the values
        self.update_info()

        # Draw the buttons to screen
        self.screen.blit(self.done_button, self.done_button_rect)

        # Draw the title
        self.screen.blit(self.title_text, self.title_text_rect)

        # Draw the averages text to the screen
        self.screen.blit(self.average_time_text, self.average_time_text_rect)
        self.screen.blit(self.average_moves_text, self.average_moves_text_rect)
        self.screen.blit(self.most_common_diff_text, self.most_common_diff_text_rect)
        self.screen.blit(self.most_common_winner_text, self.most_common_winner_text_rect)

        # Draw the actual averages data
        self.screen.blit(self.average_time_data, self.average_time_data_rect)
        self.screen.blit(self.average_moves_data, self.average_moves_data_rect)
        self.screen.blit(self.most_common_diff_data, self.most_common_diff_data_rect)
        self.screen.blit(self.most_common_winner_data, self.most_common_winner_data_rect)

        # Create the border seperating the matches from the average data
        pygame.draw.line(self.screen, self.text_color_normal, self.line_start_pos, self.line_end_pos, self.settings.line_thickness_scores)


        self.draw_highlights()
