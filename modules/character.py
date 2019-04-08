"""Contain the code for manage the movement of Macgyver
"""

import pygame

class Player(object):
    """The class permite to manage the movement and collisions of the player
    """
    def __init__(self):
        self.x_mac = 14
        self.y_mac = 0

    def move(self, screen, direction):
        """Permit to move the player
        """
        size_sprite = 40
        player = pygame.image.load("resources/MacGyver_2.png").convert_alpha()

        if direction == "DOWN":
            self.y_mac += 1
        elif direction == "UP":
            self.y_mac -= 1
        elif direction == "LEFT":
            self.x_mac -= 1
        elif direction == "RIGHT":
            self.x_mac += 1
        else:
            pass

        screen.blit(player, (self.x_mac * size_sprite, self.y_mac * size_sprite))
