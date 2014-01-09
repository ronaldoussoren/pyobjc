import Quartz
import Utilities

import sys

def scalePatternPhase(phase):
    # Adjust the pattern phase if scaling to export as bits. This is equivalent to scaling base
    # space by the scaling factor.
    patternScaling = Utilities.getScalingFactor()
    if patternScaling != 1.0:
        phase = Quartz.CGSizeApplyAffineTransform(phase,
            Quartz.CGAffineTransformMakeScale(patternScaling, patternScaling))

    return phase

def scalePatternMatrix(patternTransform):
    # Scale the pattern by the scaling factor when exporting to bits. This is equivalent to
    # scaling base space by the scaling factor.
    patternScaling = Utilities.getScalingFactor()
    if patternScaling != 1.0:
        patternTransform = Quartz.CGAffineTransformConcat(patternTransform,
                Quartz.CGAffineTransformMakeScale(patternScaling, patternScaling))

    return patternTransform


def myDrawRedBlackCheckerBoardPattern(info, patternCellContext):
    # This pattern proc draws a red and a black rectangle
    # patch representing the minimum cell needed to paint a
    # checkerboard with that pattern.
    #
    # Each 'cell' of the checkerboard is 2 units on a side.
    #
    # This code uses Quartz.CGColorRefs which are available in Panther
    # and later only. Patterns are available in all versions of
    # Mac OS X but this code uses Quartz.CGColorRefs for convenience
    # and efficiency.

    # Paint a black checkerboard box.
    Quartz.CGContextSetFillColorWithColor(patternCellContext,
            Utilities.getRGBOpaqueBlackColor())
    # This is a 1x1 unit rect whose origin is at 0,0 in pattern space.
    Quartz.CGContextFillRect(patternCellContext, Quartz.CGRectMake(0.0, 0.0, 1.0, 1.0))
    # This is a 1x1 unit rect whose origin is at 1,1 in pattern space.
    Quartz.CGContextFillRect(patternCellContext, Quartz.CGRectMake(1.0, 1.0, 1.0, 1.0))

    # Paint a red checkerboard box.
    Quartz.CGContextSetFillColorWithColor(patternCellContext,
            Utilities.getRGBOpaqueRedColor())
    # This is a 1x1 unit rect whose origin is at 1,0 in pattern space,
    # that is, immediately to the right of first black checkerboard box.
    Quartz.CGContextFillRect(patternCellContext, Quartz.CGRectMake(1.0, 0.0, 1.0, 1.0))
    # This is a 1x1 unit rect whose origin is at 0,1 in pattern space,
    # that is, immediately above the first black checkerboard box.
    Quartz.CGContextFillRect(patternCellContext, Quartz.CGRectMake(0.0, 1.0, 1.0, 1.0))

def createRedBlackCheckerBoardPattern(patternTransform):
    pattern = Quartz.CGPatternCreate(None,
        # The pattern cell origin is at (0,0) with a
        # width of 2 units and a height of 2 units.
        Quartz.CGRectMake(0, 0, 2, 2),
        # Use the pattern transform supplied to this routine.
        scalePatternMatrix(patternTransform),
        # In pattern space the xStep is 2 units to the next cell in x
        # and the yStep is 2 units to the next row of cells in y.
        2, 2,
        # This value is a good choice for this type of pattern and it
        # avoids seams between tiles.
        Quartz.kCGPatternTilingConstantSpacingMinimalDistortion,
        # This pattern has intrinsic color.
        True,
        myDrawRedBlackCheckerBoardPattern,
        )
    return pattern

