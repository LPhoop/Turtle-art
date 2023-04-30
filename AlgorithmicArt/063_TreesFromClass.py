import random

from AlgorithmicArt.palettes import randomPalette
from AlgorithmicArt.util import getTurtleAndScreen
# Tree, using recursion. This time we vary some of the parameters
# to get different looks. We also vary the exact angle of each branch
# to get a more organic look
# CAC, 3/31/2023

def drawTree(turtle,length,lengthFactor,angle,level,colors):
    randomnessFactor = 15
    realAngle=angle/2
    newLength = length*lengthFactor
    if level > 0:
        # Draw a line
        turtle.color(random.choice(colors))
        turtle.forward(length)
        # Save the position of the turtle and its heading
        x, y = turtle.pos()
        ang = turtle.heading()
        # Turn to face where we want the right tree and draw it.
        # But add a little shift to the actual distance so the branches
        # aren't so uniform.
        shift = random.randint(-randomnessFactor,randomnessFactor)
        turtle.right(realAngle+shift)
        drawTree(turtle, newLength, lengthFactor, angle, level - 1, colors)
        # Go back to the starting location and face toward where
        # we want the left tree to be and draw it. Again, here
        # we add a little shift for a more organic look.
        turtle.penup()
        turtle.goto(x, y)
        shift = random.randint(-randomnessFactor,randomnessFactor)
        turtle.setheading(ang + realAngle+shift)
        turtle.pendown()
        drawTree(turtle, newLength, lengthFactor, angle, level - 1, colors)
def Draw():
    width = 800
    height = 600

    # How many levels of the tree to draw
    level = random.randint(4,9)
    # The angle between branches at each fork
    # (120 is probably too wide)
    angle = random.randint(45,120)
    # How mush shorter/longer branches should get
    lengthFactor = random.uniform(.8,1.2)
    # An estimate of how tall/wide of a drawing we can have
    # Since the exact size of the trees are somewhat unpredictable,
    # this is just our best estimate.
    maxDim = max(height*.75, width//2)
    # How long should the first line be.
    # The formula used here is based on the fact that the line
    # lengths are a geometric progression, and there is a formula
    # for the sum of these numbers.
    # It's hard to describe the details in text, but the idea
    # is that the line length should be the drawable width divided
    # by the partial sum of the powers of the length factors.
    length = maxDim*(lengthFactor-1)/(pow(lengthFactor,level+1)-1)

    title = "Recursive Tree "+str(level)+" "+str(angle)+" "+str(round(lengthFactor,3))
    turtle, screen = getTurtleAndScreen(title,width,height,moveWorld=True)

    colors = randomPalette()
    bg = random.choice(colors)
    colors.remove(bg)
    screen.bgcolor(bg)
    turtle.pensize(2)

    turtle.penup()
    if angle > 100:
        # If the angle is wider, we need to move the tree up
        # because it will wrap around the bottom
        turtle.goto(width/2,.35*height)
    else:
        turtle.goto(width/2,.25*height)
    turtle.pendown()

    turtle.setheading(90)
    drawTree(turtle,length,lengthFactor,angle,level,colors)

    turtle.penup()

    screen.mainloop()
# ----------------------------------------------------------------
if __name__ == '__main__':
   Draw()