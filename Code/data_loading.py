import pygame
import json

class Datahandling:
    """Handle game data"""

    def __init__(self, MainInstance):
        """Load the instances used"""
        self.MainInstance = MainInstance
        self.settings = MainInstance.settings

    def load_game_data(self, RESET=False):
        # Load previous game data. Returns a dictionary of data that can be manipulated
        file = open(self.settings.save_location, 'r')

        # Try to load previous game data
        try:
            self.data_dictt = json.load(file)
            # Covert the json key strings to ints
            self.fixed_dictt = {}
            for key, value in self.data_dictt.items():
                try:
                    self.fixed_dictt[int(key)] = value
                    # If the save has less than save amount, find what key to start saving at.
                    if self.data_dictt[key]['Winner'] != None:
                        self.settings.current_save = int(key) + 1
                except:
                    self.fixed_dictt[key] = value
            self.data_dictt = self.fixed_dictt
        # Except statement if this is completely new player
        except:
            self.data_dictt = self._create_new_data()
        file.close()

        # Check if player wants to reset all the stats
        if RESET:
            self.data_dictt = self._create_new_data()

        # Return the dictionary
        return self.data_dictt


    def _create_new_data(self):
        # Create a new empty dictionary
        dictt = {"Avg_Time": 0, "Avg_Moves": 0, "Avg_Diff": 0, "Avg_Winner": 0}
        for i in range(0, self.settings.number_saves+1):
            dictt[i] = {"Winner": None, "Difficulty": None, "Moves": 0, "Time": 0, "Date": None}
        return dictt


    def save_game_data(self):
        '''Save the game data.'''
        file = open(self.settings.save_location, 'w')
        json.dump(self.MainInstance.loaded_data, file)
        file.close()
        # Note: Json converts int keys to str. Converted back when loaded data.
