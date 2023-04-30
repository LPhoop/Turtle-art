import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Concentric Quartered Squares
# CAC, 4/19/2023

def fillSquareLL(turtle,x,y,side):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def fillQuarteredSquare(turtle,x,y,side,colors):
    rad = side//2
    turtle.color(random.choice(colors))
    fillSquareLL(turtle,x-rad,y,rad)
    turtle.color(random.choice(colors))
    fillSquareLL(turtle,x,y,rad)
    turtle.color(random.choice(colors))
    fillSquareLL(turtle,x,y-rad,rad)
    turtle.color(random.choice(colors))
    fillSquareLL(turtle,x-rad,y-rad,rad)

def drawConcentricQSquares(turtle, x, y, side, number, colors):
    for i in range(0,number):
        newSide =(number-i)*side/number
        fillQuarteredSquare(turtle,x,y,newSide,colors)

def Draw():
    title = " Concentric Quartered Squares"
    width = 800
    height = 600
    cellSize = 200
    numCols = width // cellSize
    numRows = height // cellSize

    number = random.randint(2, 6)
    title=title+" "+str(number)
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)
    turtle.pensize(1)

    for row in range (0,numRows):
        for col in range(0,numCols):
            radius = cellSize//2
            x = col*cellSize + radius
            y = row*cellSize + radius
            newSide = cellSize*.9
            drawConcentricQSquares(turtle, x, y, newSide, number, colors)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()