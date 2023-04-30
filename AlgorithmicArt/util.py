from tkinter import Canvas, Tk
from turtle import TurtleScreen, RawTurtle

# Utility methods for working with turtle.
# The first method is the only one that is important.
# Feel free to ignore the rest.
# CAC, 2022

def getTurtleAndScreen(title, width, height, moveWorld=True):
    '''
    Create a screen and a turtle to draw on that screen
    :param title: The title you want on the window.
    :param width: The width of the window/canvas
    :param height: The height of the window/canvas
    :param moveWorld: If set to true, the lower left corner will be (0,0) and
    the upper right will be (width,height)
    Otherwise, the lower left corner will be (-width/2, -height/2), the
    center of the screen will be (0,0), and the upper right will be (width/2,height/2)
    :return: a turtle and a screen
    '''

    root = Tk()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.lift()
    root.wm_title(title)

    canvas = ResizingCanvas(root, desired_width=width, desired_height=height, width=width,
                            height=height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    screen = TurtleScreen(canvas)

    if moveWorld:
        # Need the -1s in the code below because it appears that if we use 0 as the boundary,
        # we don't see things drawn at 0, so we start at -1 instead.
        screen.setworldcoordinates(0, -1, width, height - 1)

    # So you can specify colors using rgb integer values.
    screen.colormode(255)

    # Do not show the turtle drawing.
    screen.tracer(0)

    # Get an invisible turtle.
    turtle = RawTurtle(screen, visible=False)

    return turtle, screen

class ResizingCanvas(Canvas):
    def __init__(self, parent, desired_width, desired_height, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.origHeight = self.height  # save original height
        self.origWidth = self.width  # save original height
        # Need to negate this one. Not sure why.
        self.x_shift = -(self.width - desired_width) // 2
        # Don't need to negate this one. Not sure why.
        self.y_shift = (self.height - desired_height) // 2

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", self.x_shift, self.y_shift - self.origHeight, wscale, hscale)