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
line_width = 3
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
            radius = cellSize // 2
            x = col * cellSize
            y = row * cellSize
            turtle.color(random.choice(colors))

            rand_num = random.randint(0, 5)
            if rand_num == 0:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + cellSize//2, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y)
            elif rand_num == 1:
                turtle.penup()
                turtle.goto(x, y + cellSize)
                turtle.pendown()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.goto(x + cellSize//2, y)
                turtle.goto(x, y + cellSize)
            elif rand_num == 2:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y + cellSize//2)
                turtle.goto(x, y)
            elif rand_num == 3:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y)
            elif rand_num == 4:
                turtle.penup()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.pendown()
                turtle.goto(x, y + cellSize)
                turtle.goto(x + cellSize, y)
                turtle.goto(x + cellSize, y + cellSize)
            else:
                turtle.penup()
                turtle.goto(x + cellSize, y + cellSize)
                turtle.pendown()
                turtle.goto(x + cellSize, y)
                turtle.goto(x, y + cellSize//2)
                turtle.goto(x + cellSize, y + cellSize)
    turtle.penup()
    turtle.goto(0, 0)

if __name__ == '__main__':
    drawTriangles()
    screen.mainloop()