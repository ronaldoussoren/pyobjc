import math, sys

import Quartz


def doSimpleRect(context):
    # Set the fill color to opaque red.
    Quartz.CGContextSetRGBFillColor(context, 1.0, 0.0, 0.0, 1.0)
    # Set up the rectangle for drawing.
    ourRect = Quartz.CGRectMake(20.0, 20.0, 130.0, 100.0)
    # Draw the filled rectangle.
    Quartz.CGContextFillRect(context, ourRect)

def doStrokedRect(context):
    # Set the stroke color to a light opaque blue.
    Quartz.CGContextSetRGBStrokeColor(context, 0.482, 0.62, 0.871, 1.0)
    # Set up the rectangle for drawing.
    ourRect = Quartz.CGRectMake(20.0, 20.0, 130.0, 100.0)
    # Draw the stroked rectangle with a line width of 3.
    Quartz.CGContextStrokeRectWithWidth(context, ourRect, 3.0)

def doStrokedAndFilledRect(context):
    # Define a rectangle to use for drawing.
    ourRect = Quartz.CGRectMake(20.0, 220.0, 130.0, 100.0)

    # ***** Rectangle 1 *****
    # Set the fill color to a light opaque blue.
    Quartz.CGContextSetRGBFillColor(context, 0.482, 0.62, 0.871, 1.0)
    # Set the stroke color to an opaque green.
    Quartz.CGContextSetRGBStrokeColor(context, 0.404, 0.808, 0.239, 1.0)
    # Fill the rect.
    Quartz.CGContextFillRect(context, ourRect)
    # ***** Rectangle 2 *****
    # Move the rectangle's origin to the right by 200 units.
    ourRect.origin.x += 200.0
    # Stroke the rectangle with a line width of 10.
    Quartz.CGContextStrokeRectWithWidth(context, ourRect, 10.0)
    # ***** Rectangle 3 *****
    # Move the rectangle's origin to the left by 200 units
    # and down by 200 units.
    ourRect.origin.x -= 200.0
    ourRect.origin.y -= 200.0
    # Fill then stroke the rect with a line width of 10.
    Quartz.CGContextFillRect(context, ourRect)
    Quartz.CGContextStrokeRectWithWidth(context, ourRect, 10.0)
    # ***** Rectangle 4 *****
    # Move the rectangle's origin to the right by 200 units.
    ourRect.origin.x += 200.0
    # Stroke then fill the rect.
    Quartz.CGContextStrokeRectWithWidth(context, ourRect, 10.0)
    Quartz.CGContextFillRect(context, ourRect)

def createRectPath(context, rect):
    # Create a path using the coordinates of the rect passed in.
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextMoveToPoint(context, rect.origin.x, rect.origin.y)
    # ***** Segment 1 *****
    Quartz.CGContextAddLineToPoint(context, rect.origin.x + rect.size.width,
                                rect.origin.y)
    # ***** Segment 2 *****
    Quartz.CGContextAddLineToPoint(context, rect.origin.x + rect.size.width,
                                rect.origin.y + rect.size.height)
    # ***** Segment 3 *****
    Quartz.CGContextAddLineToPoint(context, rect.origin.x,
                                rect.origin.y + rect.size.height)
    # ***** Segment 4 is created by closing the path *****
    Quartz.CGContextClosePath(context)

def doPathRects(context):
    # Define a rectangle to use for drawing.
    ourRect = Quartz.CGRectMake(20.0, 20.0, 130.0, 100.0)

    # ***** Rectangle 1 *****
    # Create the rect path.
    createRectPath (context, ourRect)
    # Set the fill color to a light opaque blue.
    Quartz.CGContextSetRGBFillColor(context, 0.482, 0.62, 0.871, 1.0)
    # Fill the path.
    Quartz.CGContextDrawPath (context, Quartz.kCGPathFill) # Clears the path.
    # ***** Rectangle 2 *****
    # Translate the coordinate system 200 units to the right.
    Quartz.CGContextTranslateCTM(context, 200.0, 0.0)
    # Set the stroke color to an opaque green.
    Quartz.CGContextSetRGBStrokeColor(context, 0.404, 0.808, 0.239, 1.0)
    createRectPath (context, ourRect)
    # Set the line width to 10 units.
    Quartz.CGContextSetLineWidth (context, 10.0)
    # Stroke the path.
    Quartz.CGContextDrawPath (context, Quartz.kCGPathStroke)  # Clears the path.
    # ***** Rectangle 3 *****
    # Translate the coordinate system
    # 200 units to the left and 200 units down.
    Quartz.CGContextTranslateCTM(context, -200.0, -200.0)
    createRectPath (context, ourRect)
    #Quartz.CGContextSetLineWidth(context, 10.0)       # This is redundant.
    # Fill, then stroke the path.
    Quartz.CGContextDrawPath (context, Quartz.kCGPathFillStroke)  # Clears the path.
    # ***** Rectangle 4 *****
    # Translate the coordinate system 200 units to the right.
    Quartz.CGContextTranslateCTM(context, 200.0, 0.0)
    createRectPath (context, ourRect)
    # Stroke the path.
    Quartz.CGContextDrawPath (context, Quartz.kCGPathStroke)  # Clears the path.
    # Create the path again.
    createRectPath (context, ourRect)
    # Fill the path.
    Quartz.CGContextDrawPath (context, Quartz.kCGPathFill) # Clears the path.

