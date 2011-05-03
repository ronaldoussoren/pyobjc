"""
Example showing screen saver in PyObjC

Based on "Silly Balls.saver" by Eric Peyton <epeyton@epicware.com>
    http://www.epicware.com/macosxsavers.html
"""
import objc

from AppKit import *
from ScreenSaver import *
from random import random, randrange

class SillyBalls (ScreenSaverView):

    def animateOneFrame(self):
        # choose a random point.
        (x, y), (fw, fh) = self.frame()
        x, y = randrange(0.0, fw), randrange(0.0, fw)
        ballSize = randrange(10.0, 90.0)

        path = NSBezierPath.bezierPathWithOvalInRect_(((x, y), (ballSize, ballSize)))

        # make a random color.
        randomColor = NSColor.colorWithCalibratedRed_green_blue_alpha_(random(), random(), random(), random())

        # set it.
        randomColor.set()

        # draw a new ball.
        path.fill()

objc.removeAutoreleasePool()
