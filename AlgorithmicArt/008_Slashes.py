from AlgorithmicArt.util import getTurtleAndScreen
import random
# Drawing a checkerboard with turtle
# IN this version I use colors created in different ways
# CAC, 2022

# For this one I determine the size of the screen by first realizing I want
# to break it up into an 8x8 grid of a given size square cell.
width=800
height = 600
cellSize=50
numCols= width//cellSize
numRows= height//cellSize

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
colors = ["red","yellow",(0,255,0),"#FFFFFF",'#0000BB',(127,127,127),"turquoise","#E8205A"]

# Compute the overall width and height.


# To make things easier, you can use my utility methods to get a turtle and screen.
# It will make it much easier to get the exact size screen you want with no extra
# space anywhere you don't want it. For some reason the default turtle stuff is
# flaky, and it seems to be impossible to get things to work exactly like you want
# without going through a lot of effort, which is why I did it for you.
turtle, screen = getTurtleAndScreen("Checkerboard",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.
screen.bgcolor("beige")
turtle.color("blue")
turtle.pensize(2)

for row in range (0,numRows):
    for col in range(0,numCols):
        x = col*cellSize
        y = row*cellSize
        if random.randint(0,1)==0:
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.goto(x+cellSize,y+cellSize)
        else:
            turtle.penup()
            turtle.goto(x+cellSize, y)
            turtle.pendown()
            turtle.goto(x, y + cellSize)

turtle.penup()
# turtle

screen.mainloop()