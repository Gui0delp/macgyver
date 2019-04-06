"""Contents the code for generate the level and refresh it
"""

import pygame

class GameLvl(object):
    """the class permited to generate the game lvl and refresh it
    """
    def __init__(self, name_file):

        self.lvl_file = name_file
        self.lvl_structure = []
        self.size_sprite = 40

    def generate_lvl(self):
        """Permit to generate the level with the level_1.txt
        """

        with open(self.lvl_file, "r") as file_read:
            file_read = file_read.read()

        line = []

        for element in file_read:

            if element != "\n":    #Try to know the end of the line
                line.append(element)
            else:    #If it the end of the line, add the line to the structure
                self.lvl_structure.append(line)
                line = []


    def refresh_lvl(self, screen):
        """Permit to refresh the level
        """
        path = pygame.image.load("resources/path.png").convert_alpha()    #P
        wall = pygame.image.load("resources/wall.png").convert_alpha()    #W
        start = pygame.image.load("resources/start.png").convert_alpha()    #S
        end = pygame.image.load("resources/end.png").convert_alpha()    #E
        guardian = pygame.image.load("resources/guardan.png").convert_alpha()    #G
        item = pygame.image.load("resources/object.png").convert_alpha()    #O

        num_line = 0

        for line in self.lvl_structure:
            #We read all the sprite in line
            num_column = 0
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
