from UIHandling import *
from Quartz import *
import math

kOurImageFile = "ptlobos.tif"

# For best performance make bytesPerRow a multiple of 16 bytes.
BEST_BYTE_ALIGNMENT = 16
def COMPUTE_BEST_BYTES_PER_ROW(bpr):
    return ((bpr + (BEST_BYTE_ALIGNMENT-1)) & ~(BEST_BYTE_ALIGNMENT-1))

def DEGREES_TO_RADIANS(degrees):
    return degrees * math.pi / 180

_colorSpace = None
def myGetGenericRGBSpace():
    global _colorSpace

    if _colorSpace is None:
        _colorSpace = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)

    return _colorSpace

_blue = None
def myGetBlueColor():
    global _blue

    if _blue is None:
        _blue = CGColorCreate(myGetGenericRGBSpace(), (0, 0, 1, 1))

    return _blue

_green = None
def myGetGreenColor():
    global _green

    if _green is None:
        _green = CGColorCreate(myGetGenericRGBSpace(), (0, 1, 0, 1))

    return _green

_red = None
def myGetRedColor():
    global _red

    if _red is None:
        _red = CGColorCreate(myGetGenericRGBSpace(), (1, 0, 0, 1))

    return _red

_ourImageURL = None
def doDrawImageFile(context, doclip):
    global _ourImageURL

    if _ourImageURL is None:
        mainBundle =  CFBundleGetMainBundle()
        if mainBundle:
            _ourImageURL = CFBundleCopyResourceURL(mainBundle, kOurImageFile, None, None)

        else:
            print "Can't get the app bundle!"

    if _ourImageURL:
        if doclip:
            clipImageToEllipse(context, _ourImageURL)
        else:
            drawCGImage(context, _ourImageURL)

    else:
        print "Couldn't create the URL for our Image file!"


def myDispatchDrawing(context, drawingType):
    if drawingType == kCommandStrokedAndFilledRects:
        drawStrokedAndFilledRects(context)

    elif drawingType == kCommandAlphaRects:
        drawAlphaRects(context)

    elif drawingType == kCommandSimpleClip:
        doDrawImageFile(context, True)

    elif drawingType == kCommandDrawImageFile:
        doDrawImageFile(context, False)

    elif drawingType == kCommandDoUncachedDrawing:
        drawUncachedForLayer(context)

    elif drawingType == kCommandDoCGLayer:
        drawSimpleCGLayer(context)

def drawStrokedAndFilledRects(context):
    ourRect = CGRectMake(40, 40, 130, 100)

    # Set the fill color to an opaque blue.
    CGContextSetFillColorWithColor(context, myGetBlueColor())
    # Fill the rect.
    CGContextFillRect(context, ourRect)

    # Set the stroke color to an opaque green.
    CGContextSetStrokeColorWithColor(context, myGetGreenColor())
    # Stroke the rect with a line width of 10 units.
    CGContextStrokeRectWithWidth(context, ourRect, 10)

    # Save the current graphics state.
    CGContextSaveGState(context)
    # Translate the coordinate system origin to the right
    # by 200 units.
    CGContextTranslateCTM(context, 200, 0)
    # Stroke the rect with a line width of 10 units.
    CGContextStrokeRectWithWidth(context, ourRect, 10)
    # Fill the rect.
    CGContextFillRect(context, ourRect)
    # Restore the graphics state to the previously saved
    # graphics state. This restores all graphics state
    # parameters to those in effect during the last call
    # to CGContextSaveGState. In this example that restores
    # the coordinate system to that in effect prior to the
    # call to CGContextTranslateCTM.
    CGContextRestoreGState(context)

#    Create a mutable path object that represents 'rect'.
#    Note that this is for demonstrating how to create a simple
#    CGPath object. The Quartz function CGPathAddRect would normally
#    be a better choice for adding a rect to a CGPath object.
def createRectPath(rect):
    path = CGPathCreateMutable()

    # Start a new subpath.
    CGPathMoveToPoint(path, None, rect.origin.x, rect.origin.y)

    # ***** Segment 1 *****
    CGPathAddLineToPoint(path, None,  rect.origin.x + rect.size.width, rect.origin.y)

    # ***** Segment 2 *****
    CGPathAddLineToPoint(path, None, rect.origin.x + rect.size.width,
                         rect.origin.y + rect.size.height)

    # ***** Segment 3 *****
    CGPathAddLineToPoint(path, None, rect.origin.x, rect.origin.y + rect.size.height)

    # ***** Segment 4 is created by closing the path *****
    CGPathCloseSubpath(path)

    return path


