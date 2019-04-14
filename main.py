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
    quit_game = True
    w_sprite = 40
    l_sprite = 40
    w_width = 15 * w_sprite
    w_length = 15 * l_sprite
    game_statut = 2    #0 = Loose, 1 = Win, 2 = Nothing
    pygame.init() # pylint: disable=no-member
    pygame.display.set_caption("Macgyver maze")
    window = pygame.display.set_mode((w_width, w_length))

    dir_file = "level_1.txt"
    main_lvl = lvl.GameLvl(dir_file)
    main_lvl.generate_lvl()
    #Use the structure generate by the methode generate_lvl() from the class GameLvl()
    macgyver = mac.Player(main_lvl.game_level)
    #The main loop of the game
    while game:
        #Permit to know if the player win or... not
        if macgyver.lvl[macgyver.y_mac][macgyver.x_mac] == "G" and macgyver.u_obj == 3:
            macgyver.y_mac = 14
            macgyver.x_mac = 0
            main_lvl.game_level[13][0] = "S"
            game_statut = 1
            game = False
        elif macgyver.lvl[macgyver.y_mac][macgyver.x_mac] == "G" and macgyver.u_obj != 3:
            macgyver.y_mac = 14
            macgyver.x_mac = 2
            game_statut = 0
            game = False

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
        #Call the methode user_interface for manage the objects counter and more
        macgyver.user_interface(window, game_statut)
        pygame.display.flip()

    while quit_game:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    quit_game = False
                    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    #Call the main() function of the game
    main()
