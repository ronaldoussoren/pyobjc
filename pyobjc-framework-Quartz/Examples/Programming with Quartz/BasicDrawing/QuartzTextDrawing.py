from Quartz import *
import Quartz

import Utilities

import sys

def drawQuartzRomanText(context):
    text = "Quartz"
    textlen = len(text)
    fontSize = 60

    opaqueBlack = [0.0, 0.0, 0.0, 1.0]
    opaqueRed   = [0.663, 0.0, 0.031, 1.0]

    # Set the fill color space. This sets the
    # fill painting color to opaque black.
    CGContextSetFillColorSpace(context,
        Utilities.getTheCalibratedRGBColorSpace())

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code: the identity transform.
    CGContextSetTextMatrix(context, CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    CGContextSelectFont(context, "Times-Roman", fontSize, kCGEncodingMacRoman)

    # The default text drawing mode is fill. Draw the text at (70, 400).
    CGContextShowTextAtPoint(context, 70, 400, text, textlen)

    # Set the fill color to red.
    CGContextSetFillColor(context, opaqueRed)

    # Draw the next piece of text where the previous one left off.
    CGContextShowText(context, text, textlen)

    for i in range(3):
        # Get the current text pen position.
        p = CGContextGetTextPosition(context)
        # Translate to the current text pen position.
        CGContextTranslateCTM(context, p.x, p.y)

        # Rotate clockwise by 90 degrees for the next
        # piece of text.
        CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(-90))
        # Draw the next piece of text in blac at the origin.
        CGContextSetFillColor(context, opaqueBlack)
        CGContextShowTextAtPoint(context, 0, 0, text, textlen)
        # Draw the next piece of text where the previous piece
        # left off and paint it with red.
        CGContextSetFillColor(context, opaqueRed)
        CGContextShowText(context, text, textlen)


def myCGContextStrokeLineSegments(context, s, count):
    # CGContextStrokeLineSegments is available only on Tiger and later
    # so if it isn't available, use an emulation of
    # CGContextStrokeLineSegments. It is better to use the
    # built-in CGContextStrokeLineSegments since it has significant
    # performance optimizations on some hardware.
    if hasattr(Quartz, 'CGContextStrokeLineSegments'):
        CGContextStrokeLineSegments(context, s, count)
    else:
        CGContextBeginPath(context)
        for k in xrange(0, count, 2):
            CGContextMoveToPoint(context, s[k].x, s[k].y)
            CGContextAddLineToPoint(context, s[k+1].x, s[k+1].y)
        CGContextStrokePath(context)

_gridLines = []
def drawGridLines(context):
    numlines = 60

    if not _gridLines:
        stepsize = 4.0
        val = 0
        for i in xrange(0, 2*numlines, 2):
            _gridLines.append(CGPointMake(val, -60))
            _gridLines.append(CGPointMake(val, 200))
            val += stepsize

        val = -20
        for i in xrange(2*numlines, 4*numlines, 2):
            _gridLines.append(CGPointMake(0, val))
            _gridLines.append(CGPointMake(400, val))
            val += stepsize

    myCGContextStrokeLineSegments(context, _gridLines,  len(_gridLines))

