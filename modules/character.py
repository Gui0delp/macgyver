"""Contain the code for manage the movement of Macgyver
"""

import pygame

class Player(object):
    """The class permite to manage the movement and collisions of the player
    """
    def __init__(self, lvl):
        self.x_mac = 14
        self.y_mac = 0
        self.lvl = lvl
        self.u_obj = 0

        self.calibri_font = pygame.font.SysFont("Calibri", 22)

    def move(self, screen, direction):
        """Permit to move the player
        direction type:  String
        screen type: Object
        """
        size_sprite = 40
        player = pygame.image.load("resources/MacGyver_2.png").convert_alpha()

        if direction == "DOWN":
            self.y_mac += 1
            if self.y_mac > 14:
                self.y_mac = 14
            if self.lvl[self.y_mac][self.x_mac] == "W":
                self.y_mac -= 1
        elif direction == "UP":
            self.y_mac -= 1
            if self.y_mac < 0:
                self.y_mac = 0
            if self.lvl[self.y_mac][self.x_mac] == "W":
                self.y_mac += 1
        elif direction == "LEFT":
            self.x_mac -= 1
            if self.x_mac < 0:
                self.x_mac = 0
            if self.lvl[self.y_mac][self.x_mac] == "W":
                self.x_mac += 1
        elif direction == "RIGHT":
            self.x_mac += 1
            if self.x_mac > 14:
                self.x_mac = 14
            if self.lvl[self.y_mac][self.x_mac] == "W":
                self.x_mac -= 1

        screen.blit(player, (self.x_mac * size_sprite, self.y_mac * size_sprite))

    def user_interface(self, screen, statut):
        """Permit to manage the user interface
        screen type: object
        statut type: integer
        """
        if self.lvl[self.y_mac][self.x_mac] == "O":
            self.lvl[self.y_mac][self.x_mac] = "P"
            self.u_obj += 1

        #user win
        if statut == 1:
            win_message = self.calibri_font.render("Great work you win!", True, (255, 255, 255))
            info_message = self.calibri_font.render("PRESS ESCAPE TO QUIT", True, (255, 255, 255))
            screen.blit(win_message, (40, 548))
            screen.blit(info_message, (220, 280))
        #user loose
        elif statut == 0:
            loose_message = self.calibri_font.render("You loose!", True, (255, 255, 255))
            info_message = self.calibri_font.render("PRESS ESCAPE TO QUIT", True, (255, 255, 255))
            screen.blit(loose_message, (40, 548))
            screen.blit(info_message, (220, 280))
        #nothing
        else:
            pass

        #Update of the object number
        counter_obj = self.calibri_font.render("Object : " + str(self.u_obj), True, (255, 255, 255))
        screen.blit(counter_obj, (0, 0))
