import Quartz
import math
import Utilities

def doRotatedEllipses(context):
    totreps = 144
    tint = 1.0
    tintIncrement = 1.0/totreps
    # Create a new transform consisting of a 45 degrees rotation.
    theTransform = Quartz.CGAffineTransformMakeRotation(math.pi/4)
    # Apply a scale to the transform just created.
    theTransform = Quartz.CGAffineTransformScale(theTransform, 1, 2)
    # Place the first ellipse at a good location.
    Quartz.CGContextTranslateCTM(context, 100.0, 100.0)

    for i in range(totreps):
        # Make a snapshot the coordinate system.
        Quartz.CGContextSaveGState(context)
        # Set up the coordinate system for the rotated ellipse.
        Quartz.CGContextConcatCTM(context, theTransform)
        Quartz.CGContextBeginPath(context)
        Quartz.CGContextAddArc(context, 0.0, 0.0, 45.0, 0.0, 2*math.pi, 0);
        # Set the fill color for this instance of the ellipse.
        Quartz.CGContextSetRGBFillColor(context, tint, 0.0, 0.0, 1.0)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathFill)
        # Restore the coordinate system to that of the snapshot.
        Quartz.CGContextRestoreGState(context)
        # Compute the next tint color.
        tint -= tintIncrement
        # Move over by 1 unit in x for the next ellipse.
        Quartz.CGContextTranslateCTM(context, 1.0, 0.0)

def drawSkewedCoordinateSystem(context):
    # alpha is 22.5 degrees and beta is 15 degrees.
    alpha = math.pi/8
    beta = math.pi/12
    # Create a rectangle that is 72 units on a side
    # with its origin at (0,0).
    r = Quartz.CGRectMake(0, 0, 72, 72)

    Quartz.CGContextTranslateCTM(context, 144, 144)
    # Draw the coordinate axes untransformed.
    Utilities.drawCoordinateAxes(context)
    # Fill the rectangle.
    Quartz.CGContextFillRect(context, r)

    # Create an affine transform that skews the coordinate system,
    # skewing the x-axis by alpha radians and the y-axis by beta radians.
    skew = Quartz.CGAffineTransformMake(1, math.tan(alpha), math.tan(beta), 1, 0, 0)
    # Apply that transform to the context coordinate system.
    Quartz.CGContextConcatCTM(context, skew)

    # Set the fill and stroke color to a dark blue.
    Quartz.CGContextSetRGBStrokeColor(context, 0.11, 0.208, 0.451, 1)
    Quartz.CGContextSetRGBFillColor(context, 0.11, 0.208, 0.451, 1)

    # Draw the coordinate axes again, now transformed.
    Utilities.drawCoordinateAxes(context)
    # Set the fill color again but with a partially transparent alpha.
    Quartz.CGContextSetRGBFillColor(context, 0.11, 0.208, 0.451, 0.7)
    # Fill the rectangle in the transformed coordinate system.
    Quartz.CGContextFillRect(context, r)
