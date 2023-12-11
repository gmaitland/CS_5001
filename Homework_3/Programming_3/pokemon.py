"""
    Garfield Maitland
    CS 5001
    10/01/2023
    Homework 3 - pokemon.py
"""

import random


def get_player(number):
    """
    Function: get_player()
        Assigns a numerical value to the player that is associated
        to the numerical value to the pokemon selected.

    Parameters:
        number int: Is a value between 1 and 9 inclusive.
        Else all other numbers result in "Diglett" selection

    Preconditions:
        None

    Returns:
        Bulbasaur, or Charmander, or Butterfree, or Rattata, or Weedle,
         or Pikachu, or Sandslash, or Jigglypuff, or Raichu, Diglett
    """
    if number == 1:
        return "Bulbasaur"
    elif number == 2:
        return "Charmander"
    elif number == 3:
        return "Butterfree"
    elif number == 4:
        return "Rattata"
    elif number == 5:
        return "Weedle"
    elif number == 6:
        return "Pikachu"
    elif number == 7:
        return "Sandslash"
    elif number == 8:
        return "Jigglypuff"
    elif number == 9:
        return "Raichu"
    else:
        return "Diglett"


def check_battle(computer_choice, player_choice):
    """
    Function: check_battle()
        Creates the logic for the win condition to determine if either the
        computer choice or the player choice wins the battle.

    Parameters:
        computer_choice int: A value between 1 and 3 inclusive that represents
        rock, paper, or scissors.
        player_choice int: A value between 1 and 3 inclusive that represents
        rock, paper, or scissors.

    Preconditions:
        None

    Returns:
        DRAW! or COMPUTER or PLAYER
    """
    if computer_choice == player_choice:
        return "DRAW!"
    elif (computer_choice == 1 and player_choice == 3) or \
            (computer_choice == 2 and player_choice == 1) or \
            (computer_choice == 3 and player_choice == 2):
        return "COMPUTER"
    else:
        return "PLAYER"


def pokemon_game():
    """
    Function: pokemon_game()
        Creates 2 local variables to keep track of the running score.
        Additionally, ask's the player to select a team.
        Uses a while loop to get a random integer to select between our
        pokemon choices inclusive of 1 to 9.
        Then asks the user to input an integer that represents the choices
        of 'rock', 'paper', or 'scissors'.
        Determines the winner and adds plus 1 to either the red team
        or the blue team.
        When the player is done they can input any value except for 'y'
        to end the game and display the game's results.

    Parameters:
        None

    Preconditions:
        None

    Returns:
        DRAW! or COMPUTER or PLAYER
    """
    red_team_score = 0
    blue_team_score = 0

    print("Which team do you want (red or blue)?")
    chosen_team = input().lower()

    continue_playing = 'y'

    while continue_playing.lower() == 'y':
        red_pokemon = get_player(random.randint(1, 9))
        blue_pokemon = get_player(random.randint(1, 9))

        print(f"RED pokemon {red_pokemon} vs. BLUE pokemon {blue_pokemon}")
        print("Enter 1 for Rock, 2 for Paper, 3 for Scissors")
        player_choice = int(input())

        computer_choice = random.randint(1, 3)

        player_choice_text = "ROCK" if player_choice == 1 else \
            ("PAPER" if player_choice == 2 else "SCISSORS")
        computer_choice_text = "ROCK" if computer_choice == 1 else \
            ("PAPER" if computer_choice == 2 else "SCISSORS")

        print(f"{red_pokemon} played {player_choice_text}. "
              f"{blue_pokemon} played {computer_choice_text}")

        result = check_battle(computer_choice, player_choice)

        if result == "DRAW!":
            print("It's a draw! No winner")
        elif result == "COMPUTER":
            print(f"BLUE team wins with {blue_pokemon}!")
            blue_team_score += 1
        else:
            print(f"My RED team wins with {red_pokemon}!")
            red_team_score += 1

        print("Play again(y/n)?")
        continue_playing = input().lower()

    print("The tournament has ended!\n")
    print(f"RED team: {red_team_score}\nBLUE team: {blue_team_score}")

    if red_team_score > blue_team_score:
        print("I WIN!!!")
    elif blue_team_score > red_team_score:
        print("A COMPUTER WIN!!!")
    else:
        print("It's a draw! No winner")


def main():
    pokemon_game()


if __name__ == "__main__":
    main()
