import pygame
import time
import datetime
import copy
from start_background import StartBackground
from game_background import GameBackground
from settings_background import SettingsBackground
from scores_background import ScoreScreen

class Background:
    """Main logic for running the background of game"""

    def __init__(self, MainInstance):
        # initialize the other backgrounds used in game
        self.maininstance = MainInstance
        self.settings = MainInstance.settings
        self.start_background = StartBackground(MainInstance)
        self.game_background = GameBackground(self, MainInstance)
        self.settings_background = SettingsBackground(MainInstance)
        self.scores_background = ScoreScreen(MainInstance)

    def _update_stats(self):
        # Move the dict values all over by 1
        # IF YOU DO self.shifted_dict[0] = ... YOU ARE ASSIGNING PHYSICAL KEY AT 0
        self.copy_dict = copy.deepcopy(self.maininstance.loaded_data)
        for key, value in self.maininstance.loaded_data.items():
            try:
                new_key = key + 1
                if new_key > self.settings.number_saves:
                    # Get rid of the last value and re-add the new value
                    pass
                else:
                    self.copy_dict[new_key] = value
            except:
                self.copy_dict[key] = value
        self.maininstance.loaded_data = self.copy_dict

        # Resume saving from most recent if not complete
        if self.settings.current_save+1 == self.settings.number_saves:
            save_id = self.settings.current_save
            self.settings.current_save += 1
        else:
            save_id = 0

        # Update the stats from match that just finished
        self.maininstance.loaded_data[save_id]["Winner"] = self.settings.winner
        self.maininstance.loaded_data[save_id]["Difficulty"] = self.settings.game_difficulty
        self.maininstance.loaded_data[save_id]["Moves"] = self.settings.moves
        self.maininstance.loaded_data[save_id]["Time"] = self.settings.game_timer
        self.maininstance.loaded_data[save_id]['Date'] = datetime.datetime.now().strftime('%m/%d/%Y')

        # Fil the lists with given values
        winner, diff, moves, times, data_points = [], [], [], [], 0
        for save in range(0, self.settings.number_saves + 1):
            if self.maininstance.loaded_data[save]['Winner'] != None:
                data_points += 1
            winner.append(self.maininstance.loaded_data[save]['Winner'])
            diff.append(self.maininstance.loaded_data[save]['Difficulty'])
            moves.append(self.maininstance.loaded_data[save]['Moves'])
            times.append(self.maininstance.loaded_data[save]['Time'])

        # Compute averages by finding number of repetitions
        iterations_winner = []
        iterations_diff = []
        for value in set(winner):
            if value != None:
                iterations_winner.append((winner.count(value), value))
        for value in set(diff):
            if value != None:
                iterations_diff.append((diff.count(value), value))

        # Update the actual averages
        self.maininstance.loaded_data["Avg_Winner"] = max(iterations_winner)[1]
        self.maininstance.loaded_data["Avg_Diff"] = max(iterations_diff)[1]
        self.maininstance.loaded_data["Avg_Moves"] = round(sum(moves) / data_points, 1)
        self.maininstance.loaded_data["Avg_Time"] = round(sum(times) / data_points, 1)


    def main_background_logic(self):
        # Run the main match_running code
        if self.maininstance.match_running:
            self.game_background.draw_game_screen()

        # Run the start screen if delay ends or match over
        elif self.maininstance.start_screen:

            # Run this if the game just ended
            if self.maininstance.match_end_delay:
                self.game_background._draw_winning_screen()
                pygame.display.flip()
                time.sleep(self.settings.match_delay)
                self.maininstance.match_end_delay = False

                # If save option enabled, save the scores
                if self.settings.save_game_option:
                    self._update_stats()
                self.maininstance._reset_game()
            self.start_background.draw_start_screen()

            # Create a start tick timer at the end of start screen since game starting
            self.start_ticks=pygame.time.get_ticks()

        elif self.maininstance.scores_screen:
            self.scores_background.draw_scores_screen()

        # Run the settings background
        elif self.maininstance.settings_screen:
            self.settings_background.draw_settings_screen()
