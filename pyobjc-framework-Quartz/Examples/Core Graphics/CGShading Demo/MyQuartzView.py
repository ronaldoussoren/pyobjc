"""
Example for using CGShading and CGFunction. This code is directly translated
from procedural C code and is definitely not good Python style.
"""
import objc
from objc import super
import Cocoa
import Quartz

import math
import sys
import random
import array

# Global variables
frequency = [ 0.0, 0.0, 0.0, 0.0 ]
startPoint = Quartz.CGPoint(0.0, 0.0)
startRadius = 0.0
startExtend = False
endPoint = Quartz.CGPoint(0.0, 0.0)
endRadius = 0.0
endExtend = False

shading = None
function = None
getFunction = None
getShading = None
colorspace = None

DEFAULT_WIDTH  = 256
DEFAULT_HEIGHT = 256

MAX_WIDTH  = 1000
MAX_HEIGHT = 1000


def randomPoint():
    return Quartz.CGPoint(random.random(), random.random())



def evaluate1(components, input, output):
    out = []
    for k in range(components-1):
        out.append(1 + (math.sin(input[0] * frequency[k]))/2);
    out.append(1)
    return out

def getFunction1(colorspace):
    if sys.maxsize > 2 ** 32:
        a_type = 'd'
    else:
        a_type = 'f'
    domain = array.array(a_type, [ -2 * math.pi, 2 * math.pi ])
    range = array.array(a_type, [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ])
    components = 1 + Quartz.CGColorSpaceGetNumberOfComponents(colorspace)

    return Quartz.CGFunctionCreate(components, 1, domain, components,
                            range, evaluate1)

def evaluate2(components, input, output):
    c = [ 0.510, 0.188, 0.910, 0.122 ]

    v = input[0]
    out = []
    for k in range(components-1):
        if v < 0.5:
            out.append(c[k] * 2 * (0.5 - v))
        else:
            out.append(c[k] * 2 * (v - 0.5))
    out.append(1)
    return out

def getFunction2(colorspace):
    domain = [0, 1]
    range = [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ]

    components = 1 + Quartz.CGColorSpaceGetNumberOfComponents(colorspace);
    return Quartz.CGFunctionCreate(components, 1, domain, components,
                            range, evaluate2)

def evaluate3(components, input, output):
    c = [ 0.3, 0, 0, 0 ]

    out = []
    for k in range(components-1):
        out.append(c[k] * input[0])
    out.append(1)
    return out

def getFunction3(colorspace):
    domain = [0, 1]
    range = [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ]

    components = 1 + Quartz.CGColorSpaceGetNumberOfComponents(colorspace);
    return Quartz.CGFunctionCreate(components, 1, domain, components,
                            range, evaluate3);

def getAxialShading(colorspace, function):
    return Quartz.CGShadingCreateAxial(colorspace, startPoint, endPoint,
                                function, startExtend, endExtend);

def getRadialShading(colorspace, function):
    return Quartz.CGShadingCreateRadial(colorspace, startPoint, startRadius,
                                 endPoint, endRadius, function,
                                 startExtend, endExtend);


