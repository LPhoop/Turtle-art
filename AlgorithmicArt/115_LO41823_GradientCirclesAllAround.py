import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, draw_better_circle, drawGradientCircle
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
    title = "Gradient Circles Around but messed up"
    width = 800
    height = 600
    radius = 250

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)

    colors = randomPal()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    linewidth = 3
    turtle.pensize(linewidth)
    # turtle.penup()
    # turtle.goto(400,50)
    # turtle.circle(radius,90,90)
    # turtle.pendown()
    # x = turtle.xcor()
    # y = turtle.ycor()
    # x, y = turtle.pos()
    # draw_better_circle(turtle, x, y, radius//2, linewidth)
    turtle.penup()
    turtle.goto(400, 50)
    number = random.randint(5,10)
    amountOfCircles = 360//10
    for i in range(0,amountOfCircles):
        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.circle(radius,0 + i * 10)
        x,y = turtle.pos()
        color1 = random.choice(colors)

        color2 = random.choice(colors)
        if (color1 == color2):
            while (color1 == color2):
                color2 = random.choice(colors)
        drawGradientCircle(turtle, x, y, radius, number, color1, color2)
        turtle.color()
        turtle.goto(400,50)

    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
