import Cocoa
import Quartz

import math


def doAlphaRects(context):
    # ***** Part 1 *****
    ourRect = Quartz.CGRectMake(0.0, 0.0, 130.0, 100.0)
    numRects = 6
    rotateAngle = 2 * math.pi / numRects
    tintAdjust = 1./numRects

    # ***** Part 2 *****
    Quartz.CGContextTranslateCTM(context, 2*ourRect.size.width,
                                    2*ourRect.size.height)

    # ***** Part 3 *****
    tint = 1.0
    for i in range(numRects):
        Quartz.CGContextSetRGBFillColor(context, tint, 0.0, 0.0, tint)
        Quartz.CGContextFillRect(context, ourRect)
        Quartz.CGContextRotateCTM(context, rotateAngle)  # cumulative
        tint -= tintAdjust

class MyView (Cocoa.NSView):
    def drawRect_(self, rect):
        nsctx = Cocoa.NSGraphicsContext.currentContext()
        context = nsctx.graphicsPort()

        Quartz.CGContextSetLineWidth(context, 5.0)
        # Draw the coordinate axes.
        Quartz.CGContextBeginPath(context)
        # First draw the x axis.
        Quartz.CGContextMoveToPoint(context, -2000., 0.0)
        Quartz.CGContextAddLineToPoint(context, 2000., 0.0)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)
        # Next draw the y axis.
        Quartz.CGContextMoveToPoint(context, 0.0, -2000.0)
        Quartz.CGContextAddLineToPoint(context, 0.0, 2000.0)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

        doAlphaRects(context)
