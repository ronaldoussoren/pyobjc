import Cocoa
import objc
import random

class NSColor (objc.Category(Cocoa.NSColor)):
    @classmethod
    def randomColor(self):
        return Cocoa.NSColor.colorWithCalibratedRed_green_blue_alpha_(
                random.uniform(0, 1),
                random.uniform(0, 1),
                random.uniform(0, 1),
                1)

def makeRandomPointInRect(rect):
    return Cocoa.NSPoint(
        x = random.uniform(Cocoa.NSMinX(rect), Cocoa.NSMaxX(rect)),
        y = random.uniform(Cocoa.NSMinY(rect), Cocoa.NSMaxY(rect)))
