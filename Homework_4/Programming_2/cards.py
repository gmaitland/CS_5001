"""
    Garfield Maitland
    CS 5001
    10/02/2023
    Homework 4 - cards.py
"""

import random


def create_deck():
    """
    Function:
        Takes a list of run-length encoding (RLE) values and returns a list
        containing the decoded values with the "runs" expanded.

    Parameters:
        list_of_integers, which is a possible UPC number

    Preconditions:
        None # Data

    Returns:
        Boolean, indicating whether the given input is valid or not
    """
    values = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']

    deck = [value + suit.lower() for suit in suits for value in values]

    return deck


def shuffle(cards):
    """
    Function:
        Takes a list of run-length encoding (RLE) values and returns a list
        containing the decoded values with the "runs" expanded.

    Parameters:
        list_of_integers, which is a possible UPC number

    Preconditions:
        None # Data

    Returns:
        Boolean, indicating whether the given input is valid or not
    """
    shuffled_deck = random.sample(cards, len(cards))
    return shuffled_deck


def deal(number_of_hands, number_of_cards, cards):
    """
    Function:
        Takes a list of run-length encoding (RLE) values and returns a list
        containing the decoded values with the "runs" expanded.

    Parameters:
        list_of_integers, which is a possible UPC number

    Preconditions:
        None # Data

    Returns:
        Boolean, indicating whether the given input is valid or not
    """
    hands = [[] for _ in range(number_of_hands)]

    for _ in range(number_of_cards):
        for i in range(number_of_hands):
            if len(cards) > 0:
                card = cards.pop()
                hands[i].append(card)

    return hands