def drawAlphaRects(context):
    ourRect = CGRectMake(0, 0, 130, 100)
    numRects = 6
    rotateAngle = 2*math.pi/numRects
    tintAdjust = 1.0/numRects

    # Create the path object representing our rectangle. This
    # example is for demonstrating the use of a CGPath object.
    # For a simple rectangular shape, you'd typically use
    # CGContextFillRect or CGContextStrokeRect instead of this
    # approach.
    path = createRectPath(ourRect)

    # Move the origin of coordinates to a location that allows
    # the drawing to be within the window.
    CGContextTranslateCTM(context, 2*ourRect.size.width,
                           2*ourRect.size.height)

    # Set the fill color to a red color.
    CGContextSetFillColorWithColor(context, myGetRedColor())

    tint = 1.0
    while 0 < tint:
        # Set the global alpha to the tint value.
        CGContextSetAlpha(context, tint)

        # For a CGPath object that is a simple rect,
        # this is equivalent to CGContextFillRect.
        CGContextBeginPath(context)
        CGContextAddPath(context, path)
        CGContextFillPath(context)

        # These transformations are cummulative.
        CGContextRotateCTM(context, rotateAngle)

        tint -= tintAdjust

def drawCGImage(context, url):
    # Create a CGImageSource object from 'url'.
    imageSource = CGImageSourceCreateWithURL(url, None)

    # Create a CGImage object from the first image in the file. Image
    # indexes are 0 based.
    image = CGImageSourceCreateImageAtIndex(imageSource, 0, None)

    # Create a rectangle that has its origin at (100, 100) with the width
    # and height of the image itself.
    imageRect = CGRectMake(100, 100, CGImageGetWidth(image), CGImageGetHeight(image))

    # Draw the image into the rect.
    CGContextDrawImage(context, imageRect, image)

def clipImageToEllipse(context, url):
    # Create a CGImageSource object from 'url'.
    imageSource =  CGImageSourceCreateWithURL(url, None)

    # Create a CGImage object from the first image in the file. Image
    # indexes are 0 based.
    image = CGImageSourceCreateImageAtIndex( imageSource, 0, None )

    # Create a rectangle that has its origin at (100, 100) with the width
    # and height of the image itself.
    imageRect = CGRectMake(100, 100, CGImageGetWidth(image), CGImageGetHeight(image))

    CGContextBeginPath(context)
    # Create an elliptical path corresponding to the image width and height.
    CGContextAddEllipseInRect(context, imageRect)
    # Clip to the current path.
    CGContextClip(context)

    # Draw the image into the rect, clipped by the ellipse.
    CGContextDrawImage(context, imageRect, image)

def createRGBAImageFromQuartzDrawing(dpi, drawingCommand):
    # For generating RGBA data from drawing. Use a Letter size page as the
    # image dimensions. Typically this size would be the minimum necessary to
    # capture the drawing of interest. We want 8 bits per component and for
    # RGBA data there are 4 components.
    width = 8.5*dpi
    height = 11*dpi
    bitsPerComponent = 8
    numComps = 4
    # Compute the minimum number of bytes in a given scanline.
    bytesPerRow = width* bitsPerComponent/8 * numComps

    # This bitmapInfo value specifies that we want the format where alpha is
    # premultiplied and is the last of the components. We use this to produce
    # RGBA data.
    bitmapInfo = kCGImageAlphaPremultipliedLast

    # Round to nearest multiple of BEST_BYTE_ALIGNMENT for optimal performance.
    bytesPerRow = COMPUTE_BEST_BYTES_PER_ROW(bytesPerRow)

    # Allocate the data for the bitmap.
    data = array.array('c', '\0' * bytesPerRow * height)

    # Create the bitmap context. Characterize the bitmap data with the
    # Generic RGB color space.
    bitmapContext = CGBitmapContextCreate(
                    data, width, height, bitsPerComponent, bytesPerRow,
                    myGetGenericRGBSpace(), bitmapInfo)

    # Clear the destination bitmap so that it is completely transparent before
    # performing any drawing. This is appropriate for exporting PNG data or
    # other data formats that capture alpha data. If the destination output
    # format doesn't support alpha then a better choice would be to paint
    # to white.
    CGContextClearRect(bitmapContext, CGRectMake(0, 0, width, height))

    # Scale the coordinate system so that 72 units are dpi pixels.
    CGContextScaleCTM(bitmapContext, dpi/72, dpi/72)

    # Perform the requested drawing.
    myDispatchDrawing(bitmapContext, drawingCommand)

    # Create a CGImage object from the drawing performed to the bitmapContext.
    image = CGBitmapContextCreateImage(bitmapContext)

    # Return the CGImage object this code created from the drawing.
    return image

