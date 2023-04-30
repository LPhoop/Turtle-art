import math
import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

MIN_DIST = 10
MAX_ANGLE = 10
FORWARD_LENGTH = 10

def dist(x,y,x2,y2):
    return math.sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2))

def drawWobblyLine(turtle, x, y, x2, y2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    xn, yn = turtle.pos()
    while dist(xn, yn, x2, y2) > MIN_DIST:
        angle = turtle.towards(x2,y2)
        angle = angle + random.uniform(-MAX_ANGLE, MAX_ANGLE)
        turtle.setheading(angle)
        length = random.uniform(FORWARD_LENGTH/2, FORWARD_LENGTH)
        turtle.forward(length)
        xn,yn = turtle.pos()

    # angle = turtle.towards(x2, y2)

    turtle.goto(x2,y2)



def Draw():
    width = 800
    height = 600

    title = "Rough Line Squares (weird thing in the middle)"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    turtle.pensize(15)
    x,y,x2,y2 = 0,0,800,600

    while x2 - x > 10:
        turtle.color(random.choice(colors))
        drawWobblyLine(turtle,x,y,x,y2)
        drawWobblyLine(turtle, x, y2, x2, y2)
        drawWobblyLine(turtle, x2, y2, x2, y)
        drawWobblyLine(turtle, x2, y, x, y)
        x += 15
        y += 15
        x2 -= 15
        y2 -= 15

    # for i in range(30):
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     x2 = random.randint(0, width)
    #     y2 = random.randint(0, height)
    #     turtle.color(random.choice(colors))
    #     drawWobblyLine(turtle, x, y, x2, y2)

    turtle.penup()

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()