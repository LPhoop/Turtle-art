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


def ScreenSquares(turtle, x, y, width, height, colors,  minDim=20, cutoff=40):
    turtle.penup()
    # turtle.color(random.choice(colors))
    turtle.fillcolor(random.choice(colors))
    if width - x > cutoff and height - y > cutoff:
        if width - x <= height - y: # horizontal left
            new_y = random.randint(y + minDim, height - minDim)
            turtle.goto(x, new_y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(x, height)
            turtle.goto(width, height)
            turtle.goto(width, new_y)
            turtle.goto(x, new_y)
            turtle.end_fill()

            ScreenSquares(turtle, x, y, width, new_y, colors)
            ScreenSquares(turtle, x, new_y, width, height, colors)
        else: # vetical left
            new_x = random.randint(x + minDim, width - minDim)
            turtle.goto(new_x, y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(new_x, height)
            turtle.goto(width, height)
            turtle.goto(width, y)
            turtle.goto(new_x, y)
            turtle.end_fill()
            ScreenSquares(turtle, x, y, new_x, height, colors)
            ScreenSquares(turtle, new_x, y, width, height, colors)
    else:
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x, height)
        turtle.goto(width, height)
        turtle.goto(width, y)
        turtle.goto(x, y)
        turtle.end_fill()


# title = title + " " + str(levels) + " Levels"

def Draw():
    title = "Wicked Cool Squares Lars Overos"
    width = 3840
    height = 2160
    x = 0
    y = 0

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    # screen.tracer(1)
    # turtle.showturtle()
    colors = randomPal()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    turtle.color('black')
    turtle.pensize(5)

    # turtle.color

    ScreenSquares(turtle,0, 0, width//2,height//2, colors , 100, cutoff=200)
    colors = randomPal()
    ScreenSquares(turtle, width//2, 0, width, height // 2, colors, 20, cutoff=100)
    colors = randomPal()
    ScreenSquares(turtle, 0, height//2, width // 2, height, colors, 20, cutoff=100)
    colors = randomPal()
    ScreenSquares(turtle, width//2, height//2, width, height, colors, 20, cutoff=100)

    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
