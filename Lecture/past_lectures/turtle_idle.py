import turtle

# Set up your screen
scrn = turtle.Screen()
scrn.bgcolor("black")  # Change the background color if needed

# Create a new turtle
N = turtle.Turtle()
N.color('red')
N.width(5)

N.fillcolor('white')

# Draw a block-style letter 'N'
N.begin_fill()
N.left(90)
N.forward(100)
N.right(145)
N.forward(141.4)
N.left(145)
N.forward(100)
N.left(145)
N.forward(141.4)
N.right(145)
N.forward(100)
N.penup()
N.hideturtle()
N.end_fill()

# Keep the window open
turtle.done()
