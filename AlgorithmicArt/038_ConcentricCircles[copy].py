import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

p = randomPalette()
print(p)
colors = p

def Draw():
    title = "Circles"
    width = 800
    height = 600
    cellSize = 100
    numCols = width // cellSize
    numRows = height // cellSize

    number = random.randint(2, 8)
    title = title + " " + str(number) + " Rings"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2*random.randint(1,10)
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
            drawConcentricCircle(turtle, x, y, radius, number, colors, extent=extent, start=start)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()