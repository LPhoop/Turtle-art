# CAC (4/3/23)
# Me:
# Can you draw a penrose tiling using python turtle?
#
# ChatGPT:
# Yes, it is possible to draw a Penrose tiling using Python Turtle.
# Here's an example code that draws a Penrose tiling using Turtle graphics:
#
# <The code in this file>
#
# This code uses the turtle module to draw the Penrose tiling recursively.
# The penrose function takes in two arguments:
# size, which determines the size of the largest rhombus in the tiling,
# and depth, which determines the level of recursion.
# The base case for the recursion is depth <= 0,
# and the recursive step is to draw two smaller rhombi and call the
# penrose function again with size/2 and depth-1.
# The colors used in the tiling are arbitrary and can be changed to
# suit your preferences.

import turtle


# Define the recursive function for drawing the Penrose tiling
def penrose(size, depth):
    if depth <= 0:
        return
    else:
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-size / 2, size / 2)
        turtle.pendown()
        turtle.color("#FDB813")
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

        turtle.color("#DB0A5B")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(size / 2, -size / 2)
        turtle.pendown()
        for i in range(5):
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

        turtle.color("#0B4F6C")
        penrose(size / 2, depth - 1)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.right(36)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)
        penrose(size / 2, depth - 1)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(72)


# Set up the Turtle screen and drawing settings
turtle.setup(800, 800)
turtle.bgcolor("#ffffff")
turtle.title("Penrose Tiling")
turtle.hideturtle()

# Draw the Penrose tiling
penrose(400, 3)

# Keep the Turtle window open until manually closed
turtle.done()