def doRedBlackCheckerboard(context):
    dash = [4]
    pattern = createRedBlackCheckerBoardPattern(
                            Quartz.CGAffineTransformMakeScale(20, 20))
    if pattern is None:
        print("Couldn't create pattern!")
        return

    # Create the pattern color space. Since the pattern
    # itself has intrinsic color, the 'baseColorSpace' parameter
    # to Quartz.CGColorSpaceCreatePattern must be None.
    patternColorSpace = Quartz.CGColorSpaceCreatePattern(None)
    Quartz.CGContextSetFillColorSpace(context, patternColorSpace)

    # The pattern has intrinsic color so the color components array
    # passed to CGContextSetFillPattern is just the alpha value used
    # to composite the pattern cell.

    # Paint the pattern with alpha = 1.
    color = [1.0]

    # Set the fill color to the checkerboard pattern.
    Quartz.CGContextSetFillPattern(context, pattern, color)

    # Fill a 100x100 unit rect at (20,20).
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(20, 20, 100, 100))

    # Save the graphics state before changing the stroke color.
    Quartz.CGContextSaveGState(context)
    if 1:
        # Set the stroke color space and color to the pattern.
        Quartz.CGContextSetStrokeColorSpace(context, patternColorSpace)
        Quartz.CGContextSetStrokePattern(context, pattern, color)

        # Stroke an ellipse with the pattern.
        Quartz.CGContextSetLineWidth(context, 8)
        Quartz.CGContextBeginPath(context)
        Utilities.myCGContextAddEllipseInRect(context, Quartz.CGRectMake(120, 20, 50, 100))
        Quartz.CGContextStrokePath(context)

    # Restore to the graphics state without the
    # pattern stroke color.
    Quartz.CGContextRestoreGState(context)

    # Now draw text.
    Quartz.CGContextSetTextMatrix(context, Quartz.CGAffineTransformIdentity)
    # Choose the font with the PostScript name "Times-Roman",
    # size 80 points, with the encoding MacRoman encoding.
    Quartz.CGContextSelectFont(context, b"Times-Roman", 80, Quartz.kCGEncodingMacRoman)

    # Using the fill text drawing mode.
    Quartz.CGContextSetTextDrawingMode(context, Quartz.kCGTextFill)

    # Draw text with the pattern.
    Quartz.CGContextShowTextAtPoint(context, 20, 120, b"Text", 4)

    # Rectangle 1, filled.
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(200, 20, 90, 90))

    # Rectangle 2, filled and stroked with a dash.
    Quartz.CGContextSetLineWidth(context, 2)
    Quartz.CGContextSetLineDash(context, 0, dash, 1)
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextAddRect(context, Quartz.CGRectMake(200, 70, 90, 90))
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFillStroke)

