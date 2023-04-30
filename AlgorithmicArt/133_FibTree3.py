import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Tree, using recursion.
# CAC, 3/31/2023

def drawTree(turtle,length,angle,level,colors, typeA):
    realAngle=angle/2

    if level >0: # If level <=0, draw nothing.
        if typeA:
            turtle.color(random.choice(colors))
            turtle.forward(length)
            drawTree(turtle, length * .9, angle, level - 1, colors, False)

        else:
            version = random.randint(0,1)
            x, y = turtle.pos()
            heading = turtle.heading()
            turtle.left(realAngle)
            turtle.color(random.choice(colors))
            turtle.forward(length)
            # turtle.right(realAngle)
            if version:
                drawTree(turtle,length * .9,angle,level-1,colors, True)
            else:
                drawTree(turtle, length * .9, angle, level - 1, colors, False)
            turtle.penup()
            turtle.goto(x,y)
            turtle.setheading(heading-realAngle)
            turtle.pendown()
            turtle.color(random.choice(colors))
            turtle.forward(length)
            if version:
                drawTree(turtle, length * .9, angle, level - 1, colors, False)
            else:
                drawTree(turtle, length * .9, angle, level - 1, colors, True)

def Draw():
    level = random.randint(5,15)
    # level = 10
    title = "Recursive Tree "+str(level)

    width = 800
    height = 600
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    turtle.pensize(4)

    length = height/(level+1)
    angle = 45

    turtle.penup()
    turtle.goto(width/2,length*7)
    turtle.pendown()

    turtle.setheading(270)
    drawTree(turtle,length,angle,level,colors, True)

    turtle.penup()

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()