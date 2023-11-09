"""
    CS 5001
    11/09/2023
    Lab 7 - lab_7 notes.py
    Garfield Maitland
"""


def is_even(number):
    # Base cases
    # Even
    print("Number is: ", number)
    if number == 0:
        print("It's Even!")
        return True
    # Odd
    if number == 1:
        print("It's Odd!")
        return False

    return is_even(number - 2)


def main():
    a = 10
    is_even(10)


if __name__ == "__main__":


"""
    Special Methods
    __str__(self)
    __eq__(self, other)
    __init__(self)
"""