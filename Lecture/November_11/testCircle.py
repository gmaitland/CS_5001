"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - testCircle.py
"""

PI = 3.1415


class TestCircle(unittest.TestCase):

    # positive tests

    def test_init(self):
        c = Circle(2)
        self.assertEqual(c.get_radius(), 2, "Wrong Radius")

    def test_get_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.get_area(), PI * 4, "Incorrect Area")

    def test_get_X(self):
        c = Circle(2, 3, 3)
        self.assertEqual(c.get_X, 3)
