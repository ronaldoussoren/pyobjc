import Quartz
import math

def doEgg(context):
    p0 = Quartz.CGPoint(0, 0)
    p1 = Quartz.CGPoint(0, 200)
    c1 = Quartz.CGPoint(140, 5)
    c2 = Quartz.CGPoint(80, 198)

    Quartz.CGContextTranslateCTM(context, 100, 5)
    Quartz.CGContextBeginPath(context)

    Quartz.CGContextMoveToPoint(context, p0.x, p0.y)
    # Create the Bezier path segment for the right side of the egg.
    Quartz.CGContextAddCurveToPoint(context, c1.x, c1.y, c2.x, c2.y, p1.x, p1.y)
    # Create the Bezier path segment for the left side of the egg.
    Quartz.CGContextAddCurveToPoint(context, -c2.x, c2.y, -c1.x, c1.y, p0.x, p0.y)
    Quartz.CGContextClosePath(context)
    Quartz.CGContextSetLineWidth(context, 2)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

def addRoundedRectToPath(context, rect, ovalWidth, ovalHeight):
    # If either ovalWidth or ovalHeight is 0, draw a regular rectangle.
    if ovalWidth == 0 or ovalHeight == 0:
        Quartz.CGContextAddRect(context, rect)
    else:
        Quartz.CGContextSaveGState(context)
        if 1:
            # Translate to lower-left corner of rectangle.
            Quartz.CGContextTranslateCTM(context,
                    Quartz.CGRectGetMinX(rect), Quartz.CGRectGetMinY(rect))
            # Scale by the oval width and height so that
            # each rounded corner is 0.5 units in radius.
            Quartz.CGContextScaleCTM(context, ovalWidth, ovalHeight)
            # Unscale the rectangle width by the amount of the X scaling.
            fw = Quartz.CGRectGetWidth(rect) / ovalWidth
            # Unscale the rectangle height by the amount of the Y scaling.
            fh = Quartz.CGRectGetHeight(rect) / ovalHeight
            # Start at the right edge of the rect, at the midpoint in Y.
            Quartz.CGContextMoveToPoint(context, fw, fh/2)
            # Segment 1
            Quartz.CGContextAddArcToPoint(context, fw, fh, fw/2, fh, 0.5)
            # Segment 2
            Quartz.CGContextAddArcToPoint(context, 0, fh, 0, fh/2, 0.5)
            # Segment 3
            Quartz.CGContextAddArcToPoint(context, 0, 0, fw/2, 0, 0.5)
            # Segment 4
            Quartz.CGContextAddArcToPoint(context, fw, 0, fw, fh/2, 0.5)
            # Closing the path adds the last segment.
            Quartz.CGContextClosePath(context)
        Quartz.CGContextRestoreGState(context)

def doRoundedRects(context):
    rect = Quartz.CGRectMake(10, 10, 210, 150)
    ovalWidth = 100
    ovalHeight = 100
    Quartz.CGContextSetLineWidth(context, 2.)
    Quartz.CGContextBeginPath(context)
    addRoundedRectToPath(context, rect, ovalWidth, ovalHeight)
    Quartz.CGContextSetRGBStrokeColor(context, 1, 0, 0, 1)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

def doStrokeWithCTM(context):
    Quartz.CGContextTranslateCTM(context, 150., 180.)
    Quartz.CGContextSetLineWidth(context, 10)
    # Draw ellipse 1 with a uniform stroke.
    Quartz.CGContextSaveGState(context)
    if 1:
        # Scale the CTM so the circular arc will be elliptical.
        Quartz.CGContextScaleCTM(context, 2, 1)
        Quartz.CGContextBeginPath(context)
        # Create an arc that is a circle.
        Quartz.CGContextAddArc(context, 0., 0., 45., 0., 2*math.pi, 0)
        # Restore the context parameters prior to stroking the path.
        # CGContextRestoreGState does not affect the path in the context.
    Quartz.CGContextRestoreGState(context)
    Quartz.CGContextStrokePath(context)

    # *** was 0, -120
    Quartz.CGContextTranslateCTM(context, 220., 0.)
    # Draw ellipse 2 with non-uniform stroke.
    Quartz.CGContextSaveGState(context)
    if 1:
        # Scale the CTM so the circular arc will be elliptical.
        Quartz.CGContextScaleCTM(context, 2, 1)
        Quartz.CGContextBeginPath(context)
        # Create an arc that is a circle.
        Quartz.CGContextAddArc(context, 0., 0., 45., 0., 2*math.pi, 0)
        # Stroke the path with the scaled coordinate system in effect.
        Quartz.CGContextStrokePath(context)
    Quartz.CGContextRestoreGState(context)

def doRotatedEllipsesWithCGPath(context):
    totreps = 144
    tint = 1.0
    tintIncrement = 1.0/totreps

    # Create a new transform consisting of a 45 degree rotation.
    theTransform = Quartz.CGAffineTransformMakeRotation(math.pi/4)
    # Apply a scaling transformation to the transform just created.
    theTransform = Quartz.CGAffineTransformScale(theTransform, 1, 2)
    # Create a mutable CGPath object.
    path = Quartz.CGPathCreateMutable()
    if path is None:
        print("Couldn't create path!")
        return

    # Add a circular arc to the CGPath object, transformed
    # by an affine transform.
    Quartz.CGPathAddArc(path, theTransform, 0., 0., 45., 0., 2*math.pi, False);
    # Close the CGPath object.
    Quartz.CGPathCloseSubpath(path)

    # Place the first ellipse at a good location.
    Quartz.CGContextTranslateCTM(context, 100, 100)
    for i in range(totreps):
        Quartz.CGContextBeginPath(context)
        # Add the CGPath object to the current path in the context.
        Quartz.CGContextAddPath(context, path)

        # Set the fill color for this instance of the ellipse.
        Quartz.CGContextSetRGBFillColor(context, tint, 0., 0., 1.)
        # Filling the path implicitly closes it.
        Quartz.CGContextFillPath(context)
        # Compute the next tint color.
        tint -= tintIncrement
        # Move over for the next ellipse.
        Quartz.CGContextTranslateCTM(context, 1, 0.)

def alignPointToUserSpace(context, p):
    # Compute the coordinates of the point in device space.
    p = Quartz.CGContextConvertPointToDeviceSpace(context, p)
    # Ensure that coordinates are at exactly the corner
    # of a device pixel.
    p.x = math.floor(p.x)
    p.y = math.floor(p.y)
    # Convert the device aligned coordinate back to user space.
    return Quartz.CGContextConvertPointToUserSpace(context, p)

def alignSizeToUserSpace(context, s):
    # Compute the size in device space.
    s = Quartz.CGContextConvertSizeToDeviceSpace(context, s)
    # Ensure that size is an integer multiple of device pixels.
    s.width = math.floor(s.width)
    s.height = math.floor(s.height)
    # Convert back to user space.
    return Quartz.CGContextConvertSizeToUserSpace(context, s)

def alignRectToUserSpace(context, r):
    # Compute the coordinates of the rectangle in device space.
    r = Quartz.CGContextConvertRectToDeviceSpace(context, r)
    # Ensure that the x and y coordinates are at a pixel corner.
    r.origin.x = math.floor(r.origin.x)
    r.origin.y = math.floor(r.origin.y)
    # Ensure that the width and height are an integer number of
    # device pixels. Note that this produces a width and height
    # that is less than or equal to the original width. Another
    # approach is to use ceil to ensure that the new rectangle
    # encloses the original one.
    r.size.width = math.floor(r.size.width)
    r.size.height = math.floor(r.size.height)

    # Convert back to user space.
    return Quartz.CGContextConvertRectToUserSpace(context, r)

def doPixelAlignedFillAndStroke(context):
    p1 = Quartz.CGPointMake(16.7, 17.8)
    p2 = Quartz.CGPointMake(116.7, 17.8)
    r = Quartz.CGRectMake(16.7, 20.8, 100.6, 100.6)

    Quartz.CGContextSetLineWidth(context, 2)
    Quartz.CGContextSetRGBFillColor(context, 1., 0., 0., 1.)
    Quartz.CGContextSetRGBStrokeColor(context, 1., 0., 0., 1.)

    # Unaligned drawing.
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextMoveToPoint(context, p1.x, p1.y)
    Quartz.CGContextAddLineToPoint(context, p2.x, p2.y)
    Quartz.CGContextStrokePath(context)
    Quartz.CGContextFillRect(context, r)

    # Translate to the right before drawing along
    # aligned coordinates.
    Quartz.CGContextTranslateCTM(context, 106, 0)

    # Aligned drawing.

    # Compute the length of the line in user space.
    s = Quartz.CGSizeMake(p2.x - p1.x, p2.y - p1.y)

    Quartz.CGContextBeginPath(context)
    # Align the starting point to a device
    # pixel boundary.
    p1 = alignPointToUserSpace(context, p1)
    # Establish the starting point of the line.
    Quartz.CGContextMoveToPoint(context, p1.x, p1.y)
    # Compute the line length as an integer
    # number of device pixels.
    s = alignSizeToUserSpace(context, s)
    Quartz.CGContextAddLineToPoint(context,
                                p1.x + s.width,
                                p1.y + s.height)
    Quartz.CGContextStrokePath(context)
    # Compute a rect that is aligned to device
    # space with a width that is an integer
    # number of device pixels.
    r = alignRectToUserSpace(context, r)
    Quartz.CGContextFillRect(context, r)
