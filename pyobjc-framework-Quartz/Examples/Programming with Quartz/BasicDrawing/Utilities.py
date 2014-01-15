
import math

import Quartz
import Cocoa

class ExportInfo (object):
    command = None
    fileType = None
    useQTForExport = False
    dpi = 1

def DEGREES_TO_RADIANS(degrees):
    return degrees * math.pi / 180


gScalingFactor = 1.0

# These routines are used for getting the correct results when
# drawing shadows and patterns with Quartz and exporting the
# results as bits. This is a hack; in principle the scaling
# factor should be passed to the draw proc.
def setScalingFactor(scalingFactor):
    if scalingFactor > 0:
        gScalingFactor = scalingFactor

def getScalingFactor():
    return gScalingFactor

_appBundle = None
def getAppBundle():
    global _appBundle

    if _appBundle is None:
        _appBundle = Cocoa.CFBundleGetMainBundle()

    return _appBundle


#
#    This version of getTheRGBColorSpace returns
#    the DeviceRGB color space.
#
_deviceRGB = None
def getTheRGBColorSpace():
    global _deviceRGB

    # Set once, the first time this function is called.
    if _deviceRGB is None:
        _deviceRGB = Quartz.CGColorSpaceCreateDeviceRGB()

    return _deviceRGB


_genericRGBColorSpace = None
def getTheCalibratedRGBColorSpace():
    global _genericRGBColorSpace

    if _genericRGBColorSpace is None:
        _genericRGBColorSpace = Quartz.CGColorSpaceCreateWithName(
                Quartz.kCGColorSpaceGenericRGB)

    return _genericRGBColorSpace

_genericGrayColorSpace = None
def getTheCalibratedGrayColorSpace():
    global _genericGrayColorSpace

    if _genericGrayColorSpace is None:
        _genericGrayColorSpace = Quartz.CGColorSpaceCreateWithName(
                Quartz.kCGColorSpaceGenericGray)
    return _genericGrayColorSpace


_genericSRGBColorSpace = None
def getTheSRGBColorSpace():
    # This only works on 10.5 or later
    global _genericSRGBColorSpace

    if _genericSRGBColorSpace is None:
        _genericSRGBColorSpace = Quartz.CGColorSpaceCreateWithName(
                Quartz.kCGColorSpaceGenericRGB) # XXX: should be GenericSRGB
    return _genericSRGBColorSpace

def getTheDisplayColorSpace():
    # This is a hack, basicly here because the C implementation uses APIs that
    # aren't wrapped yet.
    return getTheRGBColorSpace()


_rgbWhite = None
def getRGBOpaqueWhiteColor():
    global _rgbWhite

    if _rgbWhite is None:
        opaqueWhite = (1.0, 1.0, 1.0, 1.0)
        _rgbWhite = Quartz.CGColorCreate(getTheCalibratedRGBColorSpace(), opaqueWhite)
    return _rgbWhite

_rgbBlack = None
def getRGBOpaqueBlackColor():
    global _rgbBlack
    if _rgbBlack is None:
        opaqueBlack = (0, 0, 0, 1)
        _rgbBlack = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueBlack)
    return _rgbBlack

_rgbGray = None
def getRGBOpaqueGrayColor():
    global _rgbGray
    if _rgbGray is None:
        opaqueGray = (0.9, 0.9, 0.9, 1)
        _rgbGray = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueGray)
    return _rgbGray

_rgbRed = None
def getRGBOpaqueRedColor():
    global _rgbRed
    if _rgbRed is None:
        opaqueRed = (0.663, 0, 0.031, 1)
        _rgbRed = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueRed)
    return _rgbRed

_rgbBlue = None
def getRGBOpaqueBlueColor():
    global _rgbBlue
    if _rgbBlue is None:
        opaqueBlue = (0.482, 0.62, 0.871, 1)
        _rgbBlue = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueBlue)
    return _rgbBlue

_rgbPurple = None
def getRGBOpaquePurpleColor():
    global _rgbPurple
    if _rgbPurple is None:
        opaquePurple = (0.69, 0.486, 0.722, 1)
        _rgbPurple = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaquePurple)
    return _rgbPurple

_rgbDarkBlue = None
def getRGBOpaqueDarkBlueColor():
    global _rgbDarkBlue
    if _rgbDarkBlue is None:
        opaqueDarkBlue = (0.11, 0.208, 0.451, 1)
        _rgbDarkBlue = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueDarkBlue)
    return _rgbDarkBlue

_rgbBrown = None
def getRGBOpaqueBrownColor():
    global _rgbBrown
    if _rgbBrown is None:
        opaqueBrown = (0.325, 0.208, 0.157, 1)
        _rgbBrown = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueBrown)
    return _rgbBrown

_rgbOrange = None
def getRGBOpaqueOrangeColor():
    global _rgbOrange
    if _rgbOrange is None:
        opaqueOrange = (0.965, 0.584, 0.059, 1)
        _rgbOrange = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueOrange)
    return _rgbOrange

_rgbYellow = None
def getRGBOpaqueYellowColor():
    global _rgbYellow
    if _rgbYellow is None:
        opaqueYellow = (1, 0.816, 0, 1)
        _rgbYellow = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueYellow)
    return _rgbYellow

