from AlgorithmicArt.util import getTurtleAndScreen
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

# For this one I determine the size of the screen by first realizing I want
# to break it up into an 8x8 grid of a given size square cell.
# cellSize=120
cellSize=80
numCols=9
numRows=9

# Here is an array of colors that uses 3 different options:
# 1) Named colors (A limited number are available)
# 2) RGB using values in the range 0-255
# 3) Hex code which is encoding the RGB values in hexadecimal,
#    with 2 hex digits needed for each color.
# A few Notes:
# - The RGB values are specified as a list of 3 values. Quotes are NOT used here
#   because this is not a string.
# - The hex codes are stored in a string that is prefaced with the "#" character.
#   This is to let the turtle color method know that the string is not a named color
#   but is represented in hex code.
# colors = ["blue","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]
colors = ["#8B4513","#228B22",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A", "#FF1493"]

# Compute the overall width and height.
width=cellSize*numCols
height = cellSize*numRows

# To make things easier, you can use my utility methods to get a turtle and screen.
# It will make it much easier to get the exact size screen you want with no extra
# space anywhere you don't want it. For some reason the default turtle stuff is
# flaky, and it seems to be impossible to get things to work exactly like you want
# without going through a lot of effort, which is why I did it for you.
turtle, screen = getTurtleAndScreen("Playing",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.
screen.bgcolor("blue")

for row in range (0,numRows):
    for col in range(0, numCols):
        # Move to the lower left corner of the cell.
        turtle.penup()
        turtle.goto(col*cellSize,row*cellSize)
        turtle.pendown()

        color = (row+col)%9
        turtle.color(colors[color])

        # Draw a square, filled in.
        turtle.begin_fill()
        turtle.setheading(0)
        for i in range(0,4):
            turtle.forward(cellSize)
            turtle.left(90)
        turtle.end_fill()

# turtle.color("purple")
# for i in range(0, 5):
#     turtle.forward(50)
#     turtle.left(45)
#     turtle.forward(50)

turtle.penup()
turtle.goto(200,200)
turtle.color("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.color("black")
turtle.penup()

turtle.goto(230, 310)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
# turtle.
turtle.penup()

turtle.back(60)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()

turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(30)
turtle.pensize(5)

turtle.pendown()
turtle.circle(20, 180)
# turtle.left(90)
# turtle.forward(60)
turtle.penup()

turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(35)
turtle.left(90)

turtle.pendown()
turtle.circle(40, 180)
turtle.penup()

turtle.goto(0,0)

screen.mainloop()