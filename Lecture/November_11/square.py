"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - square.py
"""


class Square:
    def __init__(self, length):
        self.length = length
        if length <= 0:
            raise ValueError

    def get_area(self):
        return self.length ** 2

    def __str__(self):
        return f"Square with length {self.length}"

    def __eq__(self, other):
        return self.lenth == other.length