_rgbGreen = None
def getRGBOpaqueGreenColor():
    global _rgbGreen
    if _rgbGreen is None:
        opaqueGreen = (0.584, 0.871, 0.318, 1)
        _rgbGreen = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueGreen)
    return _rgbGreen

_rgbDarkGreen = None
def getRGBOpaqueDarkGreenColor():
    global _rgbDarkGreen
    if _rgbDarkGreen is None:
        opaqueDarkGreen = (0.404, 0.808, 0.239, 1)
        _rgbDarkGreen = Quartz.CGColorCreate(
                getTheCalibratedRGBColorSpace(), opaqueDarkGreen)
    return _rgbDarkGreen

def myCGContextAddEllipseInRect(context, r):
    if hasattr(Quartz, 'CGContextAddEllipseInRect'):
        Quartz.CGContextAddEllipseInRect(context, r)

    else:
        # This is not a perfect emulation but is correct as long as there is
        # not an open subpath already in the current path. In that case the
        # CGContextClosePath here would not necessarily produce the desired
        # result.
        Quartz.CGContextSaveGState(context)
        if 1:
        # Translate to the center of the ellipse.
            Quartz.CGContextTranslateCTM(context,
                            Quartz.CGRectGetMidX(r),
                            Quartz.CGRectGetMidY(r))
            # Scale by half the width and height of the rectangle
            # bounding the ellipse.
            Quartz.CGContextScaleCTM(context, r.size.width/2, r.size.height/2)
            # Establish a current point at the first point
            # on the ellipse. This ensures that there
            # is no line segment connecting the previous
            # current point to the first point on the subpath.
            Quartz.CGContextMoveToPoint(context, 1, 0)
            # Circular arc around the ellipse center with
            # a radius that, when scaled by the CTM, produces
            # the major and minor axes of the ellipse. Since
            # CGContextAddEllipseInRect defines the direction
            # of the path as clockwise, this routine will
            # draw the arc clockwise also.
            Quartz.CGContextAddArc(context, 0, 0, 1, 0, 2*math.pi, 1)
            Quartz.CGContextClosePath(context)
        Quartz.CGContextRestoreGState(context)

# Routines that are useful for debugging.

def drawPoint(context, p):
    Quartz.CGContextSaveGState(context)
    if 1:
        # Opaque black.
        Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 0, 1)
        Quartz.CGContextSetLineWidth(context, 5)
        Quartz.CGContextSetLineCap(context, Quartz.kCGLineCapRound)
        Quartz.CGContextMoveToPoint(context, p.x, p.y)
        Quartz.CGContextAddLineToPoint(context, p.x, p.y)
        Quartz.CGContextStrokePath(context)
    Quartz.CGContextRestoreGState(context)


def printCTM(context):
    t = Quartz.CGContextGetCTM(context)
    print("CurrentCTM is %r"%(t,))

kTickLength = 5
kTickDistance = 72
kAxesLength = (20*kTickDistance)

def drawCoordinateAxes(context):
    tickLength = kTickLength

    Quartz.CGContextSaveGState(context)
    if 1:
        Quartz.CGContextBeginPath(context)
        # Paint the x-axis in red.
        Quartz.CGContextSetRGBStrokeColor(context, 1, 0, 0, 1)
        Quartz.CGContextMoveToPoint(context, -kTickLength, 0.)
        Quartz.CGContextAddLineToPoint(context, kAxesLength, 0.)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

        # Paint the y-axis in blue.
        Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 1, 1)
        Quartz.CGContextMoveToPoint(context, 0, -kTickLength)
        Quartz.CGContextAddLineToPoint(context, 0, kAxesLength)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

        # Paint the x-axis tick marks in red.
        Quartz.CGContextSetRGBStrokeColor(context, 1, 0, 0, 1)
        for i in range(2):
            for t in range(0, kAxesLength, kTickDistance):
                Quartz.CGContextMoveToPoint(context, t, -tickLength)
                Quartz.CGContextAddLineToPoint(context, t, tickLength)

            Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)
            Quartz.CGContextRotateCTM(context, math.pi/2.)
            # Paint the y-axis tick marks in blue.
            Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 1, 1)

        drawPoint(context, Quartz.CGPointZero)
    Quartz.CGContextRestoreGState(context)

def drawDebuggingRect(context, rect):
    Quartz.CGContextSaveGState(context)
    if 1:
        Quartz.CGContextSetLineWidth(context, 4.)
        # Draw opaque red from top-left to bottom-right.
        Quartz.CGContextSetRGBStrokeColor(context, 1, 0, 0, 1.0)
        Quartz.CGContextMoveToPoint(context, rect.origin.x,
                                        rect.origin.y + rect.size.height)
        Quartz.CGContextAddLineToPoint(context,
                                        rect.origin.x + rect.size.width,
                                        rect.origin.y)
        Quartz.CGContextStrokePath(context)
        # Draw opaque blue from top-right to bottom-left.
        Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 1, 1.0)
        Quartz.CGContextMoveToPoint(context, rect.origin.x + rect.size.width,
                                        rect.origin.y + rect.size.height)
        Quartz.CGContextAddLineToPoint(context, rect.origin.x, rect.origin.y)
        Quartz.CGContextStrokePath(context)
        # Opaque black.
        Quartz.CGContextSetRGBStrokeColor(context, 0, 0, 0, 1.)
        Quartz.CGContextStrokeRect(context, rect)
    Quartz.CGContextRestoreGState(context)
