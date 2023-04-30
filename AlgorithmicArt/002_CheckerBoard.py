from AlgorithmicArt.util import getTurtleAndScreen
# Drawing a checkerboard with turtle
# CAC, 2022

# For this one I determine the size of the screen by first realizing I want
# to break it up into an 8x8 grid of a given size square cell.
cellSize=70
numCols=8
numRows=8

# Compute the overall width and height.
width = cellSize*numCols
height = cellSize*numRows

# To make things easier, you can use my utility methods to get a turtle and screen.
# It will make it much easier to get the exact size screen you want with no extra
# space anywhere you don't want it. For some reason the default turtle stuff is
# flaky, and it seems to be impossible to get things to work exactly like you want
# without going through a lot of effort, which is why I did it for you.
turtle, screen = getTurtleAndScreen("Checkerboard",width,height,moveWorld=True)

# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.
screen.bgcolor("gray")

for row in range (0,8):
    for col in range(0,8):
        # Move to the lower left corner of the cell.
        turtle.penup()
        turtle.goto(col*cellSize,row*cellSize)
        turtle.pendown()

        # Determine what color should be used based on location in the grid.
        if (row+col)%2==0:
            turtle.color("black")
        else:
            turtle.color("white")

        # Draw a square, filled in.
        turtle.begin_fill()
        turtle.setheading(0)
        for i in range(0,4):
            turtle.forward(cellSize)
            turtle.left(90)
        turtle.end_fill()

screen.mainloop()