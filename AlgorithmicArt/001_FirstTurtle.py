import turtle

# A very basic example of working with turtle.
# CAC, 2022

# Define the width and height you want here so you can easily change it
WIDTH, HEIGHT = 800, 600

# Get the screen that the turtle will draw on
screen = turtle.Screen()
# Set the size of the window. Notice that it is a little larger than
# the width and height. This takes into account the borders and such.
screen.setup(WIDTH + 4, HEIGHT + 8)
# Set the coordinate system that you want to draw on.
# This will give a canvas with lower left corner (0,0)
# and upper right corner (WIDTH,HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle.penup()
turtle.goto(300,300)

turtle.pendown()
turtle.color("green")
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(500,200)
turtle.pendown()
turtle.pensize(4)
turtle.begin_fill()
turtle.pencolor("blue")
turtle.fillcolor("yellow")
turtle.setheading(0)
turtle.circle(50)
turtle.end_fill()

# Make this the last statement. It will make the screen keep displaying.
# If you remove this, the screen will draw and then immediately disappear.
turtle.mainloop()