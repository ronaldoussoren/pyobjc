import Quartz

import Utilities


def scaleShadowOffset(offset):
    shadowScaling = Utilities.getScalingFactor()
    # Adjust the shadow offset if scaling to export as bits. This is
    # equivalent to scaling base space by the scaling factor.
    if shadowScaling != 1.0:
        offset = Quartz.CGSizeApplyAffineTransform(offset,
                    Quartz.CGAffineTransformMakeScale(shadowScaling, shadowScaling))
    return offset


def createTrianglePath(context):
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextMoveToPoint(context, 0, 0)
    Quartz.CGContextAddLineToPoint(context, 50, 0)
    Quartz.CGContextAddLineToPoint(context, 25, 50)
    Quartz.CGContextClosePath(context)

def drawSimpleShadow(context):
    r = Quartz.CGRectMake(20, 20, 100, 200)

    Quartz.CGContextTranslateCTM(context, 20, 300)

    # A blur of 0 is a hard edge blur.
    blur = 0
    # An offset where both components are negative casts a shadow to the
    # left and down from the object. The coordinate system for the offset
    # is base space, not current user space.
    offset = Quartz.CGSize(-7, -7)
    offset = scaleShadowOffset(offset)

    # Set the shadow in the context.
    Quartz.CGContextSetShadow(context, offset, blur)

    # Object 1.
    # Paint a rectangle.
    Quartz.CGContextFillRect(context, r)

    # Object 2.
    Quartz.CGContextTranslateCTM(context, 150, 0)
    # A blur of 3 is a soft blur more
    # appropriate for a shadow effect.
    blur = 3
    Quartz.CGContextSetShadow(context, offset, blur)

    # Fill an ellipse to the right of the rect.
    Quartz.CGContextBeginPath(context)
    Utilities.myCGContextAddEllipseInRect(context, r)
    Quartz.CGContextFillPath(context)

    # Object 3.
    Quartz.CGContextTranslateCTM(context, -130, -140)
    # Scale the coordinate system but the shadow is not affected. The offset
    # is in the base space of the context. Typically it looks best if the shapes
    # have a uniform shadow regardless of how the shapes were created, scaled,
    # rotated, or otherwise transformed.
    Quartz.CGContextScaleCTM(context, 2, 2)
    createTrianglePath(context)
    Quartz.CGContextSetStrokeColorWithColor(context, Utilities.getRGBOpaqueRedColor())

    Quartz.CGContextSetLineWidth(context, 5)
    # Stroking produces a shadow as well.
    Quartz.CGContextStrokePath(context)

    # Object 4.
    Quartz.CGContextTranslateCTM(context, 75, 0)
    createTrianglePath(context)
    # Cast the shadow to the left and up from
    # the shape painted.
    offset.width = -5
    offset.height = +7
    offset = scaleShadowOffset(offset)

    # The shadow can be colored. Create a CGColorRef
    # that represents a red color with opacity of 0.3333...
    shadowColor = Quartz.CGColorCreateCopyWithAlpha(Utilities.getRGBOpaqueRedColor(), 1.0/3.0)

    Quartz.CGContextSetShadowWithColor(context, offset, blur, shadowColor)
    Quartz.CGContextStrokePath(context)

    # Object 5. Three stroked circles.
    Quartz.CGContextTranslateCTM(context, -75, -65)
    # Set a black shadow offset at -7,-7.
    offset.width = -7
    offset.height = -7

    offset = scaleShadowOffset(offset)

    Quartz.CGContextSetShadow(context, offset, blur)
    # Draw a set of three circles side by side.
    Quartz.CGContextBeginPath(context)
    Quartz.CGContextSetLineWidth(context, 3)
    r = Quartz.CGRectMake(30, 20, 20, 20)
    Utilities.myCGContextAddEllipseInRect(context, r)
    r = Quartz.CGRectOffset(r, 20, 0)
    Utilities.myCGContextAddEllipseInRect(context, r)
    r = Quartz.CGRectOffset(r, 20, 0)
    Utilities.myCGContextAddEllipseInRect(context, r)
    Quartz.CGContextStrokePath(context)


