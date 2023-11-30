"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - Point.py
"""


class Point:
    """
    Class: Point
        Is the class that has the coordinates of the points x and y

    Parameters:
        None

    Returns:
        None

    Defense:
        None
    """
    def __init__(self, x, y):
        """
        Function: __init__()
            Is the constructor for the Class Point

        Parameters:
            self
            x
            y

        Returns:
            None

        Defense:
            None
        """
        self.x = x
        self.y = y

    def delta_x(self, other):
        """
        Function: delta_x()
            Records the change in the x-coordinate

        Parameters:
            self
            other

        Returns:
            None

        Defense:
            None
        """
        return abs(self.x - other.x)

    def delta_y(self, other):
        """
        Function: delta_y()
            Records the change in the y-coordinate

        Parameters:
            self
            other

        Returns:
            None

        Defense:
            None
        """
        return abs(self.y - other.y)
