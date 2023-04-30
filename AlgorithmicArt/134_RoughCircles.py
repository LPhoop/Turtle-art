import math
import random

from AlgorithmicArt.drawMethods import fillCircle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

p = randomPalette()
print(p)
colors = p

def roughCircle(turtle,x,y,radius):
    startAngle = random.randint(0,359)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(startAngle)
    turtle.forward(radius)
    # turtle.goto(x,y-radius)
    # turtle.setheading(0)
    c = 2*math.pi*radius
    dist = c/360
    turtle.begin_fill()
    # turtle.setheading(startAngle)
    for i in range(0,359):
        angle = random.randrange(-15,15)
        turtle.pendown()
        turtle.setheading(startAngle*i+90 + angle)
        turtle.forward(dist)
        turtle.penup()
    turtle.end_fill()

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
            color= random.choice(colors)
            turtle.color(color)
            extent = random.randint(30, 359)
            start = random.randint(0, 359)
            rad = radius * 0.8
            roughCircle(turtle,x,y,rad)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()