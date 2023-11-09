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
        fraction = SimpleFraction()
        self.assertEqual(fraction.get_numerator(), 1)
        self.assertEqual(fraction.get_denominator(), 1)

    def test_parameter_constructor(self):
        fraction = SimpleFraction(2, 3)
        self.assertEqual(fraction.get_numerator(), 2)
        self.assertEqual(fraction.get_denominator(), 3)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            SimpleFraction(1.5, 2)
        with self.assertRaises(ValueError):
            SimpleFraction(1, 'a')
        with self.assertRaises(ValueError):
            SimpleFraction(1, 0)

    def test_reciprocal(self):
        fraction = SimpleFraction(3, 4)
        reciprocal = fraction.make_reciprocal()
        self.assertEqual(reciprocal.get_numerator(), 4)
        self.assertEqual(reciprocal.get_denominator(), 3)

    def test_multiply_with_fraction(self):
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(3, 4)
        result = fraction1.multiply(fraction2)
        self.assertEqual(result.get_numerator(), 3)
        self.assertEqual(result.get_denominator(), 8)

    def test_multiply_with_integer(self):
        fraction = SimpleFraction(1, 2)
        result = fraction.multiply(2)
        self.assertEqual(result.get_numerator(), 2)
        self.assertEqual(result.get_denominator(), 2)

    def test_divide_with_fraction(self):
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(3, 4)
        result = fraction1.divide(fraction2)
        self.assertEqual(result.get_numerator(), 4)
        self.assertEqual(result.get_denominator(), 6)

    def test_divide_with_integer(self):
        fraction = SimpleFraction(1, 2)
        result = fraction.divide(2)
        self.assertEqual(result.get_numerator(), 1)
        self.assertEqual(result.get_denominator(), 4)

    def test_str(self):
        fraction = SimpleFraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

    def test_equality(self):
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(2, 4)
        fraction3 = SimpleFraction(2, 3)
        self.assertTrue(fraction1 == fraction2)
        self.assertFalse(fraction1 == fraction3)


if __name__ == '__main__':
    unittest.main()
