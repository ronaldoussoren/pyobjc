"""
Example for using CGShading and CGFunction. This code is directly translated
from procedural C code and is definitely not good Python style.
"""
from PyObjCTools import NibClassBuilder
from Quartz import *

import math
import random
import objc
import array

NibClassBuilder.extractClasses("MainMenu")

# Global variables
frequency = [ 0.0, 0.0, 0.0, 0.0 ]
startPoint = CGPoint(0.0, 0.0)
startRadius = 0.0
startExtend = False
endPoint = CGPoint(0.0, 0.0)
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
    return CGPoint(random.random(), random.random())



def evaluate1(components, input, output):
    out = []
    for k in range(components-1):
        out.append(1 + (math.sin(input[0] * frequency[k]))/2);
    out.append(1)
    return out

def getFunction1(colorspace):
    callbacks = ( evaluate1, None )
    domain = array.array('f', [ -2 * math.pi, 2 * math.pi ])
    range = array.array('f', [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ])
    components = 1 + CGColorSpaceGetNumberOfComponents(colorspace)

    return CGFunctionCreate(components, 1, domain, components,
                            range, callbacks)

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
    callbacks = ( evaluate2, None )
    domain = [0, 1]
    range = [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ]

    components = 1 + CGColorSpaceGetNumberOfComponents(colorspace);
    return CGFunctionCreate(components, 1, domain, components,
                            range, callbacks)

def evaluate3(components, input, output):
    c = [ 0.3, 0, 0, 0 ]

    out = []
    for k in range(components-1):
        out.append(c[k] * input[0])
    out.append(1)
    return out

def getFunction3(colorspace):
    callbacks = ( evaluate3, None )
    domain = [0, 1]
    range = [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ]

    components = 1 + CGColorSpaceGetNumberOfComponents(colorspace);
    return CGFunctionCreate(components, 1, domain, components,
                            range, callbacks);

def getAxialShading(colorspace, function):
    return CGShadingCreateAxial(colorspace, startPoint, endPoint,
                                function, startExtend, endExtend);

def getRadialShading(colorspace, function):
    return CGShadingCreateRadial(colorspace, startPoint, startRadius,
                                 endPoint, endRadius, function,
                                 startExtend, endExtend);


class MyQuartzView (NibClassBuilder.AutoBaseClass):
    def initWithFrame_(self, frameRect):
        global startPoint, startRadius, startExtend
        global endPoint, endRadius, endExtend

        super(MyQuartzView, self).initWithFrame_(frameRect)

        startPoint = CGPoint(0, 0)
        startRadius = 0;
        startExtend = False;

        endPoint = CGPointMake( 0, 0 );
        endRadius = 0;
        endExtend = False;

	return self;

    def drawRect_(self, rect):
        currentContext = NSGraphicsContext.currentContext().graphicsPort()

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

        m = CGAffineTransformIdentity;
        m = CGAffineTransformRotate(m, angle);
        m = CGAffineTransformScale(m, width, height);
        m = CGAffineTransformScale(m, sx, sy);

        CGContextBeginPage(currentContext, bounds)

        CGContextTranslateCTM(currentContext, 
                bounds.size.width/2, bounds.size.height/2);
        CGContextConcatCTM(currentContext, m);
        CGContextTranslateCTM(currentContext, -0.5, -0.5);

        CGContextSaveGState(currentContext);

        CGContextClipToRect(currentContext, CGRectMake(0, 0, 1, 1));
        CGContextSetRGBFillColor(currentContext, 0.7, 0.7, 0.9, 1);
        CGContextFillRect(currentContext, CGRectMake(0, 0, 1, 1));

        CGContextDrawShading(currentContext, shading);

        CGContextRestoreGState(currentContext);

        CGContextSaveGState(currentContext);
        CGContextClipToRect(currentContext, CGRectMake(0, 0, 1, 1));
        CGContextSetRGBStrokeColor(currentContext, 1, 0, 0, 1);

        if (getShading == getRadialShading):
            CGContextAddArc(currentContext, 
                    startPoint.x, startPoint.y, startRadius,
                    math.radians(0), math.radians(360), True)
            CGContextClosePath(currentContext)
            CGContextMoveToPoint(currentContext, endPoint.x + endRadius, endPoint.y)
            CGContextAddArc(currentContext, endPoint.x, endPoint.y, endRadius,
                        math.radians(0), math.radians(360), True)
            CGContextClosePath(currentContext)

        CGContextMoveToPoint(currentContext, startPoint.x + 0.01, startPoint.y)
        CGContextAddArc(currentContext, startPoint.x, startPoint.y, 0.01,
                    math.radians(0), math.radians(360), True)
        CGContextClosePath(currentContext)
        CGContextMoveToPoint(currentContext, startPoint.x, startPoint.y)
        CGContextAddLineToPoint(currentContext, endPoint.x, endPoint.y)

        ctm = CGContextGetCTM(currentContext)
        CGContextConcatCTM(currentContext, CGAffineTransformInvert(ctm))
        CGContextStrokePath(currentContext)
        CGContextRestoreGState(currentContext)

        CGContextSaveGState(currentContext)
        CGContextSetGrayStrokeColor(currentContext, 0, 1)
        CGContextAddRect(currentContext, CGRectMake(0, 0, 1, 1))
        ctm = CGContextGetCTM(currentContext)
        CGContextConcatCTM(currentContext, CGAffineTransformInvert(ctm))
        CGContextStrokePath(currentContext)
        CGContextRestoreGState(currentContext)

        CGContextEndPage(currentContext)

        CGContextFlush(currentContext);   

    def randomize_(self, sender):
        global colorspace, getFunction, getShading
        global function, shading
        global startPoint, startRadius, endPoint, endRadius

        if colorspace is None:
            colorspace = CGColorSpaceCreateDeviceRGB()

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

    def toggleStartExtend_(self, sender):
        global startExtend, shading
        
        startExtend = not startExtend
        shading = getShading(colorspace, function)

        self.setNeedsDisplay_(True)

    def toggleEndExtend_(self, sender):
        global endExtend, shading
        
        endExtend = not endExtend
        shading = getShading(colorspace, function)

        self.setNeedsDisplay_(True)
