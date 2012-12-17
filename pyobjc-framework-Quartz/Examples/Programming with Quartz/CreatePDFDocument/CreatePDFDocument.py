from Quartz import *
import Quartz
import os, sys

# Return the generic RGB color space. This is a 'get' function and the caller
# should not release the returned value unless the caller retains it first.
# Usually callers of this routine will immediately use the returned colorspace
# with CoreGraphics so they typically do not need to retain it themselves.
# This function creates the generic RGB color space once and hangs onto it so
# it can return it whenever this function is called.

_genericRGBColorSpace = None
def getTheCalibratedRGBColorSpace():
    global _genericRGBColorSpace

    if _genericRGBColorSpace is None:
        _genericRGBColorSpace = CGColorSpaceCreateWithName(
            kCGColorSpaceGenericRGB)

    return _genericRGBColorSpace


def addURLAnnotationToPDFPage(c, rect):
    link = "http:#developer.apple.com/documentation/GraphicsImaging/"
    linkURL = CFURLCreateWithBytes(None, link, len(link),
                                            kCFStringEncodingUTF8, None)
    if linkURL is None:
        print >>sys.stderr, "Couldn't create url for link!"
        return

    CGPDFContextSetURLForRect(c, linkURL, rect)

def myCreatePDFDocumentAtURL(url):
    red = [1., 0., 0., 1.]

    # Make the media box the same size as the graphics this code draws.
    mediaBox = CGRectMake(0, 0, 200, 200)

    # Create a PDF context using mediaBox as the default media box for the
    # document. The document will be created at the location described by
    # the supplied URL. This example passes None for the auxiliaryInfo
    # dictionary.
    pdfContext = CGPDFContextCreateWithURL(url, mediaBox, None)
    if pdfContext is None:
        print >>sys.stderr, "Couldn't create PDF context!"
        return

    # Calling CGContextBeginPage indicates the following content is
    # to appear on the first page. The rect passed to this function
    # specifies the media box for this page.
    mediaBox = CGContextBeginPage(pdfContext, None)
    # It is good programming practice to bracket the drawing
    # you do on a page with saving and restoring the graphics
    # state.
    CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        CGContextSetFillColorSpace(pdfContext,
                                getTheCalibratedRGBColorSpace())
        CGContextSetFillColor(pdfContext, red)
        # Fill the rectangle of the media box with red.
        CGContextFillRect(pdfContext, mediaBox)

        # Add a link to a URL so that if you click
        # on the rect you will go to that URL.
        addURLAnnotationToPDFPage(pdfContext, mediaBox)
    CGContextRestoreGState(pdfContext)

    # Calling CGContextEndPage denotes the end of the first page.
    # You MUST call CGContextEndPage after each time you call
    # CGContextBeginPage and they should not be nested.
    CGContextEndPage(pdfContext)

    # You MUST release the PDF context when done with it. When the
    # retain count on the context reaches zero, Quartz flushes the
    # drawing content to the PDF file being created and closes it.
    CGContextRelease(pdfContext)

# This function returns a None CFStringRef if the password
# is greater than 32 bytes long or the string contains
# characters outside the range 32-127 inclusive.
def createPasswordString(password):

    # Check the length.
    if len(password) > 32:
        return None

    # Check that the byte codes are in the printable ASCII range.
    for ch in password:
        if not (32 <= ord(ch) <= 127):
            return None

    return CFStringCreateWithCString(None, password,
                                        kCFStringEncodingASCII)

def addEncryptionKeys(dict):
    ownerPassword = "test"
    ownerPasswordRef = None
    if dict is None:
        return

    ownerPasswordRef = createPasswordString(ownerPassword)
    if ownerPasswordRef == None:
        print >>sys.stderr,  "Invalid owner password %s!"%(ownerPassword,)
        return

    if hasattr(Quartz, 'kCGPDFContextOwnerPassword'):
        # Add the owner password.
        dict[kCGPDFContextOwnerPassword] = ownerPasswordRef

        # No user password supplied so Quartz will use the empty string.

        # Mark that printing is disallowed.
        dict[kCGPDFContextAllowsPrinting] = False

    else:
        print >>sys.stderr, "Encrypted PDF not available in this version of Mac OS X!"

def myCreate2PagePDFDocumentAtURL(url):
    red = [1., 0., 0., 1.]
    blue = [0., 0., 1., 1.]
    redPageName = u"com.mycompany.links.dg.redpage"
    bluePageName = u"com.mycompany.links.dg.bluepage"

    # Make the media box the same size as a US Letter size page.
    mediaBox = CGRectMake(0, 0, 612, 792)
    rectBox = CGRectMake(55, 55, 500, 680)
    # Create a point whose center is the center of rectBox.
    centerPoint = CGPoint(rectBox.origin.x + rectBox.size.width/2,
                                rectBox.origin.y + rectBox.size.height/2)

    auxiliaryInfo = {}
    addEncryptionKeys(auxiliaryInfo)
    pdfContext =  CGPDFContextCreateWithURL(url, mediaBox, auxiliaryInfo)

    if pdfContext is None:
        print >>sys.stderr, "Couldn't create PDF context!"
        return

    # Start the first page
    CGContextBeginPage(pdfContext, mediaBox)
    CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        CGContextSetFillColorSpace(pdfContext,
                                getTheCalibratedRGBColorSpace())
        CGContextSetFillColor(pdfContext, red)
        # Fill the rectangle of the media box with red.
        CGContextFillRect(pdfContext, rectBox)
        # Make a new named destination at the center of the rect being
        # painted. Here the code uses the name redPageName since
        # this is the "red" page that is being named.
        CGPDFContextAddDestinationAtPoint(pdfContext,
                        redPageName, centerPoint)
        # Make a link to a destination not yet created, that for
        # the "blue" page. Making this link is independent from
        # the creation of the destination above. Clicking
        # on this link in the generated PDF document navigates to
        # the destination referenced by bluePageName.
        CGPDFContextSetDestinationForRect(pdfContext, bluePageName,
                rectBox)
    CGContextRestoreGState(pdfContext)
    CGContextEndPage(pdfContext)

    # Start the second page.
    CGContextBeginPage(pdfContext, mediaBox)
    CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        CGContextSetFillColorSpace(pdfContext,
                                getTheCalibratedRGBColorSpace())
        CGContextSetFillColor(pdfContext, blue)
        # Fill the rectangle of the media box with blue.
        CGContextFillRect(pdfContext, rectBox)
        # Make a new named destination at the center of the rect
        # being painted. Here the code uses the name bluePageName
        # since this is the "blue" page that is being named. The link
        # on page 1 refers to this destination.
        CGPDFContextAddDestinationAtPoint(pdfContext,
                        bluePageName, centerPoint)
        # Make a link to a destination already created
        # for page 1, the red page. Clicking on this link
        # in the generated PDF document navigates to
        # the destination referenced by redPageName.
        CGPDFContextSetDestinationForRect(pdfContext, redPageName,
                rectBox)
    CGContextRestoreGState(pdfContext)
    CGContextEndPage(pdfContext)

    # You MUST release the PDF context when done with it. When the
    # retain count on the context reaches zero, Quartz flushes the
    # drawing content to the PDF file being created and closes it.
    del pdfContext

def main(args=None):
    if args is None:
        args = sys.argv

    path = "output.pdf"
    url = CFURLCreateFromFileSystemRepresentation(None, path, len(path), False)
    if url is None:
        print >>sys.stderr, "Couldn't create URL!"
        return 1

    myCreate2PagePDFDocumentAtURL(url)
    return 0

if __name__ == "__main__":
    sys.exit(main())
