"""This file contents the main code of the game, it execute this code first
"""

#! /usr/bin/env python3
# coding: utf-8

import modules.level as lvl
import modules.character as mac

def main():
    """The function contents the main code of the game
    """

    dir_file = "level_1.txt"

    main_lvl = lvl.GameLvl(dir_file)
    main_lvl.generate_lvl()
    main_lvl.refresh_lvl()

if __name__ == "__main__":
    main()
