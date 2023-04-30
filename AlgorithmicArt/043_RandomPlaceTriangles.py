import random

from AlgorithmicArt.drawMethods import fillCircle, drawConcentricCircle, drawTriangle
from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

# colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']

p = randomPalette()
print(p)
colors = p

def Draw():
    title = "Random Triangles"
    width = 800
    height = 600
    numTriangles = random.randint(100, 400)
    # number = random.randint(2, 8)
    title = title + " " + str(numTriangles) + " Triangles"
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = random.choice(colors)

    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2*random.randint(1,10)
    turtle.pensize(3)


    for i in range(0, numTriangles):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(5, 50)

        turtle.color(random.choice(colors))
        turtle.penup()
        drawTriangle(turtle, x, y, size)
        turtle.pendown()


    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()