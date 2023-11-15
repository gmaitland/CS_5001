"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - circle.py
"""

PI = 3.1415

# Class names are in pascal case. Classes are singular, they are not plural


class Circle:
    def __init__(self, radius, x = 0, y = 0):

        self.radius = radius
        self.x = x
        self.y = y
        self.color = "blue"

        if radius <= 0:
            raise ValueError

    def get_area(self):
        return PI * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def __str__(self):
        return "Circle with radius " + str(self.radius)

    def __eq__(self, other):
        return (self.radius == other.radius) and (self.color == other.color)

