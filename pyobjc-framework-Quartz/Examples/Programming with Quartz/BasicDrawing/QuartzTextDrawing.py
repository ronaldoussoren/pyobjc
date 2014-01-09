import Quartz

import Utilities

import sys

def drawQuartzRomanText(context):
    text = b"Quartz"
    textlen = len(text)
    fontSize = 60

    opaqueBlack = [0.0, 0.0, 0.0, 1.0]
    opaqueRed   = [0.663, 0.0, 0.031, 1.0]

    # Set the fill color space. This sets the
    # fill painting color to opaque black.
    Quartz.CGContextSetFillColorSpace(context,
        Utilities.getTheCalibratedRGBColorSpace())

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code: the identity transform.
    Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    Quartz.CGContextSelectFont(context, b"Times-Roman", fontSize, Quartz.kCGEncodingMacRoman)

    # The default text drawing mode is fill. Draw the text at (70, 400).
    Quartz.CGContextShowTextAtPoint(context, 70, 400, text, textlen)

    # Set the fill color to red.
    Quartz.CGContextSetFillColor(context, opaqueRed)

    # Draw the next piece of text where the previous one left off.
    Quartz.CGContextShowText(context, text, textlen)

    for i in range(3):
        # Get the current text pen position.
        p = Quartz.CGContextGetTextPosition(context)
        # Translate to the current text pen position.
        Quartz.CGContextTranslateCTM(context, p.x, p.y)

        # Rotate clockwise by 90 degrees for the next
        # piece of text.
        Quartz.CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(-90))
        # Draw the next piece of text in blac at the origin.
        Quartz.CGContextSetFillColor(context, opaqueBlack)
        Quartz.CGContextShowTextAtPoint(context, 0, 0, text, textlen)
        # Draw the next piece of text where the previous piece
        # left off and paint it with red.
        Quartz.CGContextSetFillColor(context, opaqueRed)
        Quartz.CGContextShowText(context, text, textlen)


def myCGContextStrokeLineSegments(context, s, count):
    # CGContextStrokeLineSegments is available only on Tiger and later
    # so if it isn't available, use an emulation of
    # CGContextStrokeLineSegments. It is better to use the
    # built-in CGContextStrokeLineSegments since it has significant
    # performance optimizations on some hardware.
    if hasattr(Quartz, 'CGContextStrokeLineSegments'):
        Quartz.CGContextStrokeLineSegments(context, s, count)
    else:
        Quartz.CGContextBeginPath(context)
        for k in range(0, count, 2):
            Quartz.CGContextMoveToPoint(context, s[k].x, s[k].y)
            Quartz.CGContextAddLineToPoint(context, s[k+1].x, s[k+1].y)
        Quartz.CGContextStrokePath(context)

_gridLines = []
def drawGridLines(context):
    numlines = 60

    if not _gridLines:
        stepsize = 4.0
        val = 0
        for i in range(0, 2*numlines, 2):
            _gridLines.append(Quartz.CGPointMake(val, -60))
            _gridLines.append(Quartz.CGPointMake(val, 200))
            val += stepsize

        val = -20
        for i in range(2*numlines, 4*numlines, 2):
            _gridLines.append(Quartz.CGPointMake(0, val))
            _gridLines.append(Quartz.CGPointMake(400, val))
            val += stepsize

    myCGContextStrokeLineSegments(context, _gridLines,  len(_gridLines))

def drawQuartzTextWithTextModes(context):
    fillText = b"Fill "
    strokeText = b"Stroke "
    fillAndStrokeText = b"FillStroke "
    invisibleText = b"Invisible "
    clipText = b"ClipText "
    fillStrokeClipText = b"FillStrokeClip "
    fontSize = 40.0
    extraLeading = 5.0
    dash = (1,1)
    opaqueRed = (1.0, 0.0, 0.0, 1.0)

    # Set the fill and stroke color space. This sets the
    # fill and stroke painting color to opaque black.
    Quartz.CGContextSetFillColorSpace(context,
            Utilities.getTheCalibratedRGBColorSpace())
    Quartz.CGContextSetStrokeColorSpace(context,
            Utilities.getTheCalibratedRGBColorSpace())

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code: the identity transform.
    Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    Quartz.CGContextSelectFont(context, b"Times-Roman", fontSize, Quartz.kCGEncodingMacRoman)

    # ----  Text Line 1 ----

    # Default text drawing mode is fill. Draw the text at (10, 400).
    Quartz.CGContextShowTextAtPoint(context, 10, 400, fillText, len(fillText))

    # Set the fill color to red.
    Quartz.CGContextSetFillColor(context, opaqueRed)

    Quartz.CGContextSetTextPosition(context, 180, 400)
    Quartz.CGContextShowText(context, fillText, len(fillText))

    # Translate down for the next line of text.
    Quartz.CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 2 ----

    # Now stroke the text by setting the text drawing mode
    # to kCGTextStroke. When stroking text, Quartz uses the stroke
    # color in the graphics state.
    Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextStroke)
    Quartz.CGContextShowTextAtPoint(context, 10, 400, strokeText, len(strokeText))

    # When stroking text, the line width and other gstate parameters
    # that affect stroking affect text stroking as well.
    Quartz.CGContextSetLineWidth(context, 2)
    Quartz.CGContextSetLineDash(context, 0, dash, 2)

    Quartz.CGContextSetTextPosition(context, 180, 400)
    Quartz.CGContextShowText(context, strokeText, len(strokeText))

    # Reset the line dash and line width to their defaults.
    Quartz.CGContextSetLineDash(context, 0, None, 0)
    Quartz.CGContextSetLineWidth(context, 1)

    # Translate down for the next line of text.
    Quartz.CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 3 ----

    # Set the text drawing mode so that text is both filled and
    # stroked. This produces text that is filled with the fill
    # color and stroked with the stroke color.
    Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextFillStroke)
    Quartz.CGContextShowTextAtPoint(context, 10, 400,
            fillAndStrokeText, len(fillAndStrokeText))

    # Now draw again with a thicker stroke width.
    Quartz.CGContextSetLineWidth(context, 2)
    Quartz.CGContextSetTextPosition(context, 180, 400)
    Quartz.CGContextShowText(context, fillAndStrokeText, len(fillAndStrokeText))

    Quartz.CGContextSetLineWidth(context, 1)
    Quartz.CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 4 ----

    # Set the text drawing mode to invisible so that the next piece of
    # text does not appear. Quartz updates the text position as
    # if it had been drawn.
    Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextInvisible)
    Quartz.CGContextShowTextAtPoint(context, 10, 400,
            invisibleText, len(invisibleText))

    Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextFill)

    Quartz.CGContextSetTextPosition(context, 180, 400)
    Quartz.CGContextShowText(context, fillText, len(fillText))

    Quartz.CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # ----  Text Line 5 ----
    Quartz.CGContextSaveGState(context)
    if 1:
        # Use the text as a clipping path.
        Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextClip)
        Quartz.CGContextShowTextAtPoint(context, 10, 400, clipText, len(clipText))

        # Position and draw a grid of lines.
        Quartz.CGContextTranslateCTM(context, 10, 400)
        drawGridLines(context)
    Quartz.CGContextRestoreGState(context)

    Quartz.CGContextSaveGState(context)
    if 1:
        # The current text position is that after the last piece
        # of text has been drawn. Since CGContextSaveGState/
        # CGContextRestoreGState do not affect the text position or
        # the text matrix, the text position is that after the last
        # text was "drawn", that drawn with the kCGTextClip mode
        # above. This is where the next text drawn will go if it
        # isn't explicitly positioned.
        nextTextPosition = Quartz.CGContextGetTextPosition(context)

        # Draw so that the text is filled, stroked, and then used
        # the clip subsequent drawing.
        Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextFillStrokeClip)

        # Explicitly set the text position.
        Quartz.CGContextSetTextPosition(context, 180, 400)
        nextTextPosition = Quartz.CGContextGetTextPosition(context)

        Quartz.CGContextShowText(context, fillStrokeClipText, len(fillStrokeClipText))
        # Adjust the location of the grid lines so that they overlap the
        # text just drawn.
        Quartz.CGContextTranslateCTM(context, nextTextPosition.x, nextTextPosition.y)
        # Draw the grid lines clipped by the text.
        drawGridLines(context)
    Quartz.CGContextRestoreGState(context)

# showFlippedTextAtPoint is a cover routine for Quartz.CGContextShowText
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
    t = Quartz.CGAffineTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0)
    # Get the existing text matrix.
    s = Quartz.CGContextGetTextMatrix(c)
    # Set the text matrix to the one that flips in y.
    Quartz.CGContextSetTextMatrix(c, t)
    # Draw the text at the point.
    Quartz.CGContextShowTextAtPoint(c, x, y, text, textLen)
    # Get the updated text position.
    p = Quartz.CGContextGetTextPosition(c)
    # Update the saved text matrix to reflect the updated
    # text position.
    s.tx = p.x ; s.ty = p.y
    # Reset to the text matrix in effect when this
    # routine was called but with the text position updated.
    Quartz.CGContextSetTextMatrix(c, s)


def drawQuartzTextWithTextMatrix(context):
    fontSize = 60.0
    extraLeading = 10.0
    text = b"Quartz "
    textlen = len(text)

    # The Cocoa framework calls the draw method with an undefined
    # value of the text matrix. It's best to set it to what is needed by
    # this code. Initially that is the identity transform.
    Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)

    # Set the font with the PostScript name "Times-Roman", at
    # fontSize points, with the MacRoman encoding.
    Quartz.CGContextSelectFont(context, b"Times-Roman", fontSize, Quartz.kCGEncodingMacRoman)

    # ----  Text Line 1 ----

    # Draw the text at (10, 600).
    Quartz.CGContextShowTextAtPoint(context, 10, 600, text, textlen)

    # Get the current text position. The text pen is at the trailing
    # point from the text just drawn.
    textPosition = Quartz.CGContextGetTextPosition(context)

    # Set the text matrix to one that flips text in y and sets
    # the text position to the user space coordinate (0,0).
    t = Quartz.CGAffineTransformMake(1, 0, 0, -1, 0, 0)
    Quartz.CGContextSetTextMatrix(context, t)

    # Set the text position to the point where the previous text ended.
    Quartz.CGContextSetTextPosition(context, textPosition.x, textPosition.y)

    # Draw the text at the current text position. It will be drawn
    # flipped in y, relative to the text drawn previously.
    Quartz.CGContextShowText(context, text, textlen)

    # ----  Text Line 2 ----

    # Translate down for the next piece of text.
    Quartz.CGContextTranslateCTM(context, 0, -(3*fontSize + extraLeading))

    Quartz.CGContextSaveGState(context)
    if 1:
        # Change the text matrix to {1, 0, 0, 3, 0, 0}, which
        # scales text by a factor of 1 in x and 3 in y.
        # This scaling doesn't affect any drawing other than text
        # drawing since only text drawing is transformed by
        # the text matrix.
        t = Quartz.CGAffineTransformMake(1, 0, 0, 3, 0, 0)
        Quartz.CGContextSetTextMatrix(context, t)

        # This text is scaled relative to the previous text
        # because of the text matrix scaling.
        Quartz.CGContextShowTextAtPoint(context, 10, 600, text, textlen)

    # This restores the graphics state to what it was at the time
    # of the last Quartz.CGContextSaveGState, but since the text matrix
    # isn't part of the Quartz graphics state, it isn't affected.
    Quartz.CGContextRestoreGState(context)

    # The text matrix isn't affected by Quartz.CGContextSaveGState and
    # Quartz.CGContextRestoreGState. You can see this by observing that
    # the next text piece appears immediately after the first piece
    # and with the same text scaling as that text drawn with the
    # text matrix established before we did CGContextRestoreGState.
    Quartz.CGContextShowText(context, text, textlen)

    # ----  Text Line 3 ----
    # Translate down for the next piece of text.
    Quartz.CGContextTranslateCTM(context, 0, -(fontSize + extraLeading))

    # Reset the text matrix to the identity matrix.
    Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)

    # Now draw text in a flipped coordinate system.
    Quartz.CGContextSaveGState(context)
    if 1:
        # Flip the coordinate system to mimic a coordinate system with the origin
        # at the top-left corner of a window. The new origin is at 600 units in
        # +y from the old origin and the y axis now increases with positive y
        # going down the window.
        Quartz.CGContextConcatCTM(context, Quartz.CGAffineTransformMake(1, 0, 0, -1, 0, 600))
        # This text will be flipped along with the CTM.
        Quartz.CGContextShowTextAtPoint(context, 10, 10, text, textlen)
        # Obtain the user space coordinates of the current text position.
        textPosition = Quartz.CGContextGetTextPosition(context)
        # Draw text at that point but flipped in y.
        showFlippedTextAtPoint(context, textPosition.x, textPosition.y, text, textlen)
    Quartz.CGContextRestoreGState(context)
