"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - Game.py
"""

from random import randint


class MasterMind:
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.guess_length = 4
        self.guess_limit = 10
        self.guess_count = 0
        self.guesses = []
        self.game_state = "playing"
        # generate secret code
        self.secret_code = self.generate_code()

    def generate_code(self):
        color = self.colors.copy()
        secret_code = []
        for i in range(self.guess_length):
            secret_code.append(color.pop(randint(0, 5 - i)))
        return secret_code

    # Check if the guess is valid
    def validate_guess(self, guess: list):
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
        return self.game_state

    def get_secret_code(self):
        return self.secret_code
