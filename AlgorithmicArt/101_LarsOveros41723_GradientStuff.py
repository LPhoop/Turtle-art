import math
import random

from AlgorithmicArt.drawMethods import drawGradientCircle, drawGradientSquare, drawGradientSquareOLD
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Concentric Squares
# NOTE: I edited this a little after class,
# so this will look a little different (and better!).
# CAC, 4/14/2023

def Draw():
    width = 800
    height = 600
    cellsize = 100
    radius = cellsize//2
    cols = width//cellsize
    rows = height//cellsize

    title = "Gradient Squares wrong"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = "#2b2d4d"
    screen.bgcolor(bg)
    penSize = 4
    turtle.pensize(penSize)
    number = random.randint(3,9)
    color2 = (255,255,255)
    num = random.randint(10, 50)

    for row in range(rows):
        for col in range(cols):
            x = cellsize*col
            y = cellsize*row
            color1=random.choice(colors)
            color2=random.choice(colors)
            if (color1==color2):
                while (color1 == color2):
                    color2 = random.choice(colors)
            drawGradientSquareOLD(turtle, x, y, cellsize, number, color1, color2)
            turtle.color()


    turtle.penup()
    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()