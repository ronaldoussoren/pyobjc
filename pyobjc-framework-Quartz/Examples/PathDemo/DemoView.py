import objc
from objc import super
import Cocoa
import Quartz


from math import pi as PI
import random

class DemoView (Cocoa.NSView):
    _demoNumber = objc.ivar(type=objc._C_INT)


    def initWithFrame_(self, frameRect):
        self = super(DemoView, self).initWithFrame_(frameRect)
        if self is None:
            return None

        self._demoNumber = 0
        return self

    def drawRect_(self, rect):
        context = Cocoa.NSGraphicsContext.currentContext().graphicsPort()

        Quartz.CGContextSetGrayFillColor(context, 1.0, 1.0)
        Quartz.CGContextFillRect(context, rect)

        if self._demoNumber == 0:
            rectangles(context, rect)

        elif self._demoNumber == 1:
            circles(context, rect)

        elif self._demoNumber == 2:
            bezierPaths(context, rect)

        elif self._demoNumber == 3:
            circleClipping(context, rect)

        else:
            Cocoa.NSLog("Invalid demo number.")

    def setDemoNumber_(self, number):
        self._demoNumber = number


# The various demo functions

def setRandomFillColor(context):
    Quartz.CGContextSetRGBFillColor(context,
           random.uniform(0, 1), random.uniform(0, 1),
           random.uniform(0, 1), random.uniform(0, 1))

def setRandomStrokeColor(context):
    Quartz.CGContextSetRGBStrokeColor(context,
           random.uniform(0, 1), random.uniform(0, 1),
           random.uniform(0, 1), random.uniform(0, 1))


def randomPointInRect(rect):
    return Quartz.CGPoint(
        x = random.uniform(Quartz.CGRectGetMinX(rect), Quartz.CGRectGetMaxX(rect)),
        y = random.uniform(Quartz.CGRectGetMinY(rect), Quartz.CGRectGetMaxY(rect)))

def randomRectInRect(rect):
    p = randomPointInRect(rect)
    q = randomPointInRect(rect)
    return Quartz.CGRectMake(p.x, p.y, q.x - p.x, q.y - p.y)

def rectangles(context, rect):
    # Draw random rectangles (some stroked, some filled).

    for k in range(20):
        if k % 2 == 0:
            setRandomFillColor(context)
            Quartz.CGContextFillRect(context, randomRectInRect(rect))

        else:
            setRandomStrokeColor(context)
            Quartz.CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            Quartz.CGContextStrokeRect(context, randomRectInRect(rect))

def circles(context, rect):
    # Draw random circles (some stroked, some filled).

    for k in range(20):
        r = randomRectInRect(rect)
        w = Quartz.CGRectGetWidth(r)
        h = Quartz.CGRectGetHeight(r)
        Quartz.CGContextBeginPath(context)

        if w < h:
            v = w
        else:
            v = h

        Quartz.CGContextAddArc(context,
                Quartz.CGRectGetMidX(r), Quartz.CGRectGetMidY(r),
                v, 0, 2*PI, False)
        Quartz.CGContextClosePath(context)

        if k % 2 == 0:
            setRandomFillColor(context)
            Quartz.CGContextFillPath(context)

        else:
            setRandomStrokeColor(context)
            Quartz.CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            Quartz.CGContextStrokePath(context)

def bezierPaths(context, rect):
    for k in range(20):
        numberOfSegments = 1 + random.randint(0, 8)
        Quartz.CGContextBeginPath(context)
        p = randomPointInRect(rect)
        Quartz.CGContextMoveToPoint(context, p.x, p.y)
        for j in range(numberOfSegments):
            p = randomPointInRect(rect);

            if j % 2 == 0:
                Quartz.CGContextAddLineToPoint(context, p.x, p.y)

            else:
                c1 = randomPointInRect(rect)
                c2 = randomPointInRect(rect)
                Quartz.CGContextAddCurveToPoint(context, c1.x, c1.y,
                                         c2.x, c2.y, p.x, p.y)

        if k % 2 == 0:
            setRandomFillColor(context)
            Quartz.CGContextClosePath(context)
            Quartz.CGContextFillPath(context)

        else:
            setRandomStrokeColor(context)
            Quartz.CGContextSetLineWidth(context, 2 + random.randint(0, 10))
            Quartz.CGContextStrokePath(context)


def circleClipping(context, rect):
    # Draw a random path through a circular clip.

    w = Quartz.CGRectGetWidth(rect)
    h = Quartz.CGRectGetHeight(rect)
    Quartz.CGContextBeginPath(context)
    if w < h:
        v = w
    else:
        v = h
    Quartz.CGContextAddArc(context, Quartz.CGRectGetMidX(rect), Quartz.CGRectGetMidY(rect),
                    v/2, 0, 2*PI, False)
    Quartz.CGContextClosePath(context)
    Quartz.CGContextClip(context)

    # Draw something into the clip.
    bezierPaths(context, rect)

    # Draw a clip path on top as a black stroked circle.
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextAddArc(context, Quartz.CGRectGetMidX(rect), Quartz.CGRectGetMidY(rect),
                    v/2, 0, 2*PI, False)
    Quartz.CGContextClosePath(context)
    Quartz.CGContextSetLineWidth(context, 1)
    Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 0, 1)
    Quartz.CGContextStrokePath(context)
