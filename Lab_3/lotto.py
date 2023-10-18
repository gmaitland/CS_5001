"""
    CS 5001
    09/29/2023
    Lab 3
    Garfield Maitland
"""

import random

MAX_GUESS = 5


def main():
    number = random.randint(1, 100)
    player_name = str(input("Hi 😃😃! What is your name?"))
    print(f"Welcome {player_name}! Let's get started.")
    print("I am thinking of a number between 1 and 100.")
    print(f"You have a maximum of {MAX_GUESS} guesses. Here we go. 3, 2, 1, begin!")
    cond = False # Creating an abstract condition is good code design
    number_of_guesses = 0

    while number_of_guesses < MAX_GUESS and cond is False:
        player_guess = int(input("What number do you think it is?"))
        number_of_guesses += 1

        if player_guess == number:
            print(f"Good job you win!")
            cond = True

        elif number_of_guesses == MAX_GUESS and player_guess != number:
            print("Sorry, you ran out of guesses")
            print(f"The number was {number}")
            # print(f"Sorry, that is the wrong number. You have {number_of_guesses - MAX_GUESS} left.")

        else:
            print(f"You have {MAX_GUESS - number_of_guesses} left")
            if player_guess < number:
                print(f"Try a larger number.")

            else:
                player_guess > number
                print(f"Try a smaller number.")


if __name__ == "__main__":
    main()
