"""
    CS 5001
    11/08/2023
    Homework 7 - TestSimpleFraction.py
    Garfield Maitland
"""

import unittest
from SimpleFraction import SimpleFraction


class TestSimpleFraction(unittest.TestCase):
    """
    Class: TestSimpleFraction
        Allows for the testing of the
        SimpleFraction program

    Parameters:
        none

    Returns:
        none

    Defense:
        none
    """
    def test_default_constructor(self):
        """
        function: test_default_constructor()
            Tests to ensure that the object is constructed

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction()
        self.assertEqual(fraction.get_numerator(), 1)
        self.assertEqual(fraction.get_denominator(), 1)

    def test_parameter_constructor(self):
        """
        function: test_parameter_constructor()
            Tests to ensure that the parameter is constructed

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction(2, 3)
        self.assertEqual(fraction.get_numerator(), 2)
        self.assertEqual(fraction.get_denominator(), 3)

    def test_invalid_parameters(self):
        """
        function: test_invalid_parameters()
            Tests to ensure that there is an invalid parameter

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        with self.assertRaises(ValueError):
            SimpleFraction(1.5, 2)
        with self.assertRaises(ValueError):
            SimpleFraction(1, 'a')
        with self.assertRaises(ValueError):
            SimpleFraction(1, 0)

    def test_reciprocal(self):
        """
        function: test_reciprocal()
            Tests to determine the reciprocal of a fraction

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction(3, 4)
        reciprocal = fraction.make_reciprocal()
        self.assertEqual(reciprocal.get_numerator(), 4)
        self.assertEqual(reciprocal.get_denominator(), 3)

    def test_multiply_with_fraction(self):
        """
        function: test_multiply_with_fraction()
            Tests to ensure that the program can multiply fractions

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(3, 4)
        result = fraction1.multiply(fraction2)
        self.assertEqual(result.get_numerator(), 3)
        self.assertEqual(result.get_denominator(), 8)

    def test_multiply_with_integer(self):
        """
        function: test_multiply_with_integer()
            Tests to multiply an integer

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction(1, 2)
        result = fraction.multiply(2)
        self.assertEqual(result.get_numerator(), 2)
        self.assertEqual(result.get_denominator(), 2)

    def test_divide_with_fraction(self):
        """
        function: test_divide_with_fraction()
            Tests to ensure that the program can divide

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(3, 4)
        result = fraction1.divide(fraction2)
        self.assertEqual(result.get_numerator(), 4)
        self.assertEqual(result.get_denominator(), 6)

    def test_divide_with_integer(self):
        """
        function: test_divide_with_integer()
            Tests to ensure the program can divide integers

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction(1, 2)
        result = fraction.divide(2)
        self.assertEqual(result.get_numerator(), 1)
        self.assertEqual(result.get_denominator(), 4)

    def test_str(self):
        """
        function: test_str()
            Tests to ensure that the program receives a string type

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction = SimpleFraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

    def test_equality(self):
        """
        function: test_equality()
            Tests to ensure that the value has equality

        Parameters:
            self

        Returns:
            none

        Defense:
            none
        """
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(2, 4)
        fraction3 = SimpleFraction(2, 3)
        self.assertTrue(fraction1 == fraction2)
        self.assertFalse(fraction1 == fraction3)


if __name__ == '__main__':
    unittest.main()
    print("Done")
