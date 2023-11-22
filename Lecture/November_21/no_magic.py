"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - no_magic.py
"""

import random


def abbra():
    print("No tricks up my sleeves")


def kadabra():
    print("No magic hats")


def bunny():
    print("Voila! A bunny rabbit!")


def main():
    FUNCTIONS = [abbra, kadabra, bunny]

    a = FUNCTIONS[1]
    a()

    b = random.choice(FUNCTIONS)
    b()

    b = random.choice(FUNCTIONS)
    b()


if __name__ == "__main__":
    main()