class MyQuartzView (Cocoa.NSView):

    def initWithFrame_(self, frameRect):
        global startPoint, startRadius, startExtend
        global endPoint, endRadius, endExtend

        super(MyQuartzView, self).initWithFrame_(frameRect)

        startPoint = Quartz.CGPoint(0, 0)
        startRadius = 0;
        startExtend = False;

        endPoint = Quartz.CGPointMake( 0, 0 );
        endRadius = 0;
        endExtend = False;

        return self;

    def drawRect_(self, rect):
        currentContext = Cocoa.NSGraphicsContext.currentContext().graphicsPort()

        # Note that at this point the current context CTM is set up such
        # that the context size corresponds to the size of the view
        # i.e. one unit in the context == one pixel
        # Also, the origin is in the bottom left of the view with +y pointing up
        global getFunction

        bounds = self.bounds()

        angle = 0;
        sx = sy = 1;
        width = bounds.size.width;
        height = bounds.size.height;

        if getFunction is None:
            self.randomize_(self)

        m = Quartz.CGAffineTransformIdentity;
        m = Quartz.CGAffineTransformRotate(m, angle);
        m = Quartz.CGAffineTransformScale(m, width, height);
        m = Quartz.CGAffineTransformScale(m, sx, sy);

        Quartz.CGContextBeginPage(currentContext, bounds)

        Quartz.CGContextTranslateCTM(currentContext,
                bounds.size.width/2, bounds.size.height/2);
        Quartz.CGContextConcatCTM(currentContext, m);
        Quartz.CGContextTranslateCTM(currentContext, -0.5, -0.5);

        Quartz.CGContextSaveGState(currentContext);

        Quartz.CGContextClipToRect(currentContext, Quartz.CGRectMake(0, 0, 1, 1));
        Quartz.CGContextSetRGBFillColor(currentContext, 0.7, 0.7, 0.9, 1);
        Quartz.CGContextFillRect(currentContext, Quartz.CGRectMake(0, 0, 1, 1));

        Quartz.CGContextDrawShading(currentContext, shading);

        Quartz.CGContextRestoreGState(currentContext);

        Quartz.CGContextSaveGState(currentContext);
        Quartz.CGContextClipToRect(currentContext, Quartz.CGRectMake(0, 0, 1, 1));
        Quartz.CGContextSetRGBStrokeColor(currentContext, 1, 0, 0, 1);

        if (getShading == getRadialShading):
            Quartz.CGContextAddArc(currentContext,
                    startPoint.x, startPoint.y, startRadius,
                    math.radians(0), math.radians(360), True)
            Quartz.CGContextClosePath(currentContext)
            Quartz.CGContextMoveToPoint(currentContext, endPoint.x + endRadius, endPoint.y)
            Quartz.CGContextAddArc(currentContext, endPoint.x, endPoint.y, endRadius,
                        math.radians(0), math.radians(360), True)
            Quartz.CGContextClosePath(currentContext)

        Quartz.CGContextMoveToPoint(currentContext, startPoint.x + 0.01, startPoint.y)
        Quartz.CGContextAddArc(currentContext, startPoint.x, startPoint.y, 0.01,
                    math.radians(0), math.radians(360), True)
        Quartz.CGContextClosePath(currentContext)
        Quartz.CGContextMoveToPoint(currentContext, startPoint.x, startPoint.y)
        Quartz.CGContextAddLineToPoint(currentContext, endPoint.x, endPoint.y)

        ctm = Quartz.CGContextGetCTM(currentContext)
        Quartz.CGContextConcatCTM(currentContext, Quartz.CGAffineTransformInvert(ctm))
        Quartz.CGContextStrokePath(currentContext)
        Quartz.CGContextRestoreGState(currentContext)

        Quartz.CGContextSaveGState(currentContext)
        Quartz.CGContextSetGrayStrokeColor(currentContext, 0, 1)
        Quartz.CGContextAddRect(currentContext, Quartz.CGRectMake(0, 0, 1, 1))
        ctm = Quartz.CGContextGetCTM(currentContext)
        Quartz.CGContextConcatCTM(currentContext, Quartz.CGAffineTransformInvert(ctm))
        Quartz.CGContextStrokePath(currentContext)
        Quartz.CGContextRestoreGState(currentContext)

        Quartz.CGContextEndPage(currentContext)

        Quartz.CGContextFlush(currentContext);

    @objc.IBAction
    def randomize_(self, sender):
        global colorspace, getFunction, getShading
        global function, shading
        global startPoint, startRadius, endPoint, endRadius

        if colorspace is None:
            colorspace = Quartz.CGColorSpaceCreateDeviceRGB()

        for k in range(len(frequency)):
            frequency[k] = random.random()

        startPoint = randomPoint();
        startRadius = random.random() / 2;
        endPoint = randomPoint();
        endRadius = random.random() / 2;

        if getFunction == getFunction1:
            getFunction = getFunction2

        elif getFunction == getFunction2:
            getFunction = getFunction3

        else:
            getFunction = getFunction1

        if getShading == getAxialShading:
            getShading = getRadialShading
        else:
            getShading = getAxialShading

        function = getFunction(colorspace)
        shading = getShading(colorspace, function)

        self.setNeedsDisplay_(True)

    @objc.IBAction
    def toggleStartExtend_(self, sender):
        global startExtend, shading

        startExtend = not startExtend
        shading = getShading(colorspace, function)

        self.setNeedsDisplay_(True)

    @objc.IBAction
    def toggleEndExtend_(self, sender):
        global endExtend, shading

        endExtend = not endExtend
        shading = getShading(colorspace, function)

        self.setNeedsDisplay_(True)
