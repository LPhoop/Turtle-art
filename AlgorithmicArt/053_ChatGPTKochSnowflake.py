import turtle
import random

def koch(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch(length/3, depth-1)
            turtle.left(angle)

# Setup turtle
turtle.setup(800, 800)
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

# Draw 10 random Koch snowflakes
for i in range(10):
    # Randomize length and depth
    length = random.randint(50, 200)
    depth = random.randint(1, 5)
    # Set random color
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)
    # Draw Koch snowflake
    for j in range(3):
        koch(length, depth)
        turtle.right(120)

turtle.done()
