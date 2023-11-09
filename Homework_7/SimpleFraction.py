"""
    CS 5001
    11/08/2023
    Homework 7 - SimpleFraction.py
    Garfield Maitland
"""


class SimpleFraction:
    """
    Class: SimpleFraction
        Allows for the manipulation of fractions

    Parameters:
        none

    Returns:
        none

    Defense:
        none
    """

    def __init__(self, numerator=1, denominator=1):
        self.validate(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def validate(numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator must be of integers")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def make_reciprocal(self):
        self.validate(self.denominator, self.numerator)
        return SimpleFraction(self.denominator, self.numerator)

    def multiply(self, other):
        if isinstance(other, SimpleFraction):
            return SimpleFraction(self.numerator *
                                  other.get_numerator(),
                                  self.denominator *
                                  other.get_denominator())
        elif isinstance(other, int):
            return SimpleFraction(self.numerator * other,
                                  self.denominator)
        else:
            raise ValueError("Can only multiply by another"
                             " SimpleFraction or an integer")

    def divide(self, other):
        if isinstance(other, SimpleFraction):
            return SimpleFraction(self.numerator *
                                  other.get_denominator(),
                                  self.denominator *
                                  other.get_numerator())
        elif isinstance(other, int):
            self.validate(other, 1)  # Ensure it's a valid integer
            return SimpleFraction(self.numerator, self.denominator * other)
        else:
            raise ValueError("Can only divide by another SimpleFraction or an integer")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if isinstance(other, SimpleFraction):
            return (self.numerator * other.get_denominator() ==
                    self.denominator * other.get_numerator())
        return False
