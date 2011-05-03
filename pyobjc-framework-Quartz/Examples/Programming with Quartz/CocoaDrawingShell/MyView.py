from Cocoa import *
from Quartz import *

import math


def doAlphaRects(context):
    # ***** Part 1 *****
    ourRect = CGRectMake(0.0, 0.0, 130.0, 100.0)
    numRects = 6
    rotateAngle = 2 * math.pi / numRects
    tintAdjust = 1./numRects
    
    # ***** Part 2 *****
    CGContextTranslateCTM(context, 2*ourRect.size.width, 
                                    2*ourRect.size.height)
    
    # ***** Part 3 *****
    tint = 1.0
    for i in range(numRects):
        CGContextSetRGBFillColor(context, tint, 0.0, 0.0, tint)
        CGContextFillRect(context, ourRect)
        CGContextRotateCTM(context, rotateAngle)  # cumulative
        tint -= tintAdjust

class MyView (NSView):
    def drawRect_(self, rect):
        nsctx = NSGraphicsContext.currentContext()
        context = nsctx.graphicsPort()

	CGContextSetLineWidth(context, 5.0)
	# Draw the coordinate axes.
	CGContextBeginPath(context)
	# First draw the x axis.
	CGContextMoveToPoint(context, -2000., 0.0)
	CGContextAddLineToPoint(context, 2000., 0.0)
	CGContextDrawPath(context, kCGPathStroke)
	# Next draw the y axis.
	CGContextMoveToPoint(context, 0.0, -2000.0)
	CGContextAddLineToPoint(context, 0.0, 2000.0)
	CGContextDrawPath(context, kCGPathStroke)
	
	doAlphaRects(context)
