import random
from AlgorithmicArt.util import getTurtleAndScreen

# Circles
# CAC, 3/2023

def drawCircle(turtle,x,y,radius,lineWidth):
    turtle.penup()
    turtle.goto(x,y-radius+lineWidth//2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(radius-lineWidth//2)

colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']
def randomPaletteColor():
    return random.choice(colors)

def Draw():
    title = "Circles"
    width = 800
    height = 600
    cellSize = 50
    numCols = width // cellSize
    numRows = height // cellSize

    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    bg = randomPaletteColor()
    screen.bgcolor(bg)
    colors.remove(bg)

    lineWidth = 2*random.randint(1,10)
    turtle.pensize(lineWidth)

    for row in range (0,numRows):
        for col in range(0,numCols):
            radius = cellSize//2
            x = col*cellSize + radius
            y = row*cellSize + radius
            color=randomPaletteColor()
            turtle.color(color)
            drawCircle(turtle,x,y,radius,lineWidth)

    turtle.penup()
    turtle.goto(0,0)

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()