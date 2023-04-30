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

def drawKline(turtle, length, level):
    if level == 1:
        turtle.forward(length)
    else:
        l = length/3
        # turtle.forward(length)
        drawKline(turtle, l, level-1)
        turtle.left(60)
        drawKline(turtle, l, level-1)
        turtle.right(120)
        drawKline(turtle, l, level-1)
        turtle.left(60)
        drawKline(turtle, l, level-1)

def Draw():
    title = "Koch Line"
    width = 800
    height = 600
    #cellSize = 100
    L = 700

    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = 'black'

    screen.bgcolor('black')
    turtle.color('white')
    turtle.pensize(2)

    # Get everything setup
    turtle.penup()
    turtle.goto(50,50)
    turtle.setheading(0)
    turtle.pendown()

    # Draw a kline-2
    # length = L/3
    # length2 = L / 9
    #turtle.forward(length)
    drawKline(turtle, L, 8)
    # turtle.left(60)
    # drawKline(turtle, L)
    #
    # turtle.right(120)
    # drawKline(turtle, L)
    #
    # turtle.left(60)
    # turtle.forward(length2)
    # turtle.left(60)
    # turtle.forward(length2)
    # turtle.right(120)
    # turtle.forward(length2)
    # turtle.left(60)
    # turtle.forward(length2)
    # turtle.penup()

    # Draw a kline-1
    # length = L/3
    # turtle.forward(length)
    # turtle.left(60)
    # turtle.forward(length)
    # turtle.right(120)
    # turtle.forward(length)
    # turtle.left(60)
    # turtle.forward(length)
    turtle.penup()

    screen.mainloop()




# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()