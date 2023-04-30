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
    title = "Random Squigles"
    width = 600
    height = 600
    x = 0
    y = 0
    radius = 250

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)
    # screen.tracer(1)
    # turtle.showturtle()

    colors = randomPal()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    linewidth = 2
    turtle.pensize(linewidth)
    turtle.penup()
    turtle.goto(300,300)
    turtle.color("black")
    for i in range(0, random.randint(300, 1000)):
        x,y = turtle.pos()
        if x >= 600 or x <=0 or y >= 600 or y <= 0:
            turtle.goto(300,300)

        turtle.pendown()
        turtle.setheading(random.randint(0,360))
        turtle.forward(random.randint(5, 30))
        turtle.penup()




    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
