import math
import random

from AlgorithmicArt.drawMethods import fillCircle
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
    # turtle.goto(x,y)
    # turtle.setheading(startAngle)
    # turtle.forward(radius)
    # # turtle.goto(x,y-radius)
    # # turtle.setheading(0)
    # c = 2*math.pi*radius
    # dist = c/360
    # turtle.begin_fill()
    # # turtle.setheading(startAngle)
    # for i in range(0,359):
    #     angle = random.randrange(-15,15)
    #     turtle.pendown()
    #     turtle.setheading(startAngle*i+90 + angle)
    #     turtle.forward(dist)
    #     turtle.penup()
    # turtle.end_fill()

def Draw():
    title = "Circles"
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

    for row in range (0,numRows):
        for col in range(0,numCols):
            radius = cellSize//2
            x = col*cellSize + radius
            y = row*cellSize + radius
            color1= random.choice(colors)
            turtle.fillcolor(color1)
            turtle.pencolor(color1)
            extent = random.randint(30, 359)
            start = random.randint(0, 359)
            rad = radius * 0.8
            rad = radius
            roughCircle(turtle,x,y,rad)
            color2 = random.choice(colors)
            if (color2 == color1):
                while (color2 == color1):
                    color2 = random.choice(colors)
            turtle.fillcolor(color2)
            roughCircle(turtle, x, y, rad//2)
            if (color2 == color1):
                while (color2 == color1):
                    color1 = random.choice(colors)
            turtle.fillcolor(color1)
            roughCircle(turtle, x, y, rad // 3)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()