import turtle

# Set up the turtle screen
wn = turtle.Screen()
wn.setup(500, 500)
wn.bgcolor("lightblue")

# Create the turtle for the face
face = turtle.Turtle()
face.shape("circle")
face.color("yellow")

# Draw the eyes
left_eye = turtle.Turtle()
left_eye.penup()
left_eye.goto(-30, 50)
left_eye.dot(20)

right_eye = turtle.Turtle()
right_eye.penup()
right_eye.goto(30, 50)
right_eye.dot(20)

# Draw the mouth
mouth = turtle.Turtle()
mouth.penup()
mouth.goto(-50, 0)
mouth.pendown()
mouth.color("red")
mouth.pensize(10)
mouth.right(90)
mouth.circle(50, 180)

# Move the turtle to draw the nose
face.penup()
face.goto(0, 20)
face.pendown()

# Draw the nose
face.color("black")
face.pensize(5)
face.right(60)
face.forward(50)
face.right(120)
face.forward(50)

# Hide the turtle
face.hideturtle()

# Exit the program
turtle.done()
