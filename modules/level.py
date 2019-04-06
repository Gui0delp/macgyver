"""Contents the code for generate the level and refresh it
"""

import pygame

class GameLvl(object):
    """the class permited to generate the game lvl and refresh it
    """
    def __init__(self, name_file):

        self.lvl_file = name_file
        self.case_x = 0
        self.case_y = 0
        self.pixel_x = 0
        self.pixel_y = 0
        self.lvl_structure = []


    def generate_lvl(self):
        """Permit to generate the level with the level_1.txt
        """

        with open(self.lvl_file, "r") as file_read:
            file_read = file_read.read()

        line = []

        for element in file_read:

            if element != "\n":
                line.append(element)
            else:
                self.lvl_structure.append(line)
                line = []


    def refresh_lvl(self):
        """Permit to refresh the level
        """
