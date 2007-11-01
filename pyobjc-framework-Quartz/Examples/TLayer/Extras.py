from AppKit import *
import objc
import random

#import <AppKit/AppKit.h>
#import <unistd.h>

class NSColor (objc.Category(NSColor)):
    @classmethod
    def randomColor(self):
        return NSColor.colorWithCalibratedRed_green_blue_alpha_(
                random.uniform(0, 1),
                random.uniform(0, 1),
                random.uniform(0, 1),
                1)

def makeRandomPointInRect(rect):
    return NSPoint(
        x = random.uniform(NSMinX(rect), NSMaxX(rect)),
        y = random.uniform(NSMinY(rect), NSMaxY(rect)))