def drawQuartzTextWithTextModes(context):
    fillText = "Fill "
    strokeText = "Stroke "
    fillAndStrokeText = "FillStroke "
    invisibleText = "Invisible "
    clipText = "ClipText "
    fillStrokeClipText = "FillStrokeClip "
    fontSize = 40.0
    extraLeading = 5.0
    dash = (1,1)
    opaqueRed = (1.0, 0.0, 0.0, 1.0)

    # Set the fill and stroke color space. This sets the
    # fill and stroke painting color to opaque black.
    CGContextSetFillColorSpace(context,
            Utilities.getTheCalibratedRGBColorSpace())
    CGContextSetStrokeColorSpace(context,
            Utilities.getTheCalibratedRGBColorSpace())

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code: the identity transform.
    CGContextSetTextMatrix(context, CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    CGContextSelectFont(context, "Times-Roman", fontSize, kCGEncodingMacRoman)

    # ----  Text Line 1 ----

    # Default text drawing mode is fill. Draw the text at (10, 400).
    CGContextShowTextAtPoint(context, 10, 400, fillText, len(fillText))

    # Set the fill color to red.
    CGContextSetFillColor(context, opaqueRed)

    CGContextSetTextPosition(context, 180, 400)
    CGContextShowText(context, fillText, len(fillText))

    # Translate down for the next line of text.
    CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 2 ----

    # Now stroke the text by setting the text drawing mode
    # to kCGTextStroke. When stroking text, Quartz uses the stroke
    # color in the graphics state.
    CGContextSetTextDrawingMode(context, kCGTextStroke)
    CGContextShowTextAtPoint(context, 10, 400, strokeText, len(strokeText))

    # When stroking text, the line width and other gstate parameters
    # that affect stroking affect text stroking as well.
    CGContextSetLineWidth(context, 2)
    CGContextSetLineDash(context, 0, dash, 2)

    CGContextSetTextPosition(context, 180, 400)
    CGContextShowText(context, strokeText, len(strokeText))

    # Reset the line dash and line width to their defaults.
    CGContextSetLineDash(context, 0, None, 0)
    CGContextSetLineWidth(context, 1)

    # Translate down for the next line of text.
    CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 3 ----

    # Set the text drawing mode so that text is both filled and
    # stroked. This produces text that is filled with the fill
    # color and stroked with the stroke color.
    CGContextSetTextDrawingMode(context, kCGTextFillStroke)
    CGContextShowTextAtPoint(context, 10, 400,
            fillAndStrokeText, len(fillAndStrokeText))

    # Now draw again with a thicker stroke width.
    CGContextSetLineWidth(context, 2)
    CGContextSetTextPosition(context, 180, 400)
    CGContextShowText(context, fillAndStrokeText, len(fillAndStrokeText))

    CGContextSetLineWidth(context, 1)
    CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 4 ----

    # Set the text drawing mode to invisible so that the next piece of
    # text does not appear. Quartz updates the text position as
    # if it had been drawn.
    CGContextSetTextDrawingMode(context, kCGTextInvisible)
    CGContextShowTextAtPoint(context, 10, 400,
            invisibleText, len(invisibleText))

    CGContextSetTextDrawingMode(context, kCGTextFill)

    CGContextSetTextPosition(context, 180, 400)
    CGContextShowText(context, fillText, len(fillText))

    CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 5 ----
    CGContextSaveGState(context)
    if 1:
        # Use the text as a clipping path.
        CGContextSetTextDrawingMode(context, kCGTextClip)
        CGContextShowTextAtPoint(context, 10, 400, clipText, len(clipText))

        # Position and draw a grid of lines.
        CGContextTranslateCTM(context, 10, 400)
        drawGridLines(context)
    CGContextRestoreGState(context)

    CGContextSaveGState(context)
    if 1:
        # The current text position is that after the last piece
        # of text has been drawn. Since CGContextSaveGState/
        # CGContextRestoreGState do not affect the text position or
        # the text matrix, the text position is that after the last
        # text was "drawn", that drawn with the kCGTextClip mode
        # above. This is where the next text drawn will go if it
        # isn't explicitly positioned.
        nextTextPosition = CGContextGetTextPosition(context)

        # Draw so that the text is filled, stroked, and then used
        # the clip subsequent drawing.
        CGContextSetTextDrawingMode(context, kCGTextFillStrokeClip)

        # Explicitly set the text position.
        CGContextSetTextPosition(context, 180, 400)
        nextTextPosition = CGContextGetTextPosition(context)

        CGContextShowText(context, fillStrokeClipText, len(fillStrokeClipText))
        # Adjust the location of the grid lines so that they overlap the
        # text just drawn.
        CGContextTranslateCTM(context, nextTextPosition.x, nextTextPosition.y)
        # Draw the grid lines clipped by the text.
        drawGridLines(context)
    CGContextRestoreGState(context)

# showFlippedTextAtPoint is a cover routine for CGContextShowText
# that is useful for drawing text in a coordinate system where the y axis
# is flipped relative to the default Quartz coordinate system.
#
# This code assumes that the text matrix is only used to
# flip the text, not to perform scaling or any other
# possible use of the text matrix.
#
# This function preserves the a, b, c, and d components of
# the text matrix across its execution but updates the
# tx, ty components (the text position) to reflect the
# text just drawn. If all the text you draw is flipped, it
# isn't necessary to continually set the text matrix. Instead
# you could simply call CGContextSetTextMatrix once with
# the flipped matrix each time your drawing
# code is called.
def showFlippedTextAtPoint(c, x, y, text, textLen):
    t = CGAffineTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0)
    # Get the existing text matrix.
    s = CGContextGetTextMatrix(c)
    # Set the text matrix to the one that flips in y.
    CGContextSetTextMatrix(c, t)
    # Draw the text at the point.
    CGContextShowTextAtPoint(c, x, y, text, textLen)
    # Get the updated text position.
    p = CGContextGetTextPosition(c)
    # Update the saved text matrix to reflect the updated
    # text position.
    s.tx = p.x ; s.ty = p.y
    # Reset to the text matrix in effect when this
    # routine was called but with the text position updated.
    CGContextSetTextMatrix(c, s)


