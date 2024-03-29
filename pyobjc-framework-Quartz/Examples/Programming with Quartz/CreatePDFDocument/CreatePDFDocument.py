import sys

import Cocoa
import Quartz

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
        _genericRGBColorSpace = Quartz.CGColorSpaceCreateWithName(
            Quartz.kCGColorSpaceGenericRGB
        )

    return _genericRGBColorSpace


def addURLAnnotationToPDFPage(c, rect):
    link = "http:#developer.apple.com/documentation/GraphicsImaging/"
    linkURL = Cocoa.CFURLCreateWithBytes(
        None, link, len(link), Cocoa.kCFStringEncodingUTF8, None
    )
    if linkURL is None:
        print("Couldn't create url for link!")
        return

    Quartz.CGPDFContextSetURLForRect(c, linkURL, rect)


def myCreatePDFDocumentAtURL(url):
    red = [1.0, 0.0, 0.0, 1.0]

    # Make the media box the same size as the graphics this code draws.
    mediaBox = Quartz.CGRectMake(0, 0, 200, 200)

    # Create a PDF context using mediaBox as the default media box for the
    # document. The document will be created at the location described by
    # the supplied URL. This example passes None for the auxiliaryInfo
    # dictionary.
    pdfContext = Quartz.CGPDFContextCreateWithURL(url, mediaBox, None)
    if pdfContext is None:
        print("Couldn't create PDF context!")
        return

    # Calling CGContextBeginPage indicates the following content is
    # to appear on the first page. The rect passed to this function
    # specifies the media box for this page.
    mediaBox = Quartz.CGContextBeginPage(pdfContext, None)
    # It is good programming practice to bracket the drawing
    # you do on a page with saving and restoring the graphics
    # state.
    Quartz.CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        Quartz.CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        Quartz.CGContextSetFillColorSpace(pdfContext, getTheCalibratedRGBColorSpace())
        Quartz.CGContextSetFillColor(pdfContext, red)
        # Fill the rectangle of the media box with red.
        Quartz.CGContextFillRect(pdfContext, mediaBox)

        # Add a link to a URL so that if you click
        # on the rect you will go to that URL.
        addURLAnnotationToPDFPage(pdfContext, mediaBox)
    Quartz.CGContextRestoreGState(pdfContext)

    # Calling CGContextEndPage denotes the end of the first page.
    # You MUST call CGContextEndPage after each time you call
    # CGContextBeginPage and they should not be nested.
    Quartz.CGContextEndPage(pdfContext)

    # You MUST release the PDF context when done with it. When the
    # retain count on the context reaches zero, Quartz flushes the
    # drawing content to the PDF file being created and closes it.
    Quartz.CGContextRelease(pdfContext)


# This function returns a None CFStringRef if the password
# is greater than 32 bytes long or the string contains
# characters outside the range 32-127 inclusive.
def createPasswordString(password):
    if not isinstance(password, bytes):
        password = password.encode("utf-8")

    # Check the length.
    if len(password) > 32:
        return None

    # Check that the byte codes are in the printable ASCII range.
    for ch in password:
        if not (32 <= (ord(ch) if sys.version_info[0] == 2 else ch) <= 127):
            return None

    return Cocoa.CFStringCreateWithCString(None, password, Cocoa.kCFStringEncodingASCII)


def addEncryptionKeys(info_dict):
    ownerPassword = "test"
    ownerPasswordRef = None
    if info_dict is None:
        return

    ownerPasswordRef = createPasswordString(ownerPassword)
    if ownerPasswordRef is None:
        print(f"Invalid owner password {ownerPassword}!")
        return

    if hasattr(Quartz, "kCGPDFContextOwnerPassword"):
        # Add the owner password.
        info_dict[Quartz.kCGPDFContextOwnerPassword] = ownerPasswordRef

        # No user password supplied so Quartz will use the empty string.

        # Mark that printing is disallowed.
        info_dict[Quartz.kCGPDFContextAllowsPrinting] = False

    else:
        print("Encrypted PDF not available in this version of macOS!")


def myCreate2PagePDFDocumentAtURL(url):
    red = [1.0, 0.0, 0.0, 1.0]
    blue = [0.0, 0.0, 1.0, 1.0]
    redPageName = "com.mycompany.links.dg.redpage"
    bluePageName = "com.mycompany.links.dg.bluepage"

    # Make the media box the same size as a US Letter size page.
    mediaBox = Quartz.CGRectMake(0, 0, 612, 792)
    rectBox = Quartz.CGRectMake(55, 55, 500, 680)
    # Create a point whose center is the center of rectBox.
    centerPoint = Quartz.CGPoint(
        rectBox.origin.x + rectBox.size.width / 2,
        rectBox.origin.y + rectBox.size.height / 2,
    )

    auxiliaryInfo = {}
    addEncryptionKeys(auxiliaryInfo)
    pdfContext = Quartz.CGPDFContextCreateWithURL(url, mediaBox, auxiliaryInfo)

    if pdfContext is None:
        print("Couldn't create PDF context!")
        return

    # Start the first page
    Quartz.CGContextBeginPage(pdfContext, mediaBox)
    Quartz.CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        Quartz.CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        Quartz.CGContextSetFillColorSpace(pdfContext, getTheCalibratedRGBColorSpace())
        Quartz.CGContextSetFillColor(pdfContext, red)
        # Fill the rectangle of the media box with red.
        Quartz.CGContextFillRect(pdfContext, rectBox)
        # Make a new named destination at the center of the rect being
        # painted. Here the code uses the name redPageName since
        # this is the "red" page that is being named.
        Quartz.CGPDFContextAddDestinationAtPoint(pdfContext, redPageName, centerPoint)
        # Make a link to a destination not yet created, that for
        # the "blue" page. Making this link is independent from
        # the creation of the destination above. Clicking
        # on this link in the generated PDF document navigates to
        # the destination referenced by bluePageName.
        Quartz.CGPDFContextSetDestinationForRect(pdfContext, bluePageName, rectBox)
    Quartz.CGContextRestoreGState(pdfContext)
    Quartz.CGContextEndPage(pdfContext)

    # Start the second page.
    Quartz.CGContextBeginPage(pdfContext, mediaBox)
    Quartz.CGContextSaveGState(pdfContext)
    if 1:
        # Clip to the media box.
        Quartz.CGContextClipToRect(pdfContext, mediaBox)
        # Set the fill color and color space.
        Quartz.CGContextSetFillColorSpace(pdfContext, getTheCalibratedRGBColorSpace())
        Quartz.CGContextSetFillColor(pdfContext, blue)
        # Fill the rectangle of the media box with blue.
        Quartz.CGContextFillRect(pdfContext, rectBox)
        # Make a new named destination at the center of the rect
        # being painted. Here the code uses the name bluePageName
        # since this is the "blue" page that is being named. The link
        # on page 1 refers to this destination.
        Quartz.CGPDFContextAddDestinationAtPoint(pdfContext, bluePageName, centerPoint)
        # Make a link to a destination already created
        # for page 1, the red page. Clicking on this link
        # in the generated PDF document navigates to
        # the destination referenced by redPageName.
        Quartz.CGPDFContextSetDestinationForRect(pdfContext, redPageName, rectBox)
    Quartz.CGContextRestoreGState(pdfContext)
    Quartz.CGContextEndPage(pdfContext)

    # You MUST release the PDF context when done with it. When the
    # retain count on the context reaches zero, Quartz flushes the
    # drawing content to the PDF file being created and closes it.
    del pdfContext


def main(args=None):
    if args is None:
        args = sys.argv

    path = b"output.pdf"
    url = Cocoa.CFURLCreateFromFileSystemRepresentation(None, path, len(path), False)
    if url is None:
        print("Couldn't create URL!")
        return 1

    myCreate2PagePDFDocumentAtURL(url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
