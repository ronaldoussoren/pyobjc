from Quartz import *
import Quartz
import objc

import Utilities
import BitmapContext

import sys

# We're using a function that isn't made available through a wrapper, just
# load it manually:
if not hasattr(Quartz, 'PMCGImageCreateWithEPSDataProvider'):
    functions = [
        ('PMCGImageCreateWithEPSDataProvider', '@@@'),
    ]
    import AppKit
    d = {}
    objc.loadBundleFunctions(AppKit.__bundle__, d, functions)

    if 'PMCGImageCreateWithEPSDataProvider' in d:
        PMCGImageCreateWithEPSDataProvider=d['PMCGImageCreateWithEPSDataProvider']
    else:
        print >>sys.stderr, "PMCGImageCreateWithEPSDataProvider doesn't exist"

def getEPSBBox(epspath):
    try:
        fp = open(epspath, 'rU')
    except IOError, msg:
        return CGRectZero

    try:
        #  This is a VERY poor man's EPS DSC parser, here just so that
        #  this sample code can handle simple EPS files. It is
        #  simple but very inefficient. In addition it does not ensure
        #  that the DSC comments are at the beginning of a line,
        #  nor does it handle (atend) style comments at all.
        #  It will simply find the first occurance of a
        #  %%BoundingBox comment and if it is of the typical
        # form, it will obtain the bounding box data.
        #
        for ln in fp:
            if ln.startswith("%%BoundingBox:"):
                fields = ln.split()[1:]
                if len(fields) >= 4:
                    llx = int(fields[0])
                    lly = int(fields[1])
                    urx = int(fields[2])
                    ury = int(fields[3])
                    return CGRectMake(llx, lly, urx - llx, ury - lly)
    finally:
        fp.close()

    return CGRectZero

def createEPSPreviewImage(url):
    # The CGImage used as the preview needs to have the
    # same width and height as the EPS data it will
    # be associated with. This sample code doesn't attempt
    # to use any preview image associated with the EPS
    # data but instead simply draws a box of an appropriate
    # size. Your code would most likely create an image
    # that reflects a PICT or TIFF preview present in the
    # EPS data.
    result, path = CFURLGetFileSystemRepresentation(url, True, None, 1024)
    if not result:
        print >>sys.stderr, "Couldn't get the path for EPS file!"
        return None

    path = path.rstrip('\0')

    epsRect = getEPSBBox(path)
    # Check whether the EPS bounding box is empty.
    if epsRect == CGRectZero:
        print >>sys.stderr, "Couldn't find BoundingBox comment!"
        return None

    wantDisplayColorSpace = False
    needsTransparentBitmap = True
    # Create a bitmap context to draw to in order to
    # create the preview image. Use the routine
    # createRGBBitmapContext from the earlier chapter.
    bitmapContext = BitmapContext.createRGBBitmapContext(
                                    epsRect.size.width,
                                    epsRect.size.height,
                                    wantDisplayColorSpace,
                                    needsTransparentBitmap)
    if bitmapContext is None:
        print >>sys.stderr, "Couldn't create bitmap context"
        return None

    epsRect.origin.x = epsRect.origin.y = 0
    # Draw the contents of the preview. The preview consists
    # of two lines and a stroke around the bounding box. One
    # of the two lines is drawn from the lower-left corner to
    # the upper-right corner of the bounding box and the other
    # line is from the lower-right corner to the upper-left
    # corner of the bounding box.
    CGContextBeginPath(bitmapContext)
    CGContextMoveToPoint(bitmapContext, 0, 0)
    CGContextAddLineToPoint(bitmapContext, epsRect.size.width, epsRect.size.height)
    CGContextMoveToPoint(bitmapContext, epsRect.size.width, 0)
    CGContextAddLineToPoint(bitmapContext, 0, epsRect.size.height)
    CGContextStrokePath(bitmapContext)
    # Stroke the bounding rectangle, inset so that the stroke is
    # completely contained in the EPS bounding rect.
    CGContextStrokeRect(bitmapContext, CGRectInset(epsRect, 0.5, 0.5))

    # Now create an image from the bitmap raster data. This image
    # has a data provider that releases the image raster data when
    # the image is released. Use the createImageFromBitmapContext
    # from Chapter 12. Calling createImageFromBitmapContext
    # gives up ownership of the raster data used by the context.
    epsPreviewImage = BitmapContext.createImageFromBitmapContext(bitmapContext)

    if epsPreviewImage is None:
        print >>sys.stderr, "Couldn't create preview image!"
        return None

    return epsPreviewImage

# This technique of handling EPS data is available in
# Mac OS X v10.1 and later and is one alternative method
# of supporting EPS data during printing as compared to
# converting EPS data to PDF data using CGPSConverter which
# is only available in Panther and later.
def createCGEPSImage(url):
    previewImage = createEPSPreviewImage(url)
    if previewImage is None:
        print >>sys.stderr, "Couldn't create EPS preview!"
        return None

    # It is important that the data provider supplying the
    # EPS data conform to the Quartz guidelines for data providers
    # and is able to provide the data until the data releaser function
    # is called. If you have a custom data provider, you need
    # to follow these guidelines since your data provider
    # is not necessarily called before you release the image
    # that uses the provider.
    epsDataProvider = CGDataProviderCreateWithURL(url)
    if epsDataProvider is None:
        print >>sys.stderr, "Couldn't create EPS data provider!"
        return None

    # Create the hybrid CGImage that contains the preview image
    # and the EPS data. Note that the data provider isn't
    # called during image creation but at some later point in time.


    epsImage = PMCGImageCreateWithEPSDataProvider(epsDataProvider, previewImage)
    # The preview image and data provider are no longer needed
    # because Quartz retains them and this code doesn't
    # require them further.
    del previewImage
    del epsDataProvider

    if epsImage is None:
        print >>sys.stderr, "Couldn't create EPS hybrid image!"
        return None

    return epsImage

def drawEPSDataImage(context, url):
    # Create the a CGImage that has EPS data associated with it.
    epsDataImage = createCGEPSImage(url)
    if epsDataImage is None:
        return

    # Create a destination rectangle at the location
    # to draw the EPS document. The size of the rect is scaled
    # down to 1/2 the size of the EPS graphic.
    destinationRect = CGRectMake(100, 100,
                        CGImageGetWidth(epsDataImage),
                        CGImageGetHeight(epsDataImage))
    # Draw the image to the destination. When the EPS
    # data associated with the image is sent to a PostScript
    # printer, the EPS bounding box is mapped to this
    # destination rectangle, translated and scaled as necessary.
    CGContextDrawImage(context, destinationRect, epsDataImage)

    # Draw the image a second time. This time the image is
    # rotated by 45 degrees and scaled by an additional scaling factor
    # of 0.5 in the x dimension. The center point of this image coincides
    # with the center point of the earlier drawing.
    CGContextTranslateCTM(context,
            destinationRect.origin.x + destinationRect.size.width/2,
            destinationRect.origin.y + destinationRect.size.height/2)
    CGContextRotateCTM(context, Utilities.DEGREES_TO_RADIANS(45))
    CGContextScaleCTM(context, 0.5, 1)
    CGContextTranslateCTM(context,
            -(destinationRect.origin.x + destinationRect.size.width/2),
            -(destinationRect.origin.y + destinationRect.size.height/2) )
    CGContextDrawImage(context, destinationRect, epsDataImage)
