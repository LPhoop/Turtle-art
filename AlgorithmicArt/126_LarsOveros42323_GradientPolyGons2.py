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

def drawWobblyGradientTriangle(turtle, x, y, length, number, color1, color2):
    OriginalPen = turtle.pensize()
    turtle.pensize(1)
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + length//2,y + length//2)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.setheading(60)
        # turtle.pendown()
        x1, y1 = turtle.pos()
        turtle.forward(r)
        x2, y2 = turtle.pos()
        turtle.right(120)
        turtle.forward(r)
        x3,y3 = turtle.pos()
        # turtle.pendown()
        turtle.begin_fill()
        drawWobblyLine(turtle, x1, y1, x2, y2)
        drawWobblyLine(turtle, x2, y2, x3, y3)
        drawWobblyLine(turtle, x3, y3, x1, y1)

        turtle.end_fill()
        turtle.pensize(OriginalPen)

def drawGradientPolygon(turtle, x, y, length, number, color1, color2):
    OriginalPen = turtle.pensize()
    turtle.pensize(1)
    turtle.penup()
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + length,y)
        turtle.setheading(0)
        turtle.pendown()
        # xc, yc = turtle.pos()
        turtle.begin_fill()
        turtle.circle(r, steps=6)
        turtle.end_fill()
        turtle.pensize(OriginalPen)

def Draw():
    width = 800
    height = 800
    cellsize = 100
    radius = cellsize//2
    cols = width//cellsize
    rows = height//cellsize

    title = "Gradient Shapes"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    # bg = random.choice(colors)
    screen.bgcolor("black")
    penSize = 4
    turtle.pensize(penSize)
    number = random.randint(5,10)
    length = cellsize//2

    for row in range(rows):
        for col in range(cols):
            x = cellsize*col
            y = cellsize*row
            # color1=random.choice(colors)
            color1=random.choice(colors)
            color2 = random.choice(colors)
            if (color2==color1):
                while (color2 == color1):
                    color1 = random.choice(colors)
            turtle.pencolor(color1)
            # turtle.goto(x + cellsize//2,y + cellsize//2)
            # turtle.pendown()
            # turtle.circle(cellsize//2,steps=6)
            turtle.penup()
            drawGradientPolygon(turtle, x,y,radius,number, color1, color2)
            turtle.penup()
            turtle.color()
            colors = randomPalette()


    turtle.penup()
    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()