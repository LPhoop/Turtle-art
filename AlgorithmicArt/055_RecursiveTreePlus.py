import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, draw_better_circle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Tree using recursion
# CAC, 3/2023

p = randomPalette()
print(p)
colors = p

def DrawTree(turtle, length, length_factor, level, angle):
    real_angle = angle/2
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(length)
    new_length = length * length_factor
    if level <= 1:
        # turtle.forward(length)
        None
    else:
        x,y=turtle.pos()
        turtle.right(real_angle)
        ang = turtle.heading()
        DrawTree(turtle, length, angle, level - 1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(ang)
        turtle.left(angle)
        turtle.pendown()
        DrawTree(turtle,length,angle,level-1)


# title = title + " " + str(levels) + " Levels"

def Draw():
    level = random.randint(4,7)
    title = "Wicked Cool Tree"
    width = 600
    height = 600
    length = 50
    length_factor = random.randint(0.5, 1)
    title = title + " " + str(level) + " Levels"
    turtle, screen = getTurtleAndScreen(title, width, height, moveWorld=True)

    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor('black')
    # screen.bgcolor(bg)

    turtle.setheading(90)

    color = random.choice(colors)
    turtle.color(color)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(width / 2, 10)
    turtle.pendown()

    DrawTree(turtle,length, length_factor, level, 60)


    turtle.penup()
    screen.mainloop()


# ----------------------------------------------------------------
if __name__ == '__main__':
    Draw()
