import math
import random

from AlgorithmicArt.drawMethods import drawGradientCircle, drawGradientSquare, drawGradientSquareOLD, \
    drawGradientTriangle
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

    title = "Gradient Triangles and Squares and Circles Randomly"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    screen.bgcolor(bg)
    penSize = 4
    turtle.pensize(penSize)
    number = random.randint(3,9)

    num = random.randint(10, 50)

    for i in range(0,num):
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        if (color1 == color2):
            while (color1 == color2):
                color2 = random.choice(colors)
        x = random.randint(0,width- cellsize)
        y = random.randint(0,height - cellsize)
        shape = random.randint(0, 3)
        if shape == 0:
            drawGradientSquare(turtle, x, y, cellsize, number, color1, color2)
        elif shape == 1:
            drawGradientTriangle(turtle, x, y, cellsize, number, color1, color2)
        elif shape == 2:
            drawGradientCircle(turtle, x + radius, y + radius, radius, number, color1, color2)


    # for row in range(rows):
    #     for col in range(cols):
    #         x = cellsize*col
    #         y = cellsize*row
    #         color1=random.choice(colors)
    #         color2=random.choice(colors)
    #         if (color1==color2):
    #             while (color1 == color2):
    #                 color2 = random.choice(colors)
    #         if random.randint(0,1) == 0:
    #             drawGradientSquare(turtle, x, y, cellsize, number, color1, color2)
    #         if random.randint(0, 1) == 0:
    #             drawGradientTriangle(turtle, x, y, cellsize, number, color1, color2)
    #         if random.randint(0, 1) == 0:
    #             drawGradientCircle(turtle, x + radius *2, y + radius*2, radius, number, color1, color2)
    #         turtle.color()


    turtle.penup()
    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()