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
    title = "Way too Many Circles All Around"
    width = 600
    height = 600
    x = 0
    y = 0
    radius = 250

    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)

    colors = randomPal()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)

    linewidth = 2
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
    startx = 300
    starty = 50
    turtle.goto(startx, starty)
    amountOfCircles = 360//10
    for i1 in range(0, 3):
        if i1 == 1:
            linewidth += 1
            start = 0
            radius = radius // 2
            starty = 175
            turtle.goto(startx, starty)
        elif i1 == 2:
            linewidth += 2
            start = 5
            radius = radius // 2
            starty = 235
            turtle.goto(startx, starty)
        else:
            start = 5
        for i in range(0,amountOfCircles):
            turtle.color(random.choice(colors))
            # turtle.penup()
            turtle.circle(radius,start + i * 10)
            turtle.pendown()
            x, y = turtle.pos()
            draw_better_circle(turtle,x,y,radius//5,linewidth)
            # fillCircle(turtle, x, y, radius//5)
            turtle.penup()
            turtle.goto(startx,starty)

    turtle.color("black")
    fillCircle(turtle, 300, 300, 20)

    turtle.penup()

    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
