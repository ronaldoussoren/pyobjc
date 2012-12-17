"""
Add a watermark to all pages in a PDF document
"""
import sys, math, os

from Quartz import *
from Foundation import *

def usage(name):
    print >>sys.stderr, "Usage %s [inputfile]"%(name,)


class MyPDFData (object):
    pdfDoc = None
    mediaRect = None

# This is a simple function to create a CFURLRef from
# a path to a file. The path can be relative to the
# current directory or an absolute path.
def createURL(path):
    return CFURLCreateFromFileSystemRepresentation(None, path,
                            len(path), False)

# For the supplied URL and media box, create a PDF context
# that creates a PDF file at that URL and uses supplied rect
# as its document media box.
def myCreatePDFContext(url, mediaBox):
    dict = {}
    dict[kCGPDFContextCreator] = "PDF Stamper Application"

    pdfContext = CGPDFContextCreateWithURL(url, mediaBox, dict)
    return pdfContext

# For a URL corresponding to an existing PDF document on disk,
# create a CGPDFDocumentRef and obtain the media box of the first
# page.
def myCreatePDFSourceDocument(url):
    myPDFData = MyPDFData()
    myPDFData.pdfDoc = CGPDFDocumentCreateWithURL(url)
    if myPDFData.pdfDoc is not None:
        # NOTE: the original code uses CGPDFDocumentGetMediaBox, but that
        # API is deprecated and doesn't work in Leopard.
        page = CGPDFDocumentGetPage(myPDFData.pdfDoc, 1)
        myPDFData.mediaRect = CGPDFPageGetBoxRect(page, kCGPDFMediaBox)

        # Make the media rect origin at 0,0.
        myPDFData.mediaRect.origin.x = myPDFData.mediaRect.origin.y = 0.0

    return myPDFData

# Draw the source PDF document into the context and then draw the stamp PDF document
# on top of it. When drawing the stamp on top, place it along the diagonal from the lower
# left corner to the upper right corner and center its media rect to the center of that
# diagonal.
def StampWithPDFDocument(context,
                        sourcePDFDoc,
                        stampFileDoc, stampMediaRect):
    numPages = CGPDFDocumentGetNumberOfPages(sourcePDFDoc)

    # Loop over document pages and stamp each one appropriately.
    for i in range(1, numPages+1):
        # Use the page rectangle of each page from the source to compute
        # the destination media box for each page and the location of
        # the stamp.

        # NOTE: the original code uses CGPDFDocumentGetMediaBox, but that
        # API is deprecated and doesn't work in Leopard.
        page = CGPDFDocumentGetPage(sourcePDFDoc, i)
        pageRect = CGPDFPageGetBoxRect(page, kCGPDFMediaBox)

        CGContextBeginPage(context, pageRect)
        CGContextSaveGState(context)
        # Clip to the media box of the page.
        CGContextClipToRect(context, pageRect)
        # First draw the content of the source document.
        CGContextDrawPDFDocument(context, pageRect, sourcePDFDoc, i)
        # Translate to center of destination rect, that is the center of
        # the media box of content to draw on top of.
        CGContextTranslateCTM(context,
            pageRect.size.width/2, pageRect.size.height/2)
        # Compute angle of the diagonal across the destination page.
        angle = math.atan(pageRect.size.height/pageRect.size.width)
        # Rotate by an amount so that drawn content goes along a diagonal
        # axis across the page.
        CGContextRotateCTM(context, angle)
        # Move the origin so that the media box of the PDF to stamp
        # is centered around center point of destination.
        CGContextTranslateCTM(context,
            -stampMediaRect.size.width/2,
            -stampMediaRect.size.height/2)
        # Now draw the document to stamp with on top of original content.
        CGContextDrawPDFDocument(context, stampMediaRect,
            stampFileDoc, 1)
        CGContextRestoreGState(context)
        CGContextEndPage(context)

# From an input PDF document and a PDF document whose contents you
# want to draw on top of the other, create a new PDF document
# containing all the pages of the input document with the first page
# of the "stamping" overlayed.
def createStampedFileWithFile(inURL, stampURL, outURL):
    sourceFileData = myCreatePDFSourceDocument(inURL)
    if sourceFileData.pdfDoc is None:
        print >>sys.stderr, "Can't create PDFDocumentRef for source input file!"
        return

    stampFileData = myCreatePDFSourceDocument(stampURL)
    if stampFileData.pdfDoc is None:
        CGPDFDocumentRelease(sourceFileData.pdfDoc);
        print >>sys.stderr, "Can't create PDFDocumentRef for file to stamp with!"
        return

    pdfContext = myCreatePDFContext(outURL, sourceFileData.mediaRect)
    if pdfContext is None:
        print >>sys.stderr, "Can't create PDFContext for output file!"
        return

    StampWithPDFDocument(pdfContext, sourceFileData.pdfDoc,
            stampFileData.pdfDoc, stampFileData.mediaRect)

def main(args = None):
    if args is None:
        args = sys.argv

    suffix = ".watermarked.pdf";
    stampFileName = os.path.join(
            os.path.dirname(__file__), "confidential.pdf")

    if len(args) != 2:
        usage(args[0])
        return 1

    inputFileName = args[1];
    outputFileName = os.path.splitext(inputFileName)[0] + suffix

    inURL = createURL(inputFileName);
    if inURL is None:
        print >>sys.stderr, "Couldn't create URL for input file!"
        return 1

    outURL = createURL(outputFileName)
    if outURL is None:
        print >>sys.stderr, "Couldn't create URL for output file!"
        return 1

    stampURL = createURL(stampFileName)
    if stampURL is None:
        print >>sys.stderr, "Couldn't create URL for stamping file!"
        return 1

    createStampedFileWithFile(inURL, stampURL, outURL)
    return 0

if __name__ == "__main__":
    sys.exit(main())
