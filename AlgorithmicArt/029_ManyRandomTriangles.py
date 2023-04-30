from AlgorithmicArt.drawMethods import drawForwardSlash, drawUpLine, drawSideLine, drawCircle, drawDiamond, drawSquare, \
    drawBackSlash, draw_better_circle
from AlgorithmicArt.palettes import randomNamedPalette
from AlgorithmicArt.util import getTurtleAndScreen
import random
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

width=800
height = 600
cellSize=100
numCols= width//cellSize
numRows= height//cellSize

# colors = ["red","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]
# # Palette hex or something
# colors1 = ["#75c8ae","#5a3d2b","#FFECB4","#E5771E","#F4A127"]
#
# colors3 = ['#FF48C4', '#2BD1FC', '#F3EA5F', '#C04DF9', '#FF3F3F']


turtle, screen = getTurtleAndScreen("Triangles Random Palette",width,height,moveWorld=True)

p = randomNamedPalette()
print(p)
name, colors = p
# name,colors = randomNamedPalette()

# bg = random.choice(colors)
# colors.remove(bg)


# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.

# turtle.color("blue")
# line_width = random.randint(0,10)
line_width = 1
turtle.pensize(line_width)

# for debugging turtle drawing path
# screen.tracer(1)
# turtle.showturtle()

def drawTriangles():
    bg = random.choice(colors)
    screen.bgcolor(bg)
    colors.remove(bg)
    for row in range(0, numRows):
        for col in range(0, numCols):
            # radius = cellSize // 2
            x = col * cellSize + cellSize//2
            y = row * cellSize + cellSize//2
            turtle.color(random.choice(colors))
            tempSize = random.randint(cellSize//4, cellSize - 10)
            x -= tempSize // 2 - 5
            y -= tempSize // 2 - 5

            rand_num = random.randint(0, 3)
            # if rand_num == 0:
            #     turtle.penup()
            #     turtle.goto(x, y)
            #     turtle.pendown()
            #     turtle.goto(x + tempSize // 2, y + tempSize)
            #     turtle.goto(x + tempSize, y)
            #     turtle.goto(x, y)

            if rand_num == 0:
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize)
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2)
                DrawTriangle(x, y - 5, tempSize)
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 2)
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2)
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 3)
                turtle.end_fill()
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 3)
            elif rand_num == 1:
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize, "down")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "down")
                DrawTriangle(x, y - 5, tempSize, "down")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize//2, "down")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "down")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 3, "down")
                turtle.end_fill()
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 3, "down")
            elif rand_num == 2:
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize, "right")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "right")
                DrawTriangle(x, y - 5, tempSize, "right")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 2, "right")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "right")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 3, "right")
                turtle.end_fill()
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 3, "right")
            else:
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize, "left")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "left")
                DrawTriangle(x, y - 5, tempSize, "left")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 2, "left")
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 2, "left")
                DrawTriangle(x, y - 5, tempSize // 2, "left")
                turtle.color(random.choice(colors))
                turtle.begin_fill()
                DrawTriangle(x, y - 5, tempSize // 3, "left")
                turtle.end_fill()
                turtle.end_fill()
                turtle.color("black")
                DrawTriangle(x, y - 5, tempSize // 3, "left")

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
    drawTriangles()
    screen.mainloop()