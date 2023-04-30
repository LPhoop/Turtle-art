import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

p = randomPalette()
print(p)
colors = p

def Draw():
    title = "Random Straight Lines"
    width = 800
    height = 600

    #turtle.pensize(lineWidth)
    numLines = random.randint(10, 300)
    number = random.randint(2, 8)
    title = title + " " + str(numLines)
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    turtle.pensize(random.randint(2, 10))
    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2*random.randint(1,10)


    for i in range(0, numLines):
        turtle.pensize(random.randint(2, 10))
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        #y2 = random.randint(0, height)

        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2,y1)
    for i in range(0, numLines):
        turtle.pensize(random.randint(2, 10))
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        # x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x1,y2)


    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()