"""This file contents the main code of the game, it execute this code first
"""

#! /usr/bin/env python3
# coding: utf-8

import pygame
import modules.level as lvl
import modules.character as mac

def main():
    """The function contents the main code of the game
    """
    game = True
    w_sprite = 40
    l_sprite = 40
    w_width = 15 * w_sprite
    w_length = 15 * l_sprite
    pygame.init() # pylint: disable=no-member
    pygame.display.set_caption("Macgyver maze")
    window = pygame.display.set_mode((w_width, w_length))

    dir_file = "level_1.txt"
    main_lvl = lvl.GameLvl(dir_file)
    main_lvl.generate_lvl()
    macgyver = mac.Player(main_lvl.game_level)

    while game:    #The main loop of the game

        main_lvl.refresh_lvl(window)
        macgyver.move(window, "")
        #Capture the event of the player for the direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_DOWN:    # pylint: disable=no-member
                    macgyver.move(window, "DOWN")
                elif event.key == pygame.K_UP:    # pylint: disable=no-member
                    macgyver.move(window, "UP")
                elif event.key == pygame.K_LEFT:    # pylint: disable=no-member
                    macgyver.move(window, "LEFT")
                elif  event.key == pygame.K_RIGHT:    # pylint: disable=no-member
                    macgyver.move(window, "RIGHT")
                elif event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    game = False

        pygame.display.flip()

    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
