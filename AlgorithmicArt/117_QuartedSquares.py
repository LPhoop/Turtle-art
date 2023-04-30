import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, fillSquare
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen


# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']


def fillQuartedSquare(turtle, x, y, radius, colors):
    turtle.color(random.choice(colors))
    fillSquare(turtle, x - radius // 2, y - radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x - radius // 2, y + radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x + radius // 2, y + radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x + radius // 2, y - radius // 2, radius // 2)


p = randomPalette()
print(p)
colors = p


def Draw():
    title = "Quartered Squares"
    width = 800
    height = 800
    cellSize = 50
    numCols = width // cellSize
    numRows = height // cellSize

    number = random.randint(2, 8)
    title = title + " " + str(number) + " Rings"
    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)

    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2
    turtle.pensize(lineWidth)

    for row in range(0, numRows):
        for col in range(0, numCols):
            radius = cellSize // 2
            x = col * cellSize + radius
            y = row * cellSize + radius
            color = random.choice(colors)
            turtle.color(color)
            newRad = radius * .8
            fillQuartedSquare(turtle, x, y, newRad, colors)
            # fillQuartedSquare(turtle, x,y, newRad, colors)

    turtle.penup()
    turtle.goto(0, 0)

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
