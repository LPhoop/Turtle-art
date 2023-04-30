import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Tree, using recursion.
# CAC, 3/31/2023
num_points = 180
percent = .08

def roughCircle(turtle,x,y,radius):
    # startAngle = random.randint(0,359)
    # num_points = 50
    turtle.penup()
    margin = round(radius * percent)
    points = []
    for i in range(0, num_points-1):
        turtle.goto(x,y)
        turtle.setheading(i*360/num_points)
        # margin = round(radius *.05)
        turtle.forward(radius+random.randrange(-margin,margin))
        points.append(turtle.pos())
    turtle.goto(points[0])
    turtle.pendown()
    turtle.begin_fill()
    for p in points:
        turtle.goto(p)
    turtle.end_fill()

def drawTree(turtle,length,angle,level,colors, typeA):
    realAngle=angle/2
    if level >0: # If level <=0, draw nothing.
        if typeA:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.forward(length)
            drawTree(turtle, length, angle, level - 1, colors, False)
            heading = turtle.heading()
            turtle.pendown()

            x, y = turtle.pos()
            roughCircle(turtle, x, y, random.randint(20, 50))
            turtle.setheading(heading)

        else:
            heading = turtle.heading()
            x, y = turtle.pos()
            roughCircle(turtle, x, y, random.randint(20, 50))
            turtle.setheading(heading)
            version = random.randint(0,1)
            x, y = turtle.pos()
            heading = turtle.heading()
            turtle.left(realAngle)
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()
            # turtle.right(realAngle)
            if version:
                drawTree(turtle,length,angle,level-1,colors, True)
            else:
                drawTree(turtle, length, angle, level - 1, colors, False)
            turtle.penup()
            turtle.goto(x,y)
            turtle.setheading(heading-realAngle)
            turtle.pendown()
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()
            if version:
                drawTree(turtle, length, angle, level - 1, colors, False)
            else:
                drawTree(turtle, length, angle, level - 1, colors, True)

    else:
        x,y = turtle.pos()
        roughCircle(turtle,x,y,random.randint(20,50))

def Draw():
    level = random.randint(5,15)
    # level = 10
    title = "Recursive Tree With Leaves "+str(level)

    width = 800
    height = 600
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    turtle.pensize(4)

    length = height/(level+2)
    angle = 45

    turtle.penup()
    turtle.goto(width/2,length*1.5)
    turtle.pendown()

    turtle.setheading(90)
    drawTree(turtle,length,angle,level,colors, True)

    turtle.penup()

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()