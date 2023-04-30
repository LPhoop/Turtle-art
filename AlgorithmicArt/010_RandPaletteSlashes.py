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
color70 = ["#75c8ae","#5a3d2b","#FFECB4","#E5771E","#F4A127"]

turtle, screen = getTurtleAndScreen("Palette Slashes",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.

# turtle.color("blue")
turtle.pensize(2)

# for debugging turtle drawing path
# screen.tracer(1)
# turtle.showturtle()

def randomPaletteColor():
    # color = colors[random.choice()]
    color = random.choice(color70)
    return color

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

def drawUpLine(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x + (cellSize/2), y)
    turtle.pendown()
    turtle.goto(x + (cellSize/2), y + cellSize)

def drawSideLine(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y + (cellSize/2))
    turtle.pendown()
    turtle.goto(x + cellSize, y + (cellSize/2))

def drawCircle(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x + (cellSize / 2), y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(cellSize/2)
    turtle.end_fill()

def randomColor():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color


bg = randomPaletteColor()
screen.bgcolor(bg)
color70.remove(bg)

for row in range (0,numRows):
    for col in range(0,numCols):
        x = col*cellSize
        y = row*cellSize
        color = randomColor()
        turtle.color(randomPaletteColor())
        randColor = random.randint(0, 4)
        if randColor == 0:
            drawForwardSlash(turtle, x, y, cellSize)
        elif randColor == 1:
            drawBackSlash(turtle, x, y, cellSize)
        elif randColor == 2:
            drawSideLine(turtle, x, y, cellSize)
        elif randColor == 3:
            drawCircle(turtle, x, y, cellSize)
        else:
            drawUpLine(turtle, x, y, cellSize)

turtle.penup()
# turtle

screen.mainloop()