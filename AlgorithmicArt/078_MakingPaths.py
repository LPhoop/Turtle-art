import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, draw_better_circle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

def randomPal():
    p = randomPalette()
    print(p)
    return p

def Draw():
    title = "Making Paths"
    width = 600
    height = 600
    cellSize = 100
    numCols = width // cellSize
    numRows = height // cellSize

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    # screen.tracer(1)
    # turtle.showturtle()

    colors = randomPal()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    linewidth = 3
    turtle.pensize(linewidth)
    turtle.penup()
    # turtle.goto(300,300)
    # turtle.color("black")
    for col in range(0, numCols):
        for row in range(0, numRows):
            x = col * cellSize
            y = row * cellSize
            turtle.setheading(0)
            turtle.color(random.choice(colors))
            turtle.begin_fill()
            turtle.goto(x + 15, y + 15)
            turtle.pendown()
            for i in range(0,4):
                turtle.forward(cellSize - 30)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()

            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(x + cellSize, y + cellSize)
            turtle.penup()

            turtle.goto(x + cellSize, y)
            turtle.pendown()
            turtle.goto(x, y + cellSize)
            turtle.penup()





    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
