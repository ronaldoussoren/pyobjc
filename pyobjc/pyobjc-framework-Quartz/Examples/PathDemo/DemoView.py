from Cocoa import *
from Quartz import *

import objc

from math import pi as PI
import random

class DemoView (NSView):
    _demoNumber = objc.ivar(objc._C_INT)


    def initWithFrame_(self, frameRect):
        self = super(DemoView, self).initWithFrame_(frameRect)
        if self is None:
            return None

        self._demoNumber = 0
        return self

    def drawRect_(self, rect):
        context = NSGraphicsContext.currentContext().graphicsPort()

        CGContextSetGrayFillColor(context, 1.0, 1.0)
        CGContextFillRect(context, rect)
   
        if self._demoNumber == 0:
	    rectangles(context, rect)
	
        elif self._demoNumber == 1:
            circles(context, rect)

        elif self._demoNumber == 2:
            bezierPaths(context, rect)

        elif self._demoNumber == 3:
            circleClipping(context, rect)

        else:
            NSLog("Invalid demo number.")

    def setDemoNumber_(self, number):
        self._demoNumber = number


# The various demo functions

def setRandomFillColor(context):
    CGContextSetRGBFillColor(context, 
           random.uniform(0, 1), random.uniform(0, 1),
           random.uniform(0, 1), random.uniform(0, 1))

def setRandomStrokeColor(context):
    CGContextSetRGBStrokeColor(context, 
           random.uniform(0, 1), random.uniform(0, 1),
           random.uniform(0, 1), random.uniform(0, 1))


def randomPointInRect(rect):
    return CGPoint(
        x = random.uniform(CGRectGetMinX(rect), CGRectGetMaxX(rect)),
        y = random.uniform(CGRectGetMinY(rect), CGRectGetMaxY(rect)))

def randomRectInRect(rect):
    p = randomPointInRect(rect)
    q = randomPointInRect(rect)
    return CGRectMake(p.x, p.y, q.x - p.x, q.y - p.y)

def rectangles(context, rect):
    # Draw random rectangles (some stroked, some filled).

    for k in range(20):
        if k % 2 == 0:
	    setRandomFillColor(context)
            CGContextFillRect(context, randomRectInRect(rect))

        else:
	    setRandomStrokeColor(context)
            CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            CGContextStrokeRect(context, randomRectInRect(rect))

def circles(context, rect):
    # Draw random circles (some stroked, some filled).

    for k in range(20):
	r = randomRectInRect(rect)
	w = CGRectGetWidth(r)
	h = CGRectGetHeight(r)
        CGContextBeginPath(context)

        if w < h:
            v = w
        else:
            v = h

        CGContextAddArc(context, 
                CGRectGetMidX(r), CGRectGetMidY(r),
                v, 0, 2*PI, False)
        CGContextClosePath(context)

        if k % 2 == 0:
	    setRandomFillColor(context)
            CGContextFillPath(context)

        else:
	    setRandomStrokeColor(context)
            CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            CGContextStrokePath(context)

def bezierPaths(context, rect):
    for k in range(20):
        numberOfSegments = 1 + random.randint(0, 8)
        CGContextBeginPath(context)
	p = randomPointInRect(rect)
        CGContextMoveToPoint(context, p.x, p.y)
        for j in range(numberOfSegments):
	    p = randomPointInRect(rect);

            if j % 2 == 0:
                CGContextAddLineToPoint(context, p.x, p.y)

            else:
		c1 = randomPointInRect(rect)
		c2 = randomPointInRect(rect)
                CGContextAddCurveToPoint(context, c1.x, c1.y,
					 c2.x, c2.y, p.x, p.y)

        if k % 2 == 0:
	    setRandomFillColor(context)
	    CGContextClosePath(context)
            CGContextFillPath(context)

        else:
	    setRandomStrokeColor(context)
            CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            CGContextStrokePath(context)


def circleClipping(context, rect):
    # Draw a random path through a circular clip.

    w = CGRectGetWidth(rect)
    h = CGRectGetHeight(rect)
    CGContextBeginPath(context)
    if w < h:
        v = w
    else:
        v = h
    CGContextAddArc(context, CGRectGetMidX(rect), CGRectGetMidY(rect),
		    v/2, 0, 2*PI, False)
    CGContextClosePath(context)
    CGContextClip(context)
    
    # Draw something into the clip.
    bezierPaths(context, rect)
    
    # Draw a clip path on top as a black stroked circle.
    CGContextBeginPath(context)
    CGContextAddArc(context, CGRectGetMidX(rect), CGRectGetMidY(rect),
		    v/2, 0, 2*PI, False)
    CGContextClosePath(context)
    CGContextSetLineWidth(context, 1)
    CGContextSetRGBStrokeColor(context, 0, 0, 0, 1)
    CGContextStrokePath(context)
