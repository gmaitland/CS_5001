"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - Point.py
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)
