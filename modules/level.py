"""Contain the code for generate the level and refresh it
"""

import random
import pygame

class GameLvl(object):
    """the class permited to generate the game lvl and refresh it
    """
    def __init__(self, name_file):

        self.lvl_file = name_file
        self.game_level = []
        self.size_sprite = 40

    def generate_lvl(self):
        """Permit to generate the level with a text file
        """

        with open(self.lvl_file, "r") as file_read:
            file_read = file_read.read()

        line = []
        lvl_structure = []

        for element in file_read:

            if element != "\n":    #Try to know the end of the line
                line.append(element)
            else:    #If it the end of the line, add the line to the structure
                lvl_structure.append(line)
                line = []
            #Save the structure into the game_level
            self.game_level = lvl_structure


        i = 0

        while i != 3:

            test = True
            #Generate the 3 objects of the game with the random module
            while test:

                object_x = random.randint(0, 14)
                object_y = random.randint(0, 14)

                if self.game_level[object_y][object_x] == "P":
                    self.game_level[object_y][object_x] = "O"
                    object_x = 0
                    object_y = 0
                    test = False
            i += 1

        #Generate the guardian manually
        self.game_level[14][1] = "G"

    def refresh_lvl(self, screen):
        """Permit to refresh the level
        screen type: Object
        """
        path = pygame.image.load("resources/path.png").convert_alpha()    #P
        wall = pygame.image.load("resources/wall.png").convert_alpha()    #W
        start = pygame.image.load("resources/start.png").convert_alpha()    #S
        end = pygame.image.load("resources/end.png").convert_alpha()    #E
        guardian = pygame.image.load("resources/guardan.png").convert_alpha()    #G
        item = pygame.image.load("resources/object.png").convert_alpha()    #O

        num_line = 0

        for line in self.game_level:

            num_column = 0
            #We read all the sprite in line
            for sprite in line:

                x_grid = num_column * self.size_sprite
                y_grid = num_line * self.size_sprite
                #Show hte differents sprite in the level
                if sprite == "W":
                    screen.blit(wall, (x_grid, y_grid))
                elif sprite == "S":
                    screen.blit(start, (x_grid, y_grid))
                elif sprite == "E":
                    screen.blit(end, (x_grid, y_grid))
                elif sprite == "P":
                    screen.blit(path, (x_grid, y_grid))
                elif sprite == "G":
                    screen.blit(guardian, (x_grid, y_grid))
                elif sprite == "O":
                    screen.blit(item, (x_grid, y_grid))

                num_column += 1

            num_line += 1