def doPatternMatrix(context):
    basePatternMatrix = Quartz.CGAffineTransformMakeScale(20, 20)
    pattern = createRedBlackCheckerBoardPattern(basePatternMatrix)
    if pattern is None:
        print("Couldn't create pattern!")
        return

    # Create the pattern color space. Since the pattern
    # itself has intrinsic color, the 'baseColorSpace' parameter
    # to Quartz.CGColorSpaceCreatePattern must be None.
    patternColorSpace = Quartz.CGColorSpaceCreatePattern(None)

    Quartz.CGContextSetFillColorSpace(context, patternColorSpace)
    del patternColorSpace

    Quartz.CGContextTranslateCTM(context, 40, 40)
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase(Quartz.CGSize(40, 40)))

    # The pattern has intrinsic color so the color components array
    # passed to Quartz.CGContextSetFillPattern is the alpha value used
    # to composite the pattern cell.

    # Paint the pattern first with alpha = 1.
    color = [1]
    Quartz.CGContextSetFillPattern(context, pattern, color)

    # Rectangle 1.
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 100, 100))

    Quartz.CGContextSaveGState(context)
    if 1:
        # Rectangle 2.
        # Paint the pattern with 65% alpha.
        color = [0.65]
        Quartz.CGContextSetFillPattern(context, pattern, color)
        # Rotate 45 degrees about the point (150, 50).
        Quartz.CGContextTranslateCTM(context, 150.0, 50.0)
        Quartz.CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(45.0))
        Quartz.CGContextTranslateCTM(context, -50.0, -50.0)
        # Rectangle 2. Patterns do not translate, scale or
        # rotate with the CTM. You can see that the pattern
        # tile of this filled rectangle is that of Rectangle
        # 1.
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 100, 100))
        # Release the pattern.
        del pattern
    Quartz.CGContextRestoreGState(context)

    Quartz.CGContextSaveGState(context)
    if 1:
        # Rectangle 3. The pattern is rotated with the object.
        # Rotate 45 degrees about the point 250, 50.
        t = Quartz.CGAffineTransformMakeTranslation(250.0, 50.0)
        t = Quartz.CGAffineTransformRotate(t, Utilities.DEGREES_TO_RADIANS(45.0))
        # Translate back to -50, -50.
        t = Quartz.CGAffineTransformTranslate(t, -50.0, -50.0)
        Quartz.CGContextConcatCTM(context, t)
        # Make a new pattern that is equivalent to
        # the old pattern but transformed to current user
        # space. The order of transformations is crucial.
        # This ordering is equivalent to using the same pattern
        # matrix as before but transforming base space by t.
        patTransform = Quartz.CGAffineTransformConcat(basePatternMatrix, t)
        pattern = createRedBlackCheckerBoardPattern(patTransform)
        color = [1]
        Quartz.CGContextSetFillPattern(context, pattern, color)
        # Release the pattern.
        del pattern
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 100, 100))
    Quartz.CGContextRestoreGState(context)

    Quartz.CGContextSaveGState(context)
    if 1:
        # Rectangle 4. The pattern is scaled with the object.
        # Translate and scale.
        t = Quartz.CGAffineTransformMakeTranslation(320, 0)
        t = Quartz.CGAffineTransformScale(t, 2, 2)
        Quartz.CGContextConcatCTM(context, t)
        # Make a new pattern that is equivalent to
        # the old pattern but transformed to current user
        # space. The order of transformations is crucial.
        # This ordering is equivalent to using the same pattern
        # matrix as before but transforming base space by t.
        patTransform = Quartz.CGAffineTransformConcat(basePatternMatrix, t)
        pattern = createRedBlackCheckerBoardPattern(patTransform)
        color = [1]
        Quartz.CGContextSetFillPattern(context, pattern, color)
        # Release the pattern.
        del pattern
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 100, 100))
    Quartz.CGContextRestoreGState(context)


def doPatternPhase(context):
    pattern = createRedBlackCheckerBoardPattern(
                            Quartz.CGAffineTransformMakeScale(20, 20))
    if pattern is None:
        print("Couldn't create pattern!")
        return

    # Create the pattern color space for a colored pattern.
    patternColorSpace = Quartz.CGColorSpaceCreatePattern(None)
    Quartz.CGContextSetFillColorSpace(context, patternColorSpace)

    # Paint the pattern with alpha = 1.
    color = (1,)
    Quartz.CGContextSetFillPattern(context, pattern, color)

    # Rectangle 1
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(20, 150, 100, 100))

    # Rectangle 2
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(130, 150, 100, 100))

    # Rectangle 3
    # Set the pattern phase so that the pattern origin
    # is at the lower-left of the shape.
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(20, 20) ))
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(20, 20, 100, 100))

    # Rectangle 4
    # Set the pattern phase so that the pattern origin
    # is at the lower-left corner of the shape.
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(130, 20) ))
    Quartz.CGContextTranslateCTM(context, 130, 20)
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 100, 100))

def drawRotatedRect(c, p):
    r = Quartz.CGRectMake(0, 0, 1, 1)
    Quartz.CGContextSaveGState(c)
    if 1:
        Quartz.CGContextTranslateCTM(c, p.x, p.y)
        Quartz.CGContextRotateCTM(c, Utilities.DEGREES_TO_RADIANS(45))
        Quartz.CGContextTranslateCTM(c, -r.size.width/2, -r.size.height/2)
        Quartz.CGContextFillRect(c, r)
    Quartz.CGContextRestoreGState(c)

def myStencilPatternProc(info, patternCellContext):
    drawRotatedRect(patternCellContext, Quartz.CGPointMake(1, 1))
    drawRotatedRect(patternCellContext, Quartz.CGPointMake(1.75, 1))

