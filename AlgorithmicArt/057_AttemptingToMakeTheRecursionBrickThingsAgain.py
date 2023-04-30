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


def ScreenSquares(turtle, x, y, width, height, colors,  minDim=20):
    turtle.penup()
    turtle.color(random.choice(colors))
    if width - x > 40 and height - y > 40:
        if random.randint(0, 1) == 0: # horizontal left
            new_y = random.randint(y + minDim, height - minDim)
            turtle.goto(x, new_y)
            turtle.pendown()
            turtle.goto(width, new_y)
            ScreenSquares(turtle, x, y, width, new_y, colors)
            ScreenSquares(turtle, x, new_y, width, height, colors)
        else: # vetical left
            new_x = random.randint(x + minDim, width - minDim)
            turtle.goto(new_x, y)
            turtle.pendown()
            turtle.goto(new_x, height)
            ScreenSquares(turtle, x, y, new_x, height, colors)
            ScreenSquares(turtle, new_x, y, width, height, colors)
    else:
        None

    # if width > minDim or height > minDim:
    #     turtle.goto(x, y)
    #     turtle.pendown()
    #     turtle.goto(x, height)
    #     turtle.goto(width, height)
    #     turtle.goto(width, y)
    #     turtle.goto(x, y)
    #     turtle.penup()
    #     nextOrientation = random.randint(0, 1)
    #     # Split at horizontal or vertical
    #     if nextOrientation == 0:
    #         ScreenSquares(turtle, )
    #     else:
    #
    # else:
    #     None



# title = title + " " + str(levels) + " Levels"

def Draw():
    title = "Wicked Cool Squares"
    width = 800
    height = 600
    x = 0
    y = 0

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    # screen.tracer(1)
    # turtle.showturtle()

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
