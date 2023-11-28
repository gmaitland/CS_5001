"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - mastermind_game.py
"""

# from Game import MasterMind
import turtle
from GUI import *


def main():
    Game = MasterMind()
    Game_UI = MasterMind_UI()
    Game_UI.start_game(Game)


if __name__ == '__main__':
    main()
