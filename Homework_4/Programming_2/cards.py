"""
    Garfield Maitland
    CS 5001
    10/02/2023
    Homework 4 - cards.py
"""

import random


def create_deck():
    """
    Function: create_deck()
        Creates a new deck of cards within the range 2 to 10, and
        letters T, J, Q, K, A and within the suits c, d, h, and s.

    Parameters:
        None

    Preconditions:
        None

    Returns:
        List of cards (an array)
    """
    values = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']

    deck = [value + suit.lower() for suit in suits for value in values]

    return deck


def shuffle(cards):
    """
    Function: shuffle()
        Takes a list of cards, cards parameter, and shuffles it by utilizing
        the built-in random module

    Parameters:
        cards

    Preconditions:
        None

    Returns:
        List of cards that represent the shuffled deck
    """
    shuffled_deck = random.sample(cards, len(cards))
    return shuffled_deck


def deal(number_of_hands, number_of_cards, cards):
    """
    Function: deal()
        Creates a nested array that represents the number of players
        and the number of cards per players from the array of cards

    Parameters:
        number_of_hands, number_of_cards, and cards

    Preconditions:
        None

    Returns:
        List of hands representing the number of cards in hands
    """
    hands = [[] for _ in range(number_of_hands)]

    for _ in range(number_of_cards):
        for i in range(number_of_hands):
            if len(cards) > 0:
                card = cards.pop()
                hands[i].append(card)

    return hands
