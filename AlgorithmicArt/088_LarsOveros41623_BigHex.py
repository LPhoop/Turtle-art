import math
import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Hexagons
# NOTE: I edited this a little after class,
# so this will look a little different (and better!).
# CAC, 4/14/2023

def drawHexagon(turtle, x, y, radius):
    turtle.penup()
    turtle.goto(x,y-radius) # The bottom center of the hexagon

    # You can use the circle method to draw hexagons!
    # turtle.setheading(0)
    # turtle.pendown()
    # turtle.begin_fill()
    # turtle.circle(radius,steps=6)
    # turtle.end_fill()

    # Or you can draw them the old-fashioned way!
    # This way is better because it allows more flexibility
    # if you want to change things up a bit (e.g. skip drawing
    # one of the sides).
    turtle.setheading(30)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(radius)
        turtle.left(60)
    turtle.end_fill()

def Draw():
    width = 800
    height = 600
    cellHeight = 200
    cellWidth=cellHeight*math.sqrt(3)//2
    radius = cellHeight//2
    cols = round(width//cellWidth)
    rows = round(height//(cellHeight-radius/2))

    title = "Tons of (big) Hexagons"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    penSize = 4
    turtle.pensize(penSize)
    # Make the radius used to draw a little smaller to take into account the line width
    # But we still need to original radius to do the calculations of locations
    # I made it subtract penSize rather than penSize/2 so there are spaces between the hexagons.
    drawRadius = radius - penSize

    for row in range(rows+1):
        for col in range(cols+1):
            # The exact starting x and y locations can be tweaked to get the edges to look
            # exactly how you want. For both, just add a "+blah" to make each by blah pixels
            # to the right/up.
            y = (cellHeight-radius/2) * row
            if row%2==0:
                x = cellWidth*col + 10
            else: # Every other row needs to be shifted over to line up correctly.
                x = cellWidth*col + radius*math.sqrt(3)/2  + 10

            turtle.pencolor("black")
            turtle.fillcolor(random.choice(colors))
            drawHexagon(turtle,x,y,drawRadius)
            turtle.fillcolor(random.choice(colors))
            drawHexagon(turtle, x, y, drawRadius / 1.2)
            turtle.fillcolor(random.choice(colors))
            drawHexagon(turtle, x, y, drawRadius/1.5)
            drawHexagon(turtle, x, y, drawRadius//2)
            turtle.fillcolor(random.choice(colors))
            drawHexagon(turtle, x, y, drawRadius // 3)
            turtle.fillcolor(random.choice(colors))
            drawHexagon(turtle, x, y, drawRadius // 6)

    turtle.penup()
    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()