def createStencilPattern(patternTransform):
    pattern = Quartz.CGPatternCreate(None,
                # The pattern cell origin is at (0,0) with a
                # width of 2.5 units and a height of 2 units. This
                # pattern cell has transparent areas since
                # the pattern proc only marks a portion of the cell.
                Quartz.CGRectMake(0, 0, 2.5, 2),
                # Use the pattern transform supplied to this routine.
                scalePatternMatrix(patternTransform),
                # Use the width and height of the pattern cell for
                # the xStep and yStep.
                2.5, 2,
                # This value is a good choice for this type of pattern and it
                # avoids seams between tiles.
                Quartz.kCGPatternTilingConstantSpacingMinimalDistortion,
                # This pattern does not have intrinsic color.
                False,   # Must be False for a stencil pattern.
                myStencilPatternProc,
                )
    return pattern

def doStencilPattern(context):
    pattern = createStencilPattern(Quartz.CGAffineTransformMakeScale(20, 20))
    if pattern is None:
        print("Couldn't create pattern!")
        return

    # Create the pattern color space. This pattern is a stencil
    # pattern so when the code sets the pattern it also sets the
    # color it will paint the pattern with. In order to
    # set the pattern color space in this case we also have
    # to say what underlying color space should be used when
    # the pattern proc is called.
    baseColorSpace = Utilities.getTheCalibratedRGBColorSpace()
    patternColorSpace = Quartz.CGColorSpaceCreatePattern(baseColorSpace)

    Quartz.CGContextSetFillColorSpace(context, patternColorSpace)
    # This code is finished with the pattern color space and can release
    # it because Quartz retains it while it is the current color space.
    del patternColorSpace

    # The pattern has no intrinsic color so the color components array
    # passed to CGContextSetFillPattern contains the colors to paint
    # the pattern with in the baseColorSpace. In the case here,
    # first paint the pattern with opaque blue.
    color = (0.11, 0.208, 0.451, 1.0)
    Quartz.CGContextSetFillPattern(context, pattern, color)

    # Rectangle 1.
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(20, 160) ))
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextAddRect(context, Quartz.CGRectMake(20, 160, 105, 80))
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFillStroke)

    # Rectangle 2.
    # Set the pattern color so the stencil pattern
    # is painted in a yellow shade.
    color = (1.0, 0.816, 0.0, 1.0)
    Quartz.CGContextSetFillPattern(context, pattern, color)
    # Set the pattern phase to the origin of the next object.
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(140, 160) ))
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextAddRect(context, Quartz.CGRectMake(140, 160, 105, 80))
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFillStroke)

    Quartz.CGContextSaveGState(context)
    if 1:
        Quartz.CGContextSetFillColorWithColor(context,
                Utilities.getRGBOpaqueBlueColor())
        # Fill color is now blue. Paint two blue rectangles
        # that will be underneath the drawing which follows.
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(20, 40, 105, 80))
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(140, 40, 105, 80))
    Quartz.CGContextRestoreGState(context)

    # The fill color is again the stencil pattern with
    # the underlying fill color an opaque yellow.

    # Rectangle 3.
    # This paints over the blue rect just painted at 20,40
    # and the blue underneath is visible where the pattern has
    # transparent areas.
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(20, 40) ))
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(20, 40, 105, 80))

    # Rectangle 4.
    # Change the alpha value of the underlying color used
    # to paint the stencil pattern.
    color = list(color)
    color[3] = 0.75
    Quartz.CGContextSetFillPattern(context, pattern, color)
    Quartz.CGContextSetPatternPhase(context, scalePatternPhase( Quartz.CGSizeMake(140, 40) ))
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(140, 40, 105, 80))

class MyPDFPatternInfo (object):
    rect = None
    pdfDoc = None

def myDrawPDFPattern(info, patternCellContext):
    # This pattern proc draws the first page of a PDF document to
    # a destination rect.
    Quartz.CGContextSaveGState(patternCellContext)
    Quartz.CGContextClipToRect(patternCellContext, info.rect)
    Quartz.CGContextDrawPDFDocument(patternCellContext, info.rect, info.pdfDoc, 1)
    Quartz.CGContextRestoreGState(patternCellContext)

