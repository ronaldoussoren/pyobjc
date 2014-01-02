import Cocoa
import Quartz

import objc
import math

class Circle (Cocoa.NSObject):
    radius = objc.ivar(type=objc._C_FLT)
    center = objc.ivar(type=Cocoa.NSPoint.__typestr__)
    color = objc.ivar()

    def bounds(self):
        return Cocoa.NSMakeRect(
                self.center.x - self.radius,
                self.center.y - self.radius,
                2 * self.radius, 2 * self.radius)

    def draw(self):
        context = Cocoa.NSGraphicsContext.currentContext().graphicsPort()

        self.color.set()
        Cocoa.CGContextSetGrayStrokeColor(context, 0, 1)
        Cocoa.CGContextSetLineWidth(context, 1.5)

        Cocoa.CGContextSaveGState(context)

        Cocoa.CGContextTranslateCTM(context, self.center.x, self.center.y)
        Cocoa.CGContextScaleCTM(context, self.radius, self.radius)
        Cocoa.CGContextMoveToPoint(context, 1, 0)
        Cocoa.CGContextAddArc(context, 0, 0, 1, 0, 2 * math.pi, False)
        Cocoa.CGContextClosePath(context)

        Cocoa.CGContextRestoreGState(context)
        Cocoa.CGContextDrawPath(context, Cocoa.kCGPathFill)
