import math
import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
import drawMethods

# Hexagons
# NOTE: I edited this a little after class,
# so this will look a little different (and better!).
# CAC, 4/14/2023

MIN_DIST = 10
MAX_ANGLE = 10
FORWARD_LENGTH = 10


def dist(x, y, x2, y2):
    return math.sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2))


def drawWobblyLine(turtle, x, y, x2, y2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    xn, yn = turtle.pos()
    while dist(xn, yn, x2, y2) > MIN_DIST:
        angle = turtle.towards(x2, y2)
        angle = angle + random.uniform(-MAX_ANGLE, MAX_ANGLE)
        turtle.setheading(angle)
        length = random.uniform(FORWARD_LENGTH / 2, FORWARD_LENGTH)
        turtle.forward(length)
        xn, yn = turtle.pos()

    # angle = turtle.towards(x2, y2)

    turtle.goto(x2, y2)



def Draw():

    width = 800
    height = 600
    cellSize = 50
    numCols = width // cellSize
    numRows = height // cellSize

    title = "Squares different color sides"
    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    turtle.pensize(10)
    for col in range(0, numCols):
        turtle.color(random.choice(colors))
        start_y = random.randint(10, height)
        x = col * cellSize
        start_x = x + cellSize/2

        turtle.penup()
        turtle.goto(start_x,start_y)
        turtle.pendown()
        turtle.goto(start_x, 0)

        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(x, start_y)
        turtle.pendown()
        turtle.goto(x, height)




    turtle.penup()
    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
