"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - Game.py
"""

from random import randint


class MasterMind:
    """
        class: MasterMind
            Is the main class that holds the constructor and the
            essential functions for the game MasterMind.

        Parameters:
            None

        Returns:
            None

        Defense:
            None
    """
    def __init__(self):
        """
            Function: __init__()
                Constructor for the

            Parameters:
                song (type: str)
                old_word (type: str)

            Returns:
                bool

            Defense:
                None
        """
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.guess_length = 4
        self.guess_limit = 10
        self.guess_count = 0
        self.guesses = []
        self.game_state = "playing"
        # generate secret code
        self.secret_code = self.generate_code()

    def generate_code(self):
        """
            Function: generate_code()
                Creates the secret code for the game

            Parameters:
                self (type: int)

            Returns:
                array

            Defense:
                None
        """
        color = self.colors.copy()
        secret_code = []
        for i in range(self.guess_length):
            secret_code.append(color.pop(randint(0, 5 - i)))
        return secret_code

    # Check if the guess is valid
    def validate_guess(self, guess: list):
        """
            Function: validate()
                Checks the value of the secret code

            Parameters:
                self (type: str)
                guess (type: str)

            Returns:
                bool

            Defense:
                None
        """
        # check guess length
        if len(guess) != self.guess_length:
            raise ValueError("Guess must be of length " + str(self.guess_length))
        # check color duplicates
        if len(guess) != len(set(guess)):
            raise ValueError("Guess must not contain duplicates")
        # check if guess colors are in the colors list
        for i in guess:
            if i not in self.colors:
                raise ValueError("Guess must be one of the following colors: " + str(self.colors))
        return True

    def feedback(self, guess):
        """
            Function: feedback()
                Replaces the old word with the new word in the song.

            Parameters:
                self (type: str)
                guess (type: str)

            Returns:
                bool

            Defense:
                None
            """
        cows = 0
        bulls = 0
        for i in range(self.guess_length):
            if guess[i] == self.secret_code[i]:
                bulls += 1
        for i in range(self.guess_length):
            if guess[i] in self.secret_code:
                cows += 1
        cows -= bulls
        return {"Bulls": bulls, "Cows": cows}

    def add_guess(self, guess):
        """
            Function: add_guess()
                Appends the value of the guess to the array

            Parameters:
                self (type: str)
                guess (type: str)

            Returns:
                score (type: str)

            Defense:
                None
            """
        self.validate_guess(guess)
        if self.game_state == "playing":
            score = self.feedback(guess)
            self.guesses.append(self.feedback(guess))
            self.guess_count += 1
            if guess == self.secret_code:
                self.game_state = "won"
            elif self.guess_count == self.guess_limit:
                self.game_state = "lost"

            return score

    def get_game_state(self):
        """
            Function: get_game_state()
                Returns teh current state of the game

            Parameters:
                self (type: str)

            Returns:
                self.game_state (type: str)

            Defense:
                None
            """
        return self.game_state

    def get_secret_code(self):
        return self.secret_code
