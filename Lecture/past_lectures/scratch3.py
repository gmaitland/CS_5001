import turtle

g = turtle.Turtle()
g.speed(5)

def turtle_square(turtle, x, y):
    """
    Function: turtle_square()
    Draws a blue square centered at the specified (x, y) coordinates.

    Parameters:
    
        x (float): The x-coordinate for the center of the square.
        y (float): The y-coordinate for the center of the square.

    Preconditions:
        None

    Returns:
        None
    """

    # Moves to the specified (x, y) coordinates
    g.penup()
    g.goto(x - 40, y - 40)  # Adjusting the position so the square is centered at (x, y)

    # Draw a blue square
    g.pendown()
    g.color("Blue")
    g.begin_fill()
    g.forward(80)
    g.left(90)
    g.forward(80)
    g.left(90)
    g.forward(80)
    g.left(90)
    g.forward(80)
    g.end_fill()


def turtle_circle(turtle, x, y):
    """
    Function: turtle_circle()
    Draw a magenta circle centered at the specified (x, y) coordinates.

    Parameters:
        turtle (turtle.Turtle): The turtle object for drawing.
        x (float): The x-coordinate for the center of the circle.
        y (float): The y-coordinate for the center of the circle.

    Preconditions:
        None
    Returns:
        None
    """

    # Draw a magenta circle
    g.penup()
    g.goto(x - 40, y)  # Move to the center of the square's left edge
    g.pendown()

    g.color("Magenta")
    g.begin_fill()
    g.circle(40)
    g.end_fill()


def get_user_coordinates():
    """
    Function: get_user_coordinates()
    Prompt the user to enter x and y coordinates.

    Parameters:
        x (float): The x-coordinate for the center of the circle.
        y (float): The y-coordinate for the center of the circle.

    Preconditions:
        None

    Returns:
        user-provided x and y coordinates.
    """
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    return x, y

def main():
  x, y = get_user_coordinates()
  turtle_square(g, x, y)
  
  x1, y1 = get_user_coordinates()  # Get coordinates for the circle separately
  turtle_circle(g, x1, y1)
  
  turtle.done()

if __name__ == "__main__":
    main()
