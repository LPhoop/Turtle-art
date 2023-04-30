from AlgorithmicArt.drawMethods import drawForwardSlash, drawUpLine, drawSideLine, drawCircle, drawDiamond, drawSquare, \
    drawBackSlash, draw_better_circle
from AlgorithmicArt.util import getTurtleAndScreen
import random
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

width=800
height = 600
cellSize=20
numCols= width//cellSize
numRows= height//cellSize

colors = ["red","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]
# Palette hex or something
colors1 = ["#75c8ae","#5a3d2b","#FFECB4","#E5771E","#F4A127"]

colors3 = ['#FF48C4', '#2BD1FC', '#F3EA5F', '#C04DF9', '#FF3F3F']


turtle, screen = getTurtleAndScreen("Triangles n' Circles",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.

# turtle.color("blue")
# line_width = random.randint(0,10)
line_width = 3
turtle.pensize(line_width)

# for debugging turtle drawing path
# screen.tracer(1)
# turtle.showturtle()

def randomPaletteColor():
    # color = colors[random.choice()]
    color = random.choice(colors3)
    return color

def randomColor():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color

def draw_background_stripes(turtle, num_stripes):
    row_height = height//num_stripes
    x = 0
    y = 0

    for stripe in range(1, num_stripes):
        turtle.penup()
        turtle.goto(0, stripe * row_height)
        turtle.color(randomColor())
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(0, stripe * row_height + row_height)
        turtle.goto(width, stripe * row_height + row_height)
        turtle.goto(width, stripe * row_height)
        turtle.goto(0, stripe * row_height)

        turtle.end_fill()

def circles_in_circles():
    #bg = randomPaletteColor()
    #screen.bgcolor(bg)
    #colors1.remove(bg)
    for row in range (0,numRows):
        for col in range(0,numCols):
            radius = cellSize//2 - 10
            x = col*cellSize + radius + 10
            y = row*cellSize + radius + 10
            color=randomPaletteColor()
            turtle.color(color)
            turtle.begin_fill()
            drawCircle(turtle,x,y,radius,line_width)
            turtle.end_fill()
            color = randomPaletteColor()
            turtle.color(color)
            turtle.begin_fill()
            drawCircle(turtle, x, y, radius//2, line_width)
            turtle.end_fill()

    turtle.penup()
    turtle.goto(0,0)

def drawTriangles():
    # bg = randomPaletteColor()
    screen.bgcolor('black')
    # colors3.remove(bg)
    for row in range(0, numRows):
        for col in range(0, numCols):
            radius = cellSize // 2
            x = col * cellSize
            y = row * cellSize
            color = randomPaletteColor()
            turtle.color(color)
            rand_num = random.randint(0, 5)

            if rand_num == 0:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + cellSize//2, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y)
            elif rand_num == 1:
                turtle.penup()
                turtle.goto(x, y + cellSize)
                turtle.pendown()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.goto(x + cellSize//2, y)
                turtle.goto(x, y + cellSize)
            elif rand_num == 2:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y + cellSize//2)
                turtle.goto(x, y)
            elif rand_num == 3:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y)
            elif rand_num == 4:
                turtle.penup()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x + cellSize, y + cellSize)
            else:
                turtle.penup()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.pendown()
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y + cellSize//2)
                turtle.goto(x + cellSize, y + cellSize)
    turtle.penup()
    turtle.goto(0, 0)

def trianglesInCircles():
    for row in range(0, numRows):
        for col in range(0, numCols):
            x = 0
            y = 0

if __name__ == '__main__':
    cellSize = 100
    numCols = width // cellSize
    numRows = height // cellSize
    screen.mainloop()