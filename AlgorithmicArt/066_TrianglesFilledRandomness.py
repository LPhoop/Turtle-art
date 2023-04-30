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

        turtle.fillcolor(random.choice(colors))
        turtle.begin_fill()
        turtle.forward(length//2)
        tempx = turtle.xcor()
        tempy = turtle.ycor()
        turtle.forward(length // 2)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.end_fill()

        length = random.randint(200,400)
        x = random.randint(0, 800)
        y = random.randint(0, 600)

        Triangles(turtle,x, y, length//2, colors, level-1)
        Triangles(turtle, tempx, tempy, length // 2, colors, level - 1)
        Triangles(turtle, x + length//2, y, length // 2, colors, level - 1)

# title = title + " " + str(levels) + " Levels"

def Draw():
    title = "Wicked Cool Triangles blown up"
    width = 800
    height = 600
    x = 200
    y = 100
    level = random.randint(2,8)
    title = title + " " + str(level) + " Levels"

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    turtle.penup()
    turtle.goto(width / 2, .25 * height)
    # screen.tracer(1)
    # turtle.showturtle()

    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    turtle.color('black')
    turtle.pensize(1)

    # turtle.color

    Triangles(turtle,x, y, 400, colors, level)

    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
