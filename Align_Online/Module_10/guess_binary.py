"""
    Garfield Maitland
    CS 5001
    11/26/2023
    Align Online Module 10 - guess_binary.py
"""


"""
    Is an implementation of the guessing game that is smarter because
    it no longer guesses a random number.
    Binary Search. We are splitting the list in half, each and every time.
    
    Binary search is the fastest general purpose run time algorithm there is.
    It is so simple, yet so powerful.
"""


class Guessing_game:
    ''' Class that represents a random guessing game. '''

    def __init__(self, num_range):
        # the lowest number in the range starts at 1
        self.lowest = 1
        # the highst number in the range
        self.highest = num_range

    def next_guess(self, dir):
        '''
        Method: next_guess -- guess the next number
        Parameter:
           self -- the current object
           dir -- the direction the next guess should be
        Returns the next guess to make
        '''
        if dir == "l":
            # update the upper bound since the guess was lower
            self.highest = self.prev_guess - 1
        elif dir == "h":
            # update the lower bound since the guess i was higher
            self.lowest = self.prev_guess + 1
        # pick the number in the middle of the range
        self.prev_guess = self.lowest + (self.highest - self.lowest) // 2
        return self.prev_guess
        print("done ")
        # It will never take more than 6 guesses


def main():
    print("Did work on the efficiency algorithm's functionality")
    # instantiates the guessing game class
    game = Guessing_game(100)
    # keep track of how many guesses have been made
    count = 10
    guessed = False
    dir = ""
    # instead of us responding, we will automate this and tell the computer
    mystery_num = int(input("Enter your secret number (I won't tell!)): "))
    while not guessed:
        # what is your next guess
        guess = game.next_guess(dir)
        count += 1
        # displays the computer's guess
        print("The computer guesses", guess, "; ", end="")
        # determine whether the guess is right and give it feedback
        if guess < mystery_num:
            dir = "h"
            print('told it "higher"')
        elif guess > mystery_num:
            dir = "l"
            print('told it "lower"')
        else:
            guessed = True
            print('told it "correct"')
    print("I needed", count, "guesses--I hope that's good!")


if __name__ == "__main__":
    main()