def doShadowScaling(context):
    offset = Quartz.CGSize(-7, -7)
    blur = 3

    Quartz.CGContextTranslateCTM(context, 20, 220)
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), blur)

    # Object 1
    # Draw a triangle filled with black and shadowed with black.
    createTrianglePath(context)
    Quartz.CGContextFillPath(context)

    # Object 2
    # Scaling without changing the shadow doesn't impact
    # the shadow offset or blur.
    t = Quartz.CGAffineTransformMakeScale(2, 2)
    Quartz.CGContextConcatCTM(context, t)
    Quartz.CGContextTranslateCTM(context, 40, 0)
    createTrianglePath(context)
    Quartz.CGContextFillPath(context)

    # Object 3
    # By transforming the offset you can transform the shadow.
    # This may be desirable if you are drawing a zoomed view.
    offset = Quartz.CGSizeApplyAffineTransform(offset, t)
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), blur)
    Quartz.CGContextTranslateCTM(context, 70, 0)
    createTrianglePath(context)
    Quartz.CGContextFillPath(context)


def drawFillAndStrokeWithShadow(context):
    r = Quartz.CGRectMake(60, 60, 100, 100)
    offset = Quartz.CGSize(-7, -7)
    blur = 3

    # Set the shadow.
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), blur)

    Quartz.CGContextSetFillColorWithColor(context, Utilities.getRGBOpaqueOrangeColor())

    # Draw the graphic on the left.
    Quartz.CGContextBeginPath(context)
    Utilities.myCGContextAddEllipseInRect(context, r)
    Quartz.CGContextDrawPath(context, Quartz.kCGPathFillStroke)

    # Draw the graphic on the right.
    r = Quartz.CGRectOffset(r, 125, 0)
    # Begin the transparency layer.
    Quartz.CGContextBeginTransparencyLayer(context, None)
    if 1:
        Utilities.myCGContextAddEllipseInRect(context, r)
        Quartz.CGContextDrawPath(context, Quartz.kCGPathFillStroke)
    # End the transparency layer.
    Quartz.CGContextEndTransparencyLayer(context)

def drawColoredLogo(context):
    r = Quartz.CGRectMake(0, 0, 100, 100)
    Quartz.CGContextSaveGState(context)
    if 1:
        # Position the center of the rectangle on the left.
        Quartz.CGContextTranslateCTM(context, 140, 140)
        # Rotate so that the rectangles are rotated 45 degrees
        # about the current coordinate origin.
        Quartz.CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(45))
        # Translate so that the center of the rect is at the previous origin.
        Quartz.CGContextTranslateCTM(context,
                -r.size.width/2, -r.size.height/2)
        # Set the fill color to a purple color.
        Quartz.CGContextSetFillColorWithColor(context,
                Utilities.getRGBOpaquePurpleColor())
        # Fill the first rectangle.
        Quartz.CGContextFillRect(context, r)
        # Position to draw the right-most rectangle.
        Quartz.CGContextTranslateCTM(context, 60, -60)
        # Set the fill color to a yellow color.
        Quartz.CGContextSetFillColorWithColor(context,
                Utilities.getRGBOpaqueYellowColor())
        Quartz.CGContextFillRect(context, r)

        # Position for the center rectangle.
        Quartz.CGContextTranslateCTM(context, -30, +30)
        # Set the stroke color to an orange color.
        Quartz.CGContextSetStrokeColorWithColor(context,
                Utilities.getRGBOpaqueOrangeColor())
        # Stroke the rectangle with a linewidth of 12.
        Quartz.CGContextStrokeRectWithWidth(context, r, 12)
    Quartz.CGContextRestoreGState(context)

def showComplexShadowIssues(context):
    offset = Quartz.CGSize(-6, -6)
    blur = 3

    # Set the shadow.
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), blur)
    # Draw the colored logo.
    drawColoredLogo(context)

