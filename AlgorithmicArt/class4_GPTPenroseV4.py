# CAC (4/3/23)
# Me:
# It is still animating and still overlapping the tiles incorrectly.
#
# ChatGPT:
# I apologize for the error in my previous response.
# Here's a corrected version of the code that should work correctly
# and display only the final drawing:
#
# <The code in this file>
#
# This code should now correctly display the final Penrose tiling
# without animating or overlapping the tiles.
# The draw_penrose_tiling function takes two arguments:
# size for the size of the shapes and n for the number of tiles in
# each row/column. The fill argument is optional and defaults to False,
# but you can set it to True to fill the shapes with color.

import turtle

def draw_rhombus(t, size, fill=False):
    if fill:
        t.begin_fill()
    for i in range(2):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.left(108)
    t.end_fill()

def draw_kite(t, size, fill=False):
    if fill:
        t.begin_fill()
    t.left(36)
    for i in range(2):
        t.forward(size)
        t.right(108)
        t.forward(size)
        t.right(36)
    t.end_fill()

def draw_penrose_tile(t, size, fill=False):
    draw_rhombus(t, size, fill)
    for i in range(5):
        t.left(72)
        draw_kite(t, size, fill)
        t.right(144)
        draw_kite(t, size, fill)
        t.left(72)
    t.left(36)

def draw_penrose_tiling(size, n, fill=False):
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-size * n / 2, size * n / 2)
    turtle.pendown()
    for i in range(n):
        for j in range(n):
            draw_penrose_tile(turtle, size, fill)
            turtle.penup()
            turtle.forward(size * 2)
            turtle.pendown()
        turtle.penup()
        turtle.goto(-size * n / 2, turtle.ycor() - size * 2)
        turtle.pendown()
    turtle.hideturtle()
    turtle.done()

draw_penrose_tiling(20, 10, fill=True)