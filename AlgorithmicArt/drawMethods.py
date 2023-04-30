from random import random, choice

'''
def randomPaletteColor():
    # color = colors[random.choice()]
    color = random.choice(colors1)
    return color
'''


def drawForwardSlash(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + cellSize, y + cellSize)


def drawBackSlash(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x + cellSize, y)
    turtle.pendown()
    turtle.goto(x, y + cellSize)


def drawUpLine(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x + (cellSize / 2), y)
    turtle.pendown()
    turtle.goto(x + (cellSize / 2), y + cellSize)


def drawSideLine(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y + (cellSize / 2))
    turtle.pendown()
    turtle.goto(x + cellSize, y + (cellSize / 2))


def drawCircle_old(turtle, x, y, cellSize, line_width=1):
    turtle.penup()
    turtle.goto(x + (cellSize / 2), y + line_width / 2)
    turtle.pendown()
    # turtle.begin_fill()
    turtle.circle(cellSize / 2 - line_width / 2)
    # turtle.end_fill()


def drawCircle(turtle, x, y, radius, lineWidth=1, extent=360, start=0):
    """
    Draw a circle centered at (x,y) with overall radius of radius,
    line width of lineWidth, going around extent degrees starting
    at start degrees
    :param turtle: The object to draw on
    :param x: x-coordinate of the center of the circle
    :param y: y-coordinate of the center of the circle
    :param radius: radius of the circle
    :param lineWidth: width of the line around the circle
    :param extent: how many degrees of the circle to draw
    :param start: the starting angle of the circle.
    :return:
    """
    turtle.penup()
    turtle.goto(x, y - radius + lineWidth // 2)
    turtle.setheading(0)
    turtle.circle(radius - lineWidth // 2, extent=start)
    turtle.pendown()
    lw = turtle.pensize()
    turtle.pensize(lineWidth)
    turtle.circle(radius - lineWidth // 2, extent=extent)
    turtle.pensize(lw)


def fillCircle(turtle, x, y, radius, extent=360, start=0):
    '''
    Draw a filled circle center at xy with radius
    :param turtle:
    :param x:
    :param y:
    :param radius:
    :param lineWidth:
    :return:
    '''
    lw = turtle.pensize()
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(x + radius, y)
    turtle.setheading(90)
    turtle.circle(radius, extent=start)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius, extent=extent)
    turtle.goto(x, y)
    turtle.end_fill()

    turtle.pensize(lw)


def drawConcentricCircle(turtle, x, y, radius, number, colors, extent=360, start=0, forceDifferentColors=False):
    color = choice(colors)
    for i in range(0, number):
        r = (number - i) * radius / number
        turtle.color(color)
        fillCircle(turtle, x, y, r, extent=extent, start=start)
        new_color = choice(colors)
        if (forceDifferentColors):
            while (color == new_color):
                new_color = choice(colors)


def drawSquare(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # turtle.begin_fill()
    turtle.goto(x, y + cellSize)
    turtle.goto(x + cellSize, y + cellSize)
    turtle.goto(x + cellSize, y)
    turtle.goto(x, y)
    # turtle.end_fill()


def drawDiamond(turtle, x, y, cellSize):
    turtle.penup()
    turtle.goto(x, y + (cellSize / 2))
    turtle.pendown()
    # turtle.begin_fill()
    turtle.goto(x + (cellSize / 2), y + cellSize)
    turtle.goto(x + cellSize, y + (cellSize / 2))
    turtle.goto(x + (cellSize / 2), y)
    turtle.goto(x, y + (cellSize / 2))
    # turtle.end_fill()


def draw_better_circle(turtle, x, y, radius, lineWidth):
    turtle.penup()
    # x = x +
    turtle.goto(x, y - radius + lineWidth // 2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(radius - lineWidth // 2)


def drawTriangle(turtle, x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + length // 2, y + length)
    turtle.goto(x + length, y)
    turtle.goto(x, y)


def randomColor():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color


def drawGradientCircle(turtle, x, y, radius, number, color1, color2, extent=360, start=0, forceDifferentColors=False):
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * radius / number
        turtle.color(color)
        fillCircle(turtle, x, y, r, extent=extent, start=start)


def ithGradient(turtle, color1, color2, n, i):
    '''

    :param turtle:
    :param color1:
    :param color2:
    :param n: Number of colors
    :param i: a number between 0 and n-1 inclusive.
    :return:
    '''
    turtle.color(color1)
    draw, fill = turtle.color()
    r,g,b = draw
    turtle.color(color2)
    draw, fill = turtle.color()
    r2, g2, b2 = draw
    rr = r * (n - i - 1) / (n - 1) + r2 * i / (n - 1)
    gg = g * (n - i - 1) / (n - 1) + g2 * i / (n - 1)
    bb = b * (n - i - 1) / (n - 1) + b2 * i / (n - 1)

    return int(rr), int(gg), int(bb)

def drawGradientSquareOLD(turtle, x, y, length, number, color1, color2):
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x,y)
        turtle.setheading(0)
        turtle.pendown()
        for side in range(4):
            turtle.forward(r)
            turtle.left(90)

def drawGradientSquare(turtle, x, y, length, number, color1, color2):
    OriginalPen = turtle.pensize()
    turtle.pensize(1)
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        adjust = r / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + length//2,y + length//2)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        for side in range(4):
            turtle.forward(r)
            turtle.left(90)
        turtle.end_fill()
        turtle.pensize(OriginalPen)

def drawGradientTriangle(turtle, x, y, length, number, color1, color2):
    OriginalPen = turtle.pensize()
    turtle.pensize(1)
    for i in range(0, number):
        color = ithGradient(turtle, color1, color2, number, i)
        r = (number - i) * length / number
        adjust = r / number
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + length//2,y + length//2)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.right(90)
        turtle.forward(r//2)
        turtle.setheading(60)
        turtle.pendown()
        turtle.begin_fill()
        for side in range(3):
            turtle.forward(r)
            turtle.right(120)
        turtle.end_fill()
        turtle.pensize(OriginalPen)

def fillSquare(turtle,x,y,radius):
    turtle.penup()
    turtle.goto(x-radius,y-radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(2*radius)
        turtle.left(90)
    turtle.end_fill()

def drawConcentricSquare(turtle, x, y, radius, number, colors, forceDifferentColors=True):
    color = choice(colors)
    for i in range(0, number):
        r = (number - i) * radius / number
        turtle.color(color)
        fillSquare(turtle, x, y, r)
        new_color = choice(colors)
        if (forceDifferentColors):
            while (color == new_color):
                new_color = choice(colors)

def fillQuartedSquare(turtle, x, y, radius, colors):
    turtle.color(random.choice(colors))
    fillSquare(turtle, x - radius // 2, y - radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x - radius // 2, y + radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x + radius // 2, y + radius // 2, radius // 2)
    turtle.color(random.choice(colors))
    fillSquare(turtle, x + radius // 2, y - radius // 2, radius // 2)


