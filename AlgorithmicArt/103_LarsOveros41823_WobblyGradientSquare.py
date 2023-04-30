import math
import random

from AlgorithmicArt.drawMethods import drawGradientCircle, drawGradientSquare, drawGradientSquareOLD, ithGradient
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Concentric Squares
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

def drawWobblyGradientSquare(turtle, x, y, length, number, color1, color2):
    OriginalPen = turtle.pensize()
    turtle.pensize(1)
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        adjust = r / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + length//2,y + length//2)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.setheading(0)
        turtle.pendown()
        xc, yc = turtle.pos()
        turtle.begin_fill()
        drawWobblyLine(turtle, xc, yc, xc + length, yc)
        drawWobblyLine(turtle, xc + length, yc, xc + length, yc + length)
        drawWobblyLine(turtle, xc + length, yc + length, xc, yc + length)
        drawWobblyLine(turtle, xc, yc + length, xc, yc)
        # for side in range(4):
        #     turtle.forward(r)
        #     turtle.left(90)
        turtle.end_fill()
        turtle.pensize(OriginalPen)

def Draw():
    width = 3732
    height = 2100
    cellsize = 200
    radius = cellsize//2
    cols = width//cellsize
    rows = height//cellsize

    title = "Buildings Type Thing"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = "#2b2d4d"
    screen.bgcolor(bg)
    penSize = 4
    turtle.pensize(penSize)
    number = random.randint(3,9)
    color2 = (255,255,255)
    num = random.randint(10, 50)

    for row in range(rows):
        for col in range(cols):
            x = cellsize*col
            y = cellsize*row
            color1=random.choice(colors)
            color2=random.choice(colors)
            if (color1==color2):
                while (color1 == color2):
                    color2 = random.choice(colors)
            newCell = cellsize * .5
            drawWobblyGradientSquare(turtle, x, y, newCell, number, color1, color2)
            turtle.color()


    turtle.penup()
    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()