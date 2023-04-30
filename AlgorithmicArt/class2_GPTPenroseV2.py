# CAC (4/3/23)
# Me:
# That seems to draw random stars and weird shapes.
# Are you sure that is correct?
#
# ChatGPT:
# I apologize for the confusion. The code I provided earlier was incorrect.
# Here's an example code that draws a Penrose tiling using Python turtle:
#
# <The code in this file>
#
# This code draws a Penrose tiling using a combination of rhombus and
# kite shapes.
# The draw_rhombus and draw_kite functions draw a rhombus and a kite,
# respectively, while the draw_penrose_tile function combines these
# shapes to draw a Penrose tile. Finally, the draw_penrose_tiling
# function uses draw_penrose_tile to draw a Penrose tiling by
# iterating over a grid of tiles.

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

def draw_penrose_tiling(t, size, n, fill=False):
    t.speed('fastest')
    t.penup()
    t.goto(-size * n / 2, size * n / 2)
    t.pendown()
    for i in range(n):
        for j in range(n):
            draw_penrose_tile(t, size, fill)
            t.penup()
            t.forward(size * 2)
            t.pendown()
        t.penup()
        t.goto(-size * n / 2, t.ycor() - size * 2)
        t.pendown()

t = turtle.Turtle()
t.hideturtle()
draw_penrose_tiling(t, 20, 10, fill=True)
turtle.done()