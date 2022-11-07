# File: DrawTrain.js

"""
This program starts the process of drawing a three-car train consisting
of an engine, a boxcar, and a caboose.  Only the boxcar is implemented
here.  The engine and the caboose are left to the reader as an exercise.
"""

from pgl import GWindow, GCompound, GLine, GRect, GOval
from gtools import create_filled_circle

# Constants

GWINDOW_WIDTH = 500           # Width of the graphics window
GWINDOW_HEIGHT = 300          # Height of the graphics window
CAR_WIDTH = 113               # Width of the frame of a train car
CAR_HEIGHT = 54               # Height of the frame of a train car
CAR_BASELINE = 15             # Distance of car base to the track
CONNECTOR = 6                 # Width of the connector on each car
WHEEL_RADIUS = 12             # Radius of the wheels on each car
WHEEL_INSET = 24              # Distance from frame to wheel center
CAB_WIDTH = 53                # Width of the cab on the engine
CAB_HEIGHT = 12               # Height of the cab on the engine
SMOKESTACK_WIDTH = 12         # Width of the smokestack
SMOKESTACK_HEIGHT = 12        # Height of the smokestack
SMOKESTACK_INSET = 12         # Distance from smokestack to front
DOOR_WIDTH = 27               # Width of the door on the boxcar
DOOR_HEIGHT = 48              # Height of the door on the boxcar
CUPOLA_WIDTH = 53             # Width of the cupola on the caboose
CUPOLA_HEIGHT = 12            # Height of the cupola on the caboose
TIME_STEP = 20                # Time step for the animation

# Main program

def draw_train():

    def click_action(e):
        timer = gw.set_interval(step, TIME_STEP)

    def step():
        train.move(-1, 0)

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    train = Train()
    train.append(Boxcar("Green"))
    x = (gw.get_width() - train.get_width()) / 2
    y = gw.get_height()
    gw.add(train, x, y)
    gw.add_event_listener("click", click_action)

class Train(GCompound):
    """This class represents an entire train"""

    def __init__(self):
        GCompound.__init__(self)

    def append(self, car):
        self.add(car, self.get_width(), 0)

class TrainCar(GCompound):
    """This class is the top of the hierarchy for all train cars"""

    def __init__(self, color):

        def add_wheel(x, y):
            self.add(create_filled_circle(x, y, r, fill="Gray", border="Black"))

        GCompound.__init__(self)
        r = WHEEL_RADIUS
        x = CONNECTOR
        y = -CAR_BASELINE
        self.add(GLine(0, y, CAR_WIDTH + 2 * CONNECTOR, y))
        add_wheel(x + WHEEL_INSET,  -r)
        add_wheel(x + CAR_WIDTH - WHEEL_INSET, -r)
        frame = GRect(x, y - CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
        frame.set_filled(True)
        frame.set_fill_color(color)
        self.add(frame)

class Boxcar(TrainCar):
    """This class displays a boxcar in a specified color"""

    def __init__(self, color):
        TrainCar.__init__(self, color)
        x = CONNECTOR + CAR_WIDTH / 2
        y = -(CAR_BASELINE + DOOR_HEIGHT)
        self.add(GRect(x - DOOR_WIDTH, y, DOOR_WIDTH, DOOR_HEIGHT))
        self.add(GRect(x, y, DOOR_WIDTH, DOOR_HEIGHT))

# Startup code

if __name__ == "__main__":
    draw_train()
