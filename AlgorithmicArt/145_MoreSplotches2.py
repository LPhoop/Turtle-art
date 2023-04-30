import math
import random

from AlgorithmicArt.drawMethods import fillCircle, drawSquare
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Rough Circles
# LO, 3/2023

p = randomPalette()
print(p)
colors = p
num_points = 180
percent = .08

def roughCircle(turtle,x,y,radius):
    # startAngle = random.randint(0,359)
    # num_points = 50
    turtle.penup()
    margin = round(radius * percent)
    points = []
    for i in range(0, num_points-1):
        turtle.goto(x,y)
        turtle.setheading(i*360/num_points)
        # margin = round(radius *.05)
        turtle.forward(radius+random.randrange(-margin,margin))
        points.append(turtle.pos())
    turtle.goto(points[0])
    turtle.pendown()
    turtle.begin_fill()
    for p in points:
        turtle.goto(p)
    turtle.end_fill()

def Draw():
    title = "splotches lars overos"
    width = 800
    height = 600
    cellSize = 200
    numCols = width // cellSize
    numRows = height // cellSize

    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2
    turtle.pensize(lineWidth)
    radius = cellSize // 2
    amount = random.randint(200,500)
    for i in range(0,amount):
        radius = random.randint(30,150)
        x = random.randint(0,width)
        y = random.randint(0,height)
        turtle.pencolor("black")
        turtle.fillcolor(random.choice(colors))
        type = random.randint(0, 2)
        if type == 0:
            roughCircle(turtle, x, y, radius)
        elif type == 1:
            turtle.setheading(random.randint(0,359))
            turtle.begin_fill()
            turtle.circle(radius, steps=3)
            turtle.end_fill()
        elif type == 2:
            turtle.begin_fill()
            drawSquare(turtle, x, y, cellSize)
            turtle.end_fill()

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()