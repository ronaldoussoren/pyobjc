from Quartz import *
import math

def doEgg(context):
    p0 = CGPoint(0, 0)
    p1 = CGPoint(0, 200)
    c1 = CGPoint(140, 5) 
    c2 = CGPoint(80, 198)

    CGContextTranslateCTM(context, 100, 5)
    CGContextBeginPath(context)
    
    CGContextMoveToPoint(context, p0.x, p0.y)
    # Create the Bezier path segment for the right side of the egg.
    CGContextAddCurveToPoint(context, c1.x, c1.y, c2.x, c2.y, p1.x, p1.y)
    # Create the Bezier path segment for the left side of the egg.
    CGContextAddCurveToPoint(context, -c2.x, c2.y, -c1.x, c1.y, p0.x, p0.y)
    CGContextClosePath(context)
    CGContextSetLineWidth(context, 2)
    CGContextDrawPath(context, kCGPathStroke)

def addRoundedRectToPath(context, rect, ovalWidth, ovalHeight):
    # If either ovalWidth or ovalHeight is 0, draw a regular rectangle.
    if ovalWidth == 0 or ovalHeight == 0:
        CGContextAddRect(context, rect)
    else:
        CGContextSaveGState(context)
        if 1:
            # Translate to lower-left corner of rectangle.
            CGContextTranslateCTM(context, 
                    CGRectGetMinX(rect), CGRectGetMinY(rect))
            # Scale by the oval width and height so that
            # each rounded corner is 0.5 units in radius.
            CGContextScaleCTM(context, ovalWidth, ovalHeight)
            # Unscale the rectangle width by the amount of the X scaling.
            fw = CGRectGetWidth(rect) / ovalWidth
            # Unscale the rectangle height by the amount of the Y scaling.
            fh = CGRectGetHeight(rect) / ovalHeight
            # Start at the right edge of the rect, at the midpoint in Y.
            CGContextMoveToPoint(context, fw, fh/2)
            # Segment 1
            CGContextAddArcToPoint(context, fw, fh, fw/2, fh, 0.5)
            # Segment 2
            CGContextAddArcToPoint(context, 0, fh, 0, fh/2, 0.5)
            # Segment 3
            CGContextAddArcToPoint(context, 0, 0, fw/2, 0, 0.5)
            # Segment 4
            CGContextAddArcToPoint(context, fw, 0, fw, fh/2, 0.5)
            # Closing the path adds the last segment.
            CGContextClosePath(context)
        CGContextRestoreGState(context)

def doRoundedRects(context):
    rect = CGRectMake(10, 10, 210, 150)
    ovalWidth = 100
    ovalHeight = 100
    CGContextSetLineWidth(context, 2.)
    CGContextBeginPath(context)
    addRoundedRectToPath(context, rect, ovalWidth, ovalHeight)
    CGContextSetRGBStrokeColor(context, 1, 0, 0, 1)
    CGContextDrawPath(context, kCGPathStroke)

def doStrokeWithCTM(context):
    CGContextTranslateCTM(context, 150., 180.)
    CGContextSetLineWidth(context, 10)
    # Draw ellipse 1 with a uniform stroke.
    CGContextSaveGState(context)
    if 1:
        # Scale the CTM so the circular arc will be elliptical.
        CGContextScaleCTM(context, 2, 1)
        CGContextBeginPath(context)
        # Create an arc that is a circle.
        CGContextAddArc(context, 0., 0., 45., 0., 2*math.pi, 0)
	# Restore the context parameters prior to stroking the path.
	# CGContextRestoreGState does not affect the path in the context.
    CGContextRestoreGState(context)
    CGContextStrokePath(context)
	
    # *** was 0, -120
    CGContextTranslateCTM(context, 220., 0.)
    # Draw ellipse 2 with non-uniform stroke.
    CGContextSaveGState(context)
    if 1:
        # Scale the CTM so the circular arc will be elliptical.
        CGContextScaleCTM(context, 2, 1)
        CGContextBeginPath(context)
        # Create an arc that is a circle.
        CGContextAddArc(context, 0., 0., 45., 0., 2*math.pi, 0)
        # Stroke the path with the scaled coordinate system in effect.
        CGContextStrokePath(context)
    CGContextRestoreGState(context)

def doRotatedEllipsesWithCGPath(context):
    totreps = 144
    tint = 1.0
    tintIncrement = 1.0/totreps

    # Create a new transform consisting of a 45 degree rotation.
    theTransform = CGAffineTransformMakeRotation(math.pi/4)
    # Apply a scaling transformation to the transform just created.
    theTransform = CGAffineTransformScale(theTransform, 1, 2)
    # Create a mutable CGPath object.
    path = CGPathCreateMutable()
    if path is None:
        print >>sys.stderr, "Couldn't create path!"
        return

    # Add a circular arc to the CGPath object, transformed
    # by an affine transform.
    CGPathAddArc(path, theTransform, 0., 0., 45., 0., 2*math.pi, False); 
    # Close the CGPath object.
    CGPathCloseSubpath(path)
	
    # Place the first ellipse at a good location.	
    CGContextTranslateCTM(context, 100, 100)
    for i in range(totreps):
        CGContextBeginPath(context)
        # Add the CGPath object to the current path in the context.
        CGContextAddPath(context, path)
		
        # Set the fill color for this instance of the ellipse.
        CGContextSetRGBFillColor(context, tint, 0., 0., 1.)
        # Filling the path implicitly closes it.
        CGContextFillPath(context)
        # Compute the next tint color.
        tint -= tintIncrement
        # Move over for the next ellipse.
        CGContextTranslateCTM(context, 1, 0.)

def alignPointToUserSpace(context, p):
    # Compute the coordinates of the point in device space.
    p = CGContextConvertPointToDeviceSpace(context, p)
    # Ensure that coordinates are at exactly the corner
    # of a device pixel.
    p.x = math.floor(p.x)
    p.y = math.floor(p.y)
    # Convert the device aligned coordinate back to user space.
    return CGContextConvertPointToUserSpace(context, p)

def alignSizeToUserSpace(context, s):
    # Compute the size in device space.
    s = CGContextConvertSizeToDeviceSpace(context, s)
    # Ensure that size is an integer multiple of device pixels.
    s.width = math.floor(s.width)
    s.height = math.floor(s.height)
    # Convert back to user space.
    return CGContextConvertSizeToUserSpace(context, s)

def alignRectToUserSpace(context, r):
    # Compute the coordinates of the rectangle in device space.
    r = CGContextConvertRectToDeviceSpace(context, r)
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
    return CGContextConvertRectToUserSpace(context, r)

def doPixelAlignedFillAndStroke(context):
    p1 = CGPointMake(16.7, 17.8)
    p2 = CGPointMake(116.7, 17.8)
    r = CGRectMake(16.7, 20.8, 100.6, 100.6)
    
    CGContextSetLineWidth(context, 2)
    CGContextSetRGBFillColor(context, 1., 0., 0., 1.)
    CGContextSetRGBStrokeColor(context, 1., 0., 0., 1.)
    
    # Unaligned drawing.
    CGContextBeginPath(context)
    CGContextMoveToPoint(context, p1.x, p1.y)
    CGContextAddLineToPoint(context, p2.x, p2.y)
    CGContextStrokePath(context)
    CGContextFillRect(context, r)
    
    # Translate to the right before drawing along
    # aligned coordinates.
    CGContextTranslateCTM(context, 106, 0)
    
    # Aligned drawing.
    
    # Compute the length of the line in user space.
    s = CGSizeMake(p2.x - p1.x, p2.y - p1.y)
    
    CGContextBeginPath(context)
    # Align the starting point to a device
    # pixel boundary.
    p1 = alignPointToUserSpace(context, p1)
    # Establish the starting point of the line.
    CGContextMoveToPoint(context, p1.x, p1.y)
    # Compute the line length as an integer
    # number of device pixels.
    s = alignSizeToUserSpace(context, s)
    CGContextAddLineToPoint(context, 
				p1.x + s.width, 
				p1.y + s.height)
    CGContextStrokePath(context)
    # Compute a rect that is aligned to device
    # space with a width that is an integer
    # number of device pixels.
    r = alignRectToUserSpace(context, r)
    CGContextFillRect(context, r)