def showComplexShadow(context):
    offset = Quartz.CGSize(-6, -6)
    blur = 3

    # Set the shadow.
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), blur)

    # Begin a transparency layer. A snapshot is made of the graphics state and
    # the shadow parameter is temporarily reset to no shadow, the blend mode
    # is set to Normal, and the global alpha parameter is set to 1.0.
    #
    # All drawing that occurs after CGContextBeginTransparencyLayer but before
    # CGContextEndTransparencyLayer is collected together and when
    # CGContextEndTransparencyLayer is called, Quartz composites the collected
    # drawing to the context, using the global alpha, blend mode, and shadow
    # that was in effect when CGContextBeginTransparencyLayer was called.

    Quartz.CGContextBeginTransparencyLayer(context, None)
    # Draw the colored logo.
    drawColoredLogo(context)

    # Ending the transparency layer causes all drawing in the transparency
    # layer to be composited with the global alpha, blend mode, and shadow
    # in effect at the time CGContextBeginTransparencyLayer was called.  The
    # graphics state is restored to that in effect when
    # CGContextBeginTransparencyLayer was called.

    # This restores the graphics state to that in effect
    # at the last call to CGContextBeginTransparencyLayer.
    Quartz.CGContextEndTransparencyLayer(context)

def doLayerCompositing(context):
    r = Quartz.CGRectMake(40, 50, 142, 180)
    # Object 1.
    Quartz.CGContextTranslateCTM(context, 20, 20)
    Quartz.CGContextSetFillColorWithColor(context, Utilities.getRGBOpaqueGreenColor())
    # Draw a green background.
    Quartz.CGContextFillRect(context, r)
    # Draw the colored logo.
    drawColoredLogo(context)

    # Object 2.
    Quartz.CGContextTranslateCTM(context, 300, 0)
    Quartz.CGContextSetFillColorWithColor(context, Utilities.getRGBOpaqueGreenColor())
    # Draw a green background.
    Quartz.CGContextFillRect(context, r)

    # Draw the rectangles with opacity 0.75.
    Quartz.CGContextSetAlpha(context, 0.75)

    drawColoredLogo(context)

    # Object 3.
    Quartz.CGContextTranslateCTM(context, 300, 0)
    # Set the alpha to 1.0 for drawing the background.
    Quartz.CGContextSetAlpha(context, 1.0)
    Quartz.CGContextSetFillColorWithColor(context, Utilities.getRGBOpaqueGreenColor())
    Quartz.CGContextFillRect(context, r)
    # Draw the rectangles with opacity 0.75.
    Quartz.CGContextSetAlpha(context, 0.75)
    # Begin a transparency layer. Drawing collected in
    # this transparency layer will be composited with an
    # alpha value of 0.75 when the transparency layer is ended.
    Quartz.CGContextBeginTransparencyLayer(context, None)
    if 1:
    # Draw the colored logo into the transparency layer.
        drawColoredLogo(context)

    # Ending the transparency layer causes the drawing
    # to then be composited with the global alpha value
    # in effect when CGContextBeginTransparencyLayer was called.
    Quartz.CGContextEndTransparencyLayer(context)

def shadowPDFDocument(context, url):
    pdfDoc = Quartz.CGPDFDocumentCreateWithURL(url)
    offset = Quartz.CGSize(-7, -7)

    if pdfDoc is None:
        print("Couldn't create PDF document reference!")
        return

    r = Quartz.CGPDFDocumentGetMediaBox(pdfDoc, 1)
    r.origin.x = 20
    r.origin.y = 20

    # Set the shadow.
    Quartz.CGContextSetShadow(context, scaleShadowOffset(offset), 3)

    # On Tiger and later, there is no need to use
    # a transparency layer to draw a PDF document as
    # a grouped object. On Panther, you can do so
    # by using a transparency layer. Drawing collected in
    # this transparency layer is drawn with the shadow
    # when the layer is ended.
    Quartz.CGContextBeginTransparencyLayer(context, None)
    if 1:
        Quartz.CGContextDrawPDFDocument(context, r, pdfDoc, 1)

    Quartz.CGContextEndTransparencyLayer(context)
