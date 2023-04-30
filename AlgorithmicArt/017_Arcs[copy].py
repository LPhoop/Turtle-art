import random

from AlgorithmicArt.colors import randomPaletteColor
from AlgorithmicArt.drawMethods import drawCircle
from AlgorithmicArt.util import getTurtleAndScreen

# Arcs
# CAC, 3/2023

def Draw():
    title = "Goofy looking Arcs that I am not sure I like"
    width = 800
    height = 600
    cellSize = 50
    numCols = width // cellSize
    numRows = height // cellSize

    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = randomPaletteColor()
    screen.bgcolor(bg)

    for row in range (0,numRows):
        for col in range(0,numCols):
            radius = cellSize//2
            x = col*cellSize + radius
            y = row*cellSize + radius
            color=randomPaletteColor()
            turtle.color(color)

            lineWidth = 2*random.randint(1,10)
            extent = random.randint(90,360)
            start = random.randint(0,359)
            drawCircle(turtle,x,y,radius,lineWidth,extent,start)
            #drawCircle(turtle,x,y,radius)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()