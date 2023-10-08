"""
    Garfield Maitland
    CS 5001
    10/02/2023
    Homework 4 - cards_driver.py
"""

import cards

deck = cards.create_deck()
shuffled_deck = cards.shuffle(deck)
hands = cards.deal(4, 5, shuffled_deck)



print("Shuffled Deck:", shuffled_deck)
for i, hand in enumerate(hands):
    print(f"Hand {i + 1}:", hand)