import math
import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

MIN_DIST = 10
MAX_ANGLE = 10
FORWARD_LENGTH = 10

def dist(x,y,x2,y2):
    return math.sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2))

def drawWobblyLine(turtle, x, y, x2, y2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    xn, yn = turtle.pos()
    while dist(xn, yn, x2, y2) > MIN_DIST:
        angle = turtle.towards(x2,y2)
        angle = angle + random.uniform(-MAX_ANGLE, MAX_ANGLE)
        turtle.setheading(angle)
        length = random.uniform(FORWARD_LENGTH/2, FORWARD_LENGTH)
        turtle.forward(length)
        xn,yn = turtle.pos()

    # angle = turtle.towards(x2, y2)

    turtle.goto(x2,y2)



def Draw():
    width = 800
    height = 600
    title = "Rough Line Grid of Triangles (bad)"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)
    cellSize = 50
    numCols = width // cellSize
    numRows = height // cellSize

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    pensize = 3
    turtle.pensize(pensize)
    x,y,x2,y2 = 0,0,800,600

    for col in range(0, numCols):
        for row in range(0, numRows):
            turtle.penup()
            x = col * cellSize
            y = row * cellSize
            turtle.setheading(0)
            turtle.color(random.choice(colors))
            turtle.pensize(pensize)
            turtle.goto(x,y)
            turtle.pendown()
            turtle.begin_fill()
            drawWobblyLine(turtle, x,y, x+ cellSize/2,y + cellSize)
            drawWobblyLine(turtle, x+cellSize/2,y+cellSize, x+cellSize,y)
            drawWobblyLine(turtle,x+cellSize,y,x,y)
            turtle.end_fill()
            turtle.penup()

    turtle.penup()

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()