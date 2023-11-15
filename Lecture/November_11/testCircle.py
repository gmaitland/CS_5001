"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - testCircle.py
"""
import unittest
from circle import Circle

PI = 3.1415


class TestCircle(unittest.TestCase):

    # positive tests

    def test_init(self):
        c = Circle(2)
        self.assertEqual(c.get_radius(), 2, "Wrong Radius")

    def test_get_area(self):
        c = Circle(2)
        self.assertAlmostEqual(PI * 4, c.get_area(), "Incorrect Area")

    def test_get_X(self):
        c = Circle(2, 3, 3)
        self.assertEqual(c.get_X(), 3)

    # negative test

    def test_bad_init(self):
        with self.assertRaises(ValueError):
            c = Circle(-2)
def main():
    unittest.main(verbosity=3)

main()