def doAlphaRects(context):
    # ***** Part 1 *****
    ourRect = Quartz.CGRectMake(0.0, 0.0, 130.0, 100.0)
    numRects = 6
    rotateAngle = 2*math.pi/numRects
    tintAdjust = 1.0/numRects

    # ***** Part 2 *****
    Quartz.CGContextTranslateCTM(context, 2*ourRect.size.width,
                                    2*ourRect.size.height)

    # ***** Part 3 *****
    tint = 1.0
    for i in range(numRects):
        Quartz.CGContextSetRGBFillColor (context, tint, 0.0, 0.0, tint)
        Quartz.CGContextFillRect(context, ourRect)
        # These transformations are cummulative.
        Quartz.CGContextRotateCTM(context, rotateAngle)
        tint -= tintAdjust

def drawStrokedLine(context, start, end):
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextMoveToPoint(context, start.x, start.y)
    Quartz.CGContextAddLineToPoint(context, end.x, end.y)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathStroke)

def doDashedLines(context):
    lengths = ( 12.0, 6.0, 5.0, 6.0, 5.0, 6.0 )

    start = Quartz.CGPoint(20.0, 270.0)
    end = Quartz.CGPoint(300.0, 270.0)
    # ***** Line 1 solid line *****
    Quartz.CGContextSetLineWidth(context, 5.0)
    drawStrokedLine(context, start, end)
    # ***** Line 2 long dashes *****
    Quartz.CGContextTranslateCTM(context, 0.0, -50.0)
    Quartz.CGContextSetLineDash(context, 0.0, lengths, 2)
    drawStrokedLine(context, start, end)
    # ***** Line 3 long short pattern *****
    Quartz.CGContextTranslateCTM(context, 0.0, -50.0)
    Quartz.CGContextSetLineDash(context, 0.0, lengths, 4)
    drawStrokedLine(context, start, end)
    # ***** Line 4 long short short pattern *****
    Quartz.CGContextTranslateCTM(context, 0.0, -50.0)
    Quartz.CGContextSetLineDash(context, 0.0, lengths, 6)
    drawStrokedLine(context, start, end)
    # ***** Line 5 short short long pattern *****
    Quartz.CGContextTranslateCTM(context, 0.0, -50.0)
    Quartz.CGContextSetLineDash(context, lengths[0]+lengths[1], lengths, 6)
    drawStrokedLine(context, start, end)
    # ***** Line 6 solid line *****
    Quartz.CGContextTranslateCTM(context, 0.0, -50.0)
    # Reset dash to solid line.
    Quartz.CGContextSetLineDash(context, 0, None, 0)
    drawStrokedLine(context, start, end)

def doClippedCircle(context):
    circleCenter = Quartz.CGPoint(150.0, 150.0)
    circleRadius = 100.0
    startingAngle = 0.0
    endingAngle = 2*math.pi
    ourRect = Quartz.CGRectMake(65.0, 65.0, 170.0, 170.0)

    # ***** Filled Circle *****
    Quartz.CGContextSetRGBFillColor(context, 0.663, 0., 0.031, 1.0)
    Quartz.CGContextBeginPath(context)
    # Construct the circle path counterclockwise.
    Quartz.CGContextAddArc(context, circleCenter.x,
                            circleCenter.y, circleRadius,
                            startingAngle, endingAngle, 0)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFill)

    # ***** Stroked Square *****
    Quartz.CGContextStrokeRect(context, ourRect)

    # Translate so that the next drawing doesn't overlap what
    # has already been drawn.
    Quartz.CGContextTranslateCTM(context, ourRect.size.width + circleRadius + 5.0, 0)
    # Create a rectangular path and clip to that path.
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextAddRect(context, ourRect)
    Quartz.CGContextClip(context)

    # ***** Clipped Circle *****
    Quartz.CGContextBeginPath(context)
    # Construct the circle path counterclockwise.
    Quartz.CGContextAddArc (context, circleCenter.x,
                            circleCenter.y, circleRadius,
                            startingAngle, endingAngle, 0)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFill)


def doPDFDocument(context, url):

    pdfDoc = Quartz.CGPDFDocumentCreateWithURL(url)
    if pdfDoc is not None:
        Quartz.CGContextScaleCTM(context, .5, .5)
        # The media box is the bounding box of the PDF document.
        pdfRect = Quartz.CGPDFDocumentGetMediaBox(pdfDoc, 1) # page 1
        # Set the destination rect origin to the Quartz origin.
        pdfRect.origin.x = pdfRect.origin.y = 0.
        # Draw page 1 of the PDF document.
        Quartz.CGContextDrawPDFDocument(context, pdfRect, pdfDoc, 1)

        Quartz.CGContextTranslateCTM(context, pdfRect.size.width*1.2, 0)
        # Scale non-uniformly making the y coordinate scale 1.5 times
        # the x coordinate scale.
        Quartz.CGContextScaleCTM(context, 1, 1.5)
        Quartz.CGContextDrawPDFDocument(context, pdfRect, pdfDoc, 1)

        Quartz.CGContextTranslateCTM(context, pdfRect.size.width*1.2, pdfRect.size.height)
        # Flip the y coordinate axis horizontally about the x axis.
        Quartz.CGContextScaleCTM(context, 1, -1)
        Quartz.CGContextDrawPDFDocument(context, pdfRect, pdfDoc, 1)

    else:
        print("Can't create PDF document for URL!")