def  myExportCGDrawingAsPNG(url, drawingCommand):
    dpi = 300
    # Create an RGBA image from the Quartz drawing that corresponds to drawingCommand.
    image = createRGBAImageFromQuartzDrawing(dpi, drawingCommand)

    # Create a CGImageDestination object will write PNG data to URL.
    # We specify that this object will hold 1 image.
    imageDestination = CGImageDestinationCreateWithURL(url, kUTTypePNG, 1, None)

    properties = {
            kCGImagePropertyDPIWidth: dpi,
            kCGImagePropertyDPIHeight: dpi,
    }

    # Add the image to the destination, characterizing the image with
    # the properties dictionary.
    CGImageDestinationAddImage(imageDestination, image, properties)

    # When all the images (only 1 in this example) are added to the destination,
    # finalize the CGImageDestination object.
    CGImageDestinationFinalize(imageDestination)


def createCachedContent(c):
    # The cached content will be 50x50 units.
    width = height = 50

    # Create the layer to draw into.
    layer = CGLayerCreateWithContext(c,  CGSizeMake(width, height), None)

    # Get the CG context corresponding to the layer.
    layerContext = CGLayerGetContext(layer)

    # Cache some very simple drawing just as an example.
    CGContextFillRect(layerContext, CGRectMake(0, 0, width, height) )

    # The layer now contains cached drawing so return it.
    return layer

def drawSimpleCGLayer(context):
    # Create a CGLayer object that represents some drawing.
    layer = createCachedContent(context)

    # Get the size of the layer created.
    s = CGLayerGetSize(layer);

    # Position the drawing to an appropriate location.
    CGContextTranslateCTM(context, 40, 100)

    # Paint 4 columns of layer objects.
    for i in range(4):
        # Draw the layer at the point that varies as the code loops.
        CGContextDrawLayerAtPoint(context,
                            CGPointMake(2*(i+1)*s.width, 0),
                            layer)

# The equivalent drawing as doSimpleCGLayer but without creating
# a CGLayer object and caching that drawing to a layer.
def drawUncachedForLayer(context):
    r = CGRectMake(0, 0, 50, 50)

    CGContextTranslateCTM(context, 40, 100)

    for i in range(4):
        # Adjust the origin as the code loops. Recall that
        # transformations are cummulative.
        CGContextTranslateCTM( context, 2*CGRectGetWidth(r), 0 )
        CGContextFillRect(context, r) # Do the uncached drawing.

# Create a PDF document at 'url' from the drawing represented by drawingCommand.
def myCreatePDFDocument(url, drawingCommand):
    # mediaRect represents the media box for the PDF document the code is
    # creating. The size here is that of a US Letter size sheet.
    mediaRect = CGRectMake(0, 0, 8.5*72, 11*72)

    # Create a CGContext object to capture the drawing as a PDF document located
    # at 'url'.
    pdfContext, mediaRect = CGPDFContextCreateWithURL(url, mediaRect, None)

    # Start capturing drawing on a page.
    mediaRect = CGContextBeginPage(pdfContext, mediaRect)

    # Perform drawing for the first page.
    myDispatchDrawing(pdfContext, drawingCommand)

    # Tell the PDF context that drawing for the current page is finished.
    CGContextEndPage(pdfContext)

    # If there were more pages they would be captured as:
    #
    #    mediaRect = CGContextBeginPage(pdfContext, None)
    #
    #   DrawingForPage2(pdfContext)
    #
    #   CGContextEndPage(pdfContext)
    #
    #   mediaRect = CGContextBeginPage(pdfContext, None)
    #
