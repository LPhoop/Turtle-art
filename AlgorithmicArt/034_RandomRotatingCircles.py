from AlgorithmicArt.drawMethods import drawForwardSlash, drawUpLine, drawSideLine, drawCircle, drawDiamond, drawSquare, \
    drawBackSlash, draw_better_circle
from AlgorithmicArt.palettes import randomNamedPalette
from AlgorithmicArt.util import getTurtleAndScreen
import random
width=800
height = 600
cellSize=100
numCols= width//cellSize
numRows= height//cellSize

turtle, screen = getTurtleAndScreen("Cool Circles",width,height,moveWorld=True)

p = randomNamedPalette()
print(p)
name, colors = p
# name,colors = randomNamedPalette()

line_width = 1
turtle.pensize(line_width)

# for debugging turtle drawing path
# screen.tracer(1)
# turtle.showturtle()

def drawSquares():
    # bg = random.choice(colors)
    # screen.bgcolor(bg)
    # colors.remove(bg)
    square_num = 0
    for row in range(0, numRows):
        for col in range(0, numCols):
            x = col * cellSize
            y = row * cellSize
            if square_num%2 == 0:
                turtle.color("black")
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.goto(x + cellSize, y)
                turtle.goto(x + cellSize, y + cellSize)
                turtle.goto(x, y + cellSize)
                turtle.goto(x, y)
                turtle.end_fill()
            elif square_num%2 == 1:
                turtle.color("White")
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.goto(x + cellSize, y)
                turtle.goto(x + cellSize, y + cellSize)
                turtle.goto(x, y + cellSize)
                turtle.goto(x, y)
                turtle.end_fill()
            square_num += 1

    turtle.penup()
    turtle.goto(0, 0)

def drawCircles():
    bg = random.choice(colors)
    screen.bgcolor(bg)
    colors.remove(bg)
    square_num = 0
    # start = 0
    for row in range(0, numRows):
        for col in range(0, numCols):
            start = random.randint(0, 360)
            turtle.color(random.choice(colors))
            radius = cellSize//2
            x = col * cellSize + radius
            y = row * cellSize + radius

            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            # turtle.begin_fill()
            drawCircle(turtle, x, y, radius, lineWidth=10, extent=180, start=start)
            drawCircle(turtle, x, y, radius//2, lineWidth=6, extent=180, start=start + 180)
            turtle.color(random.choice(colors))
            drawCircle(turtle, x, y, radius, lineWidth=10, extent=180, start=start + 180)
            drawCircle(turtle, x, y, radius//2, lineWidth=6, extent=180, start=start)
            start += 5





    turtle.penup()
    turtle.goto(0, 0)


def DrawTriangle(x, y, cellSize, direction="upright"):
    if direction == "upright":
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + cellSize // 2, y + cellSize)
        turtle.goto(x + cellSize, y)
        turtle.goto(x, y)
    elif direction == "down":
        turtle.penup()
        turtle.goto(x, y + cellSize)
        turtle.pendown()
        turtle.goto(x + cellSize, y + cellSize)
        turtle.goto(x + cellSize // 2, y)
        turtle.goto(x, y + cellSize)
    elif direction == "left":
        turtle.penup()
        turtle.goto(x + cellSize, y + cellSize)
        turtle.pendown()
        turtle.goto(x + cellSize, y)
        turtle.goto(x, y + cellSize // 2)
        turtle.goto(x + cellSize, y + cellSize)
    elif direction == "right":
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x, y + cellSize)
        turtle.goto(x + cellSize, y + cellSize // 2)
        turtle.goto(x, y)


if __name__ == '__main__':
    drawCircles()
    screen.mainloop()