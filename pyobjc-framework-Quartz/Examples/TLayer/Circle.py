from Cocoa import *
from Quartz import *

import objc
import math

class Circle (NSObject):
    radius = objc.ivar(objc._C_FLT)
    center = objc.ivar(NSPoint.__typestr__)
    color = objc.ivar()

    def bounds(self):
        return NSMakeRect(
                self.center.x - self.radius,
                self.center.y - self.radius,
                2 * self.radius, 2 * self.radius)

    def draw(self):
        context = NSGraphicsContext.currentContext().graphicsPort()

        self.color.set()
        CGContextSetGrayStrokeColor(context, 0, 1)
        CGContextSetLineWidth(context, 1.5)

        CGContextSaveGState(context)

        CGContextTranslateCTM(context, self.center.x, self.center.y)
        CGContextScaleCTM(context, self.radius, self.radius)
        CGContextMoveToPoint(context, 1, 0)
        CGContextAddArc(context, 0, 0, 1, 0, 2 * math.pi, False)
        CGContextClosePath(context)

        CGContextRestoreGState(context)
        CGContextDrawPath(context, kCGPathFill)
