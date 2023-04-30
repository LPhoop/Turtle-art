import turtle
import random

# Set up the turtle
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.tracer(False)
turtle.hideturtle()

# Define the color palettes
background_palettes = [
    ["#F5DEB3", "#FFE4C4", "#F0E68C", "#BDB76B", "#556B2F"],
    ["#7FFFD4", "#00CED1", "#5F9EA0", "#4682B4", "#B0C4DE"],
    ["#FFB6C1", "#FFC0CB", "#FF69B4", "#FF1493", "#C71585"]
]

star_palettes = [
    ["#FFD700", "#FFE4B5", "#FFC125", "#FFB90F", "#FFA500"],
    ["#F08080", "#FA8072", "#CD5C5C", "#DC143C", "#FF0000"],
    ["#98FB98", "#90EE90", "#3CB371", "#2E8B57", "#228B22"]
]

# Choose a random background color palette
background_colors = random.choice(background_palettes)

# Choose a random star color palette
star_colors = random.choice(star_palettes)

# Set the background color
screen.bgcolor(background_colors[0])

# Define the number of stars and the size range
num_stars = 150
min_size = 10
max_size = 30

# Draw the stars
for i in range(num_stars):
    # Choose a random position
    x = random.uniform(-screen.window_width()/2, screen.window_width()/2)
    y = random.uniform(-screen.window_height()/2, screen.window_height()/2)

    # Choose a random size
    size = random.uniform(min_size, max_size)

    # Choose a random color
    color = random.choice(star_colors)

    # Draw the star
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for j in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Update the screen
turtle.update()

turtle.done()
