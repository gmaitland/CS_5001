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
        """
        Function: __init__()
            Constructs the class

        Parameters:
            self, numerator, denominator

        Returns:
            none

        Defense:
            none
        """

        self.validate(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def validate(numerator, denominator):
        """
        Function: validate()
            Validates the arguments passed into the parameter field

        Parameters:
            numerator, denominator

        Returns:
            none

        Defense:
            ValueError()
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator must be of integers")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

    def get_numerator(self):
        """
        Function: get_numerator()
            Gets the numerator

        Parameters:
            self

        Returns:
            self.numerator

        Defense:
            none
        """
        return self.numerator

    def get_denominator(self):
        """
        Function: get_denominator()
            Gets the denominator

        Parameters:
            self

        Returns:
            self.denominator

        Defense:
            none
        """
        return self.denominator

    def make_reciprocal(self):
        """
        Function: make_reciprocal()
            Places the denominator over the numerator

        Parameters:
            self

        Returns:
            SimpleFraction()

        Defense:
            none
        """
        self.validate(self.denominator, self.numerator)
        return SimpleFraction(self.denominator, self.numerator)

    def multiply(self, other):
        """
        Function: multiply()
            Multiplies another SimpleFraction or an integer

        Parameters:
            self, other

        Returns:
            SimpleFraction()

        Defense:
            ValueError()
        """
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
        """
        Function: divide()
            Divides another SimpleFraction or an integer

        Parameters:
            self, other

        Returns:
            SimpleFraction()

        Defense:
            ValueError()
        """
        if isinstance(other, SimpleFraction):
            return SimpleFraction(self.numerator *
                                  other.get_denominator(),
                                  self.denominator *
                                  other.get_numerator())
        elif isinstance(other, int):
            self.validate(other, 1)  # Ensure it's a valid integer
            return SimpleFraction(self.numerator, self.denominator * other)
        else:
            raise ValueError("Can only divide by another"
                             " SimpleFraction or an integer")

    def __str__(self):
        """
        Function: __str__()
            Returns a string representation of the class object; dunder


        Parameters:
            self

        Returns:
            String

        Defense:
            none
        """
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        Function: __eq__()
            Evaluates whether two objects are equal

        Parameters:
            self, other

        Returns:
            Boolean

        Defense:
            none
        """
        if isinstance(other, SimpleFraction):
            return (self.numerator * other.get_denominator() ==
                    self.denominator * other.get_numerator())
        return False