# Versions of Tiger prior to 10.4.3 have a bug such that use of an xStep that
# doesn't match the width of pattern bounding box or a yStep that doesn't match the
# height of the pattern bounding box produces incorrect results when drawn
# to a bit-based context. Setting TIGERSTEPWORKAROUND works around this bug.


TIGERSTEPWORKAROUND=1
SCALEPATTERN=1
OPTIMIZEDPERF=0


def createPDFPatternPattern(additionalTransformP, url):
    patternInfoP = MyPDFPatternInfo()

    patternInfoP.pdfDoc = Quartz.CGPDFDocumentCreateWithURL(url)
    if patternInfoP.pdfDoc is None:
        print("Couldn't create PDF document reference!")
        return

    patternInfoP.rect = Quartz.CGPDFDocumentGetMediaBox(patternInfoP.pdfDoc, 1)
    # Set the origin of the media rect for the PDF document to (0,0).
    patternInfoP.rect.origin = Quartz.CGPointZero

    if additionalTransformP is not None:
        patternTransform = additionalTransformP
    else:
        patternTransform = Quartz.CGAffineTransformIdentity

    # To emulate the example from the bitmap context drawing chapter,
    # the tile offset in each dimension is the tile size in that
    # dimension, plus 6 units.
    if SCALEPATTERN:
        tileOffsetX = 6. + patternInfoP.rect.size.width
        tileOffsetY = 6. + patternInfoP.rect.size.height
    else:
        tileOffsetX = 2. + patternInfoP.rect.size.width
        tileOffsetY = 2. + patternInfoP.rect.size.height

    # Tiger versions 10.4.0 - 10.4.2 have a bug such that the bounds
    # width and height is incorrectly used as the xstep,ystep.
    # To workaround this bug, we can make the bounds rect incorporate
    # the xstep,ystep since xstep,ystep are larger than the bounds.
    if OPTIMIZEDPERF or TIGERSTEPWORKAROUND:
        patternRect = Quartz.CGRectMake(0, 0, tileOffsetX, tileOffsetY)
    else:
        patternRect = patternInfoP.rect

    if OPTIMIZEDPERF:
        # Produces best performance if bbox == xstep/ystep
        spacing = Quartz.kCGPatternTilingConstantSpacing
    else:
        spacing = Quartz.kCGPatternTilingConstantSpacingMinimalDistortion

    pattern = Quartz.CGPatternCreate(patternInfoP,
            # The pattern cell size is the size
            # of the media rect of the PDF document.
            patternRect,
            scalePatternMatrix(patternTransform),
            tileOffsetX, tileOffsetY,
            # This value is a good choice for this type of pattern and
            #  it avoids seams between tiles.
            spacing,
            # This pattern has intrinsic color.
            True,
            myDrawPDFPattern,
            )
    # If the pattern can't be created then release the
    # pattern resources and info parameter.
    if pattern is None:
        patternInfoP = None

    return pattern


def drawWithPDFPattern(context, url):
    if SCALEPATTERN:
        patternMatrix = Quartz.CGAffineTransformMakeScale(1.0/3, 1.0/3)
    else:
        patternMatrix = Quartz.CGAffineTransformMakeScale(1, 1)

    # Scale the PDF pattern down to 1/3 its original size.
    pdfPattern = createPDFPatternPattern(patternMatrix, url)
    if pdfPattern is None:
        print("Couldn't create pattern!")
        return

    # Create the pattern color space. Since the pattern
    # itself has intrinsic color, the 'baseColorSpace' parameter
    # to CGColorSpaceCreatePattern must be None.
    patternColorSpace = Quartz.CGColorSpaceCreatePattern(None)
    Quartz.CGContextSetFillColorSpace(context, patternColorSpace)
    # Quartz retains the color space so this code
    # can now release it since it no longer needs it.
    del patternColorSpace

    # Paint the pattern with an alpha of 1.
    color = (1,)
    Quartz.CGContextSetFillPattern(context, pdfPattern, color)
    # Quartz retains the pattern so this code
    # can now release it since it no longer needs it.
    del pdfPattern

    # Fill a US Letter size rect with the pattern.
    Quartz.CGContextFillRect(context, Quartz.CGRectMake(0, 0, 612, 792))