def drawQuartzTextWithTextMatrix(context):
    fontSize = 60.0
    extraLeading = 10.0
    text = "Quartz "
    textlen = len(text)

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code. Initially that is the identity transform.
    CGContextSetTextMatrix(context, CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    CGContextSelectFont(context, "Times-Roman", fontSize, kCGEncodingMacRoman)

    # ----  Text Line 1 ----

    # Draw the text at (10, 600).
    CGContextShowTextAtPoint(context, 10, 600, text, textlen)

    # Get the current text position. The text pen is at the trailing
    # point from the text just drawn.
    textPosition = CGContextGetTextPosition(context)

    # Set the text matrix to one that flips text in y and sets
    # the text position to the user space coordinate (0,0).
    t = CGAffineTransformMake(1, 0, 0, -1, 0, 0)
    CGContextSetTextMatrix(context, t)

    # Set the text position to the point where the previous text ended.
    CGContextSetTextPosition(context, textPosition.x, textPosition.y)

    # Draw the text at the current text position. It will be drawn
    # flipped in y, relative to the text drawn previously.
    CGContextShowText(context, text, textlen)

    # ----  Text Line 2 ----

    # Translate down for the next piece of text.
    CGContextTranslateCTM(context, 0, -(3*fontSize + extraLeading))

    CGContextSaveGState(context)
    if 1:
        # Change the text matrix to {1, 0, 0, 3, 0, 0}, which
        # scales text by a factor of 1 in x and 3 in y.
        # This scaling doesn't affect any drawing other than text
        # drawing since only text drawing is transformed by
        # the text matrix.
        t = CGAffineTransformMake(1, 0, 0, 3, 0, 0)
        CGContextSetTextMatrix(context, t)

        # This text is scaled relative to the previous text
        # because of the text matrix scaling.
        CGContextShowTextAtPoint(context, 10, 600, text, textlen)

    # This restores the graphics state to what it was at the time
    # of the last CGContextSaveGState, but since the text matrix
    # isn't part of the Quartz graphics state, it isn't affected.
    CGContextRestoreGState(context)

    # The text matrix isn't affected by CGContextSaveGState and
    # CGContextRestoreGState. You can see this by observing that
    # the next text piece appears immediately after the first piece
    # and with the same text scaling as that text drawn with the
    # text matrix established before we did CGContextRestoreGState.
    CGContextShowText(context, text, textlen)

    # ----  Text Line 3 ----
    # Translate down for the next piece of text.
    CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # Reset the text matrix to the identity matrix.
    CGContextSetTextMatrix(context, CGAffineTransformIdentity)

    # Now draw text in a flipped coordinate system.
    CGContextSaveGState(context)
    if 1:
        # Flip the coordinate system to mimic a coordinate system with the origin
        # at the top-left corner of a window. The new origin is at 600 units in
        # +y from the old origin and the y axis now increases with positive y
        # going down the window.
        CGContextConcatCTM(context, CGAffineTransformMake(1, 0, 0, -1, 0, 600))
        # This text will be flipped along with the CTM.
        CGContextShowTextAtPoint(context, 10, 10, text, textlen)
        # Obtain the user space coordinates of the current text position.
        textPosition = CGContextGetTextPosition(context)
        # Draw text at that point but flipped in y.
        showFlippedTextAtPoint(context, textPosition.x, textPosition.y, text, textlen)
    CGContextRestoreGState(context)
