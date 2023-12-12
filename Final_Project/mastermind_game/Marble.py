"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - Marble.py
"""

import turtle
from Point import Point

MARBLE_RADIUS = 15


class Point:
    """
    Class: Point
        Is the class that has the coordinates of the Marble

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
            Is the constructor for the class Point

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
            Maps the x-coordinate of the Marble

        Parameters:
            self
            other

        Returns:
            abs()

        Defense:
            None
        """
        return abs(self.x - other.x)

    def delta_y(self, other):
        """
        Function: substitute()
            Maps the y-coordinate of the Marble

        Parameters:
            self
            other

        Returns:
            abs()

        Defense:
            None
        """
        return abs(self.y - other.y)


class Marble:
    def __init__(self, position, color, size=MARBLE_RADIUS):
        """
        Function: __init__()
            Is the constructor of the Marble Class

        Parameters:
            self
            position
            color
            size

        Returns:
            None

        Defense:
            None
        """
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self):
        """
        Function: new_pen()
            Creates a new_pen instance

        Parameters:
            self

        Returns:
            turtle.Turtle()

        Defense:
            None
        """
        return turtle.Turtle()

    def set_color(self, color):
        """
        Function: set_color()
            The function that sets the color of the object

        Parameters:
            self

        Returns:
            color

        Defense:
            None
        """
        self.color = color
        self.is_empty = False

    def get_color(self):
        """
        Function: get_color()
            A function that gets the color of the Marble object

        Parameters:
            None

        Returns:
            self.color

        Defense:
            None
        """
        return self.color

    def draw(self):
        """
        Function: draw()
            A function that draws the Marble object

        Parameters:
            self

        Returns:
            None

        Defense:
            None
        """
        # if self.visible and not self.is_empty:
        # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        """
        Function: draw_empty()
            A function that draws the previous space with a blank space

        Parameters:
            self

        Returns:
            None

        Defense:
            None
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)

    def erase(self):
        """
        Function: erase()
            A function that erases the space of the Marble

        Parameters:
            self

        Returns:
            None

        Defense:
            None
        """
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        """
        Function: clicked_in_region()
            A function that moves the cursor to the selected region

        Parameters:
            self
            x
            y

        Returns:
            False

        Defense:
            None
        """
        if abs(x - self.position.x) <= self.size * 2 and \
                abs(y - self.position.y) <= self.size * 2:
            print("clicked in region")
            return True
        return False