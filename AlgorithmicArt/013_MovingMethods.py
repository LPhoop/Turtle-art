from AlgorithmicArt.drawMethods import drawForwardSlash, drawUpLine, drawSideLine, drawCircle, drawDiamond, drawSquare, \
    drawBackSlash
from AlgorithmicArt.util import getTurtleAndScreen
import random
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

width=800
height = 600
cellSize=50
numCols= width//cellSize
numRows= height//cellSize

colors = ["red","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]
# Palette hex or something
colors1 = ["#75c8ae","#5a3d2b","#FFECB4","#E5771E","#F4A127"]

turtle, screen = getTurtleAndScreen("Palette Slashes",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.

# turtle.color("blue")
line_width = random.randint(0,10)
turtle.pensize(line_width)

# for debugging turtle drawing path
# screen.tracer(1)
# turtle.showturtle()

def randomPaletteColor():
    # color = colors[random.choice()]
    color = random.choice(colors1)
    return color

def randomColor():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color


def draw():
    global color
    bg = randomPaletteColor()
    screen.bgcolor(bg)
    colors1.remove(bg)
    for row in range(0, numRows):
        for col in range(0, numCols):
            x = col * cellSize
            y = row * cellSize
            color = randomColor()
            turtle.color(randomPaletteColor())
            randColor = random.randint(0, 5)
            if randColor == 0:
                drawForwardSlash(turtle, x, y, cellSize)
            elif randColor == 1:
                drawBackSlash(turtle, x, y, cellSize)
            elif randColor == 2:
                drawSideLine(turtle, x, y, cellSize)
            elif randColor == 3:
                drawUpLine(turtle, x, y, cellSize)
            elif randColor == 4:
                if random.randint(0, 1):
                    drawSquare(turtle, x, y, cellSize)
                else:
                    drawDiamond(turtle, x, y, cellSize)
            else:
                drawCircle(turtle, x, y, cellSize)
                circleIn = random.randint(0, 2)
                if circleIn == 0:
                    drawUpLine(turtle, x, y, cellSize)
                elif circleIn == 1:
                    drawSideLine(turtle, x, y, cellSize)
                else:
                    drawSideLine(turtle, x, y, cellSize)
                    drawUpLine(turtle, x, y, cellSize)
    turtle.penup()
    # turtle
    screen.mainloop()


# draw()

if __name__ == '__main__':
    draw()