"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - factorial.py
"""


def factorial(n):
    if n == 0:
        return 1 # base case
    return n * factorial(n - 1)

