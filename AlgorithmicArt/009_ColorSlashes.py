from AlgorithmicArt.util import getTurtleAndScreen
import random
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

width=800
height = 600
cellSize=50
numCols= width//cellSize
numRows= height//cellSize

colors = ["red","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]


turtle, screen = getTurtleAndScreen("Checkerboard",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.
screen.bgcolor("beige")
turtle.color("blue")
turtle.pensize(2)

# def randomPaletteColor():


def drawForwardSlash(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + cellSize, y + cellSize)

def drawBackSlash(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x + cellSize, y)
    turtle.pendown()
    turtle.goto(x, y + cellSize)

def randomColor():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color


for row in range (0,numRows):
    for col in range(0,numCols):
        x = col*cellSize
        y = row*cellSize
        color = randomColor()
        turtle.color(color)
        if random.randint(0, 1) == 0:
            drawForwardSlash(turtle, x, y, cellSize)
        else:
            drawBackSlash(turtle, x, y, cellSize)

turtle.penup()
# turtle

screen.mainloop()