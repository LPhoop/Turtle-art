import turtle

# Create a turtle to draw with
t = turtle.Turtle()
t.speed('fastest')

# Set up some constants
center_x = -200
center_y = 0
num_petals = 20
petal_length = 200
petal_width = 30
petal_color = 'yellow'
stroke_color = 'brown'
background_color = '#F0EAD6'

# Draw the background
t.penup()
t.goto(center_x, center_y)
t.pendown()
t.fillcolor(background_color)
t.begin_fill()
t.goto(center_x, center_y - 350)
t.goto(center_x + 600, center_y - 350)
t.goto(center_x + 600, center_y)
t.goto(center_x, center_y)
t.end_fill()

# Draw the petals
t.pensize(petal_width)
t.pencolor(stroke_color)
t.fillcolor(petal_color)
for i in range(num_petals):
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(0)
    t.right(i * (360 / num_petals))
    t.forward(petal_width / 2)
    t.pendown()
    t.begin_fill()
    t.right(30)
    t.circle(petal_length, 60)
    t.right(120)
    t.circle(petal_length, 60)
    t.end_fill()

    # Add brush strokes to the petals
    t.pensize(5)
    t.pencolor(stroke_color)
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(0)
    t.right(i * (360 / num_petals))
    t.forward(petal_width / 2 + 5)
    t.pendown()
    t.right(30)
    for j in range(3):
        t.forward(15)
        t.right(120)
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(0)
    t.right(i * (360 / num_petals))
    t.forward(petal_width / 2 + 10)
    t.pendown()
    t.right(60)
    for j in range(2):
        t.forward(20)
        t.right(120)
