"""
    Garfield Maitland
    CS 5001
    09/30/2023
    Homework 3
"""
import turtle
from PositionService import get_position_x, get_position_y, set_position_x, set_position_y


def start_position():
    """
        Function: start_position()
        Starts the position for Turtle and draws as green circle with radius 80.

    Parameters:
        None

    Preconditions:
        None

    Returns:
        None
    """
    turtle.bgpic("shape_window.png")
    turtle.penup()
    x = get_position_x()
    y = get_position_y()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("GREEN")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    set_position_x(x)
    set_position_y(y)


def move(x, y):
    """
        Function: move()
        Clears the circle that is specified at (x, y) coordinates.

    Parameters:
        x (float): The x-coordinate for the turtle.
        y (float): The y-coordinate for the turtle.

    Preconditions:
        None

    Returns:
        None

    Prints:
        If a new position is registered, the function prints the position.
        If a position is ignored, the function prints the position.
    """
    if x - get_position_x() <= 80 and y - get_position_y() <= 80:
        set_position_x(x)
        set_position_y(y)
        turtle.clear()
        start_position()
        print(f"{x},{y} New position")
    else:
        print(f"{x},{y} Ignored position")



def main():
    turtle.onscreenclick(move)
    start_position()
    turtle.done()


if __name__ == "__main__":
    main()
