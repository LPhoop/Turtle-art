import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, draw_better_circle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

p = randomPalette()
print(p)
colors = p


def Triangles(turtle, x, y, length, colors, level):
    if level >= 1:
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(x, y)
        turtle.left(60)
        turtle.pendown()
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        Triangles(turtle,x, y, length//3, colors, level-1)


# title = title + " " + str(levels) + " Levels"

def Draw():
    title = "Wicked Cool Triangles"
    width = 800
    height = 600
    x = 0
    y = 0

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    screen.tracer(1)
    turtle.showturtle()

    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    turtle.color('black')
    turtle.pensize(5)

    turtle.color

    ScreenSquares(turtle,x, y, width,height, colors , 20)

    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
