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

def drawKSnowFlake(turtle, l, level):
    drawKline(turtle, l, level)
    turtle.right(120)
    drawKline(turtle,l,level)
    turtle.right(120)
    drawKline(turtle,l,level)

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
    L = 500
    levels = random.randint(1,6)
    title = title + " " + str(levels) + " Levels"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = 'black'

    screen.bgcolor('black')
    turtle.color('white')
    turtle.pensize(2)

    # Get everything setup
    turtle.penup()
    turtle.goto(150,150)
    turtle.setheading(60)
    turtle.pendown()
    drawKSnowFlake(turtle, L, levels)

    turtle.penup()

    screen.mainloop()




# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()