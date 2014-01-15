"""
Parse a PDF file and print some information about it.

Usage:
    python parse_page_contents.py inputfile ...
"""
from __future__ import print_function
import objc
import sys
import array

import Quartz
import Cocoa

class MyDataScan (object):
    def __init__(self):
        self.numImagesWithColorThisPage = 0
        self.numImageMasksThisPage = 0
        self.numImagesMaskedWithMaskThisPage = 0
        self.numImagesMaskedWithColorsThisPage = 0

def printPageResults(outFile, myData, pageNum):
    if myData.numImagesWithColorThisPage:
        print("Found %d images with intrinsic color on page %d."%(
                myData.numImagesWithColorThisPage, pageNum), file=outFile)

    if myData.numImageMasksThisPage:
        print("Found %d image masks on page %d."%(
                    myData.numImageMasksThisPage,
                    pageNum), file=outFile)

    if myData.numImagesMaskedWithMaskThisPage:
        print("Found %d images masked with masks on page %d."%(
                    myData.numImagesMaskedWithMaskThisPage,
                    pageNum), file=outFile)

    if myData.numImagesMaskedWithColorsThisPage:
        print("Found %d images masked with colors on page %d."%(
                    myData.numImagesMaskedWithColorsThisPage,
                    pageNum), file=outFile)

def printDocResults(outFile, totPages, totImages):
    print('', file=outFile)
    print("Summary: %d page document contains %d images."%(
                        totPages, totImages), file=outFile)
    print('', file=outFile)


def checkImageType(imageDict, myScanData):
    hasMaskKey, isMask = Quartz.CGPDFDictionaryGetBoolean(imageDict, "ImageMask", None);
    if not hasMaskKey:
        hasMaskKey, isMask = Quartz.CGPDFDictionaryGetBoolean(imageDict, "IM", None);

    if hasMaskKey and isMask:
        myScanData.numImageMasksThisPage += 1
        return

    # If image is masked with an alpha image it has an SMask entry.
    hasSMaskKey, object = Quartz.CGPDFDictionaryGetObject(imageDict, "SMask", None)
    if hasSMaskKey:
        # This object must be an XObject that is an image.
        # This code assumes the PDF is well formed in this regard.
        myScanData.numImagesMaskedWithMaskThisPage += 1
        return

    # If this image is masked with an image or with colors it has
    # a Mask entry.
    hasMask, object = Quartz.CGPDFDictionaryGetObject(imageDict, "Mask", None)
    if hasMask:
        # If the object is an XObject then the mask is an image.
        # If it is an array, the mask is an array of colors.
        type = Quartz.CGPDFObjectGetType(object)
        # Check if it is a stream type which it must be to be an XObject.
        if type == Quartz.kCGPDFObjectTypeStream:
            myScanData.numImagesMaskedWithMaskThisPage += 1
        elif type == Quartz.kCGPDFObjectTypeArray:
            myScanData.numImagesMaskedWithColorsThisPage += 1
        else:
            print("Mask entry in Image object is not well formed!")

        return

    # This image is not a mask, is not masked with another image or
    # color so it must be an image with intrinsic color with no mask.
    myScanData.numImagesWithColorThisPage += 1

#       The "Do" operator consumes one value off the stack, the name of
#       the object to execute. The name is a resource in the resource
#       dictionary of the page and the object corresponding to that name
#       is an XObject. The most common types of XObjects are either
#       Form objects or Image objects. This code only counts images.
#
#       Note that forms, patterns, and potentially other resources contain
#       images. This code only counts the top level images in a PDF document,
#       not images embedded in other resources.
@objc.callbackFor(Quartz.CGPDFOperatorTableSetCallback)
def myOperator_Do(s, info):
    # Check to see if this is an image or not.
    cs = Quartz.CGPDFScannerGetContentStream(s)

    # The Do operator takes a name. Pop the name off the
    # stack. If this fails then the argument to the
    # Do operator is not a name and is therefore invalid!
    res, name = Quartz.CGPDFScannerPopName(s, None)
    if not res:
        print("Couldn't pop name off stack!")
        return

    # Get the resource with type "XObject" and the name
    # obtained from the stack.
    xobject = Quartz.CGPDFContentStreamGetResource(cs, "XObject", name);
    if xobject is None:
        print("Couldn't get XObject with name %s"%(name,))
        return

    # An XObject must be a stream so obtain the value from the xobject
    # as if it were a stream. If this fails, the PDF is malformed.
    res, stream = Quartz.CGPDFObjectGetValue(xobject, Quartz.kCGPDFObjectTypeStream, None)
    if not res:
        print("XObject '%s' is not a stream"%(name,))
        return

    print(stream)

    # Streams consist of a dictionary and the data associated
    # with the stream. This code only cares about the dictionary.
    dict = Quartz.CGPDFStreamGetDictionary(stream);
    if dict is None:
        print("Couldn't obtain dictionary from stream %s!"%(name,))
        return

    # An XObject dict has a Subtype that indicates what kind it is.
    res, name = Quartz.CGPDFDictionaryGetName(dict, "Subtype", None)
    if not res:
        print("Couldn't get SubType of dictionary object!")
        return

    # This code is interested in the "Image" Subtype of an XObject.
    # Check whether this object has Subtype of "Image".
    if name != "Image":
        # The Subtype is not "Image" so this must be a form
        # or other type of XObject.
        return


    # This is an Image so figure out what variety of image it is.
    checkImageType(dict, info)

# This callback handles inline images. Inline images end with the
# "EI" operator.
@objc.callbackFor(Quartz.CGPDFOperatorTableSetCallback)
def myOperator_EI(s, info):
    print("EI")
    # When the scanner encounters the EI operator, it has a
    # stream corresponding to the image on the operand stack.
    # This code pops the stream off the stack in order to
    # examine it.
    res, stream = Quartz.CGPDFScannerPopStream(s, None)
    if not res:
        print("Couldn't create stream from inline image")
        return

    # Get the image dictionary from the stream.
    dict = Quartz.CGPDFStreamGetDictionary(stream);
    if dict is None:
        print("Couldn't get dict from inline image stream!")
        return

    # By definition the stream passed to EI is an image so
    # pass it to the code to check the type of image.
    checkImageType(dict, info)

def createMyOperatorTable():
    myTable = Quartz.CGPDFOperatorTableCreate()
    Quartz.CGPDFOperatorTableSetCallback(myTable, b"Do", myOperator_Do)
    Quartz.CGPDFOperatorTableSetCallback(myTable, b"EI", myOperator_EI)
    return myTable

def dumpPageStreams(url, outFile):
    # Create a CGPDFDocumentRef from the input PDF file.
    pdfDoc = Quartz.CGPDFDocumentCreateWithURL(url);
    if pdfDoc is None:
        print("Couldn't open PDF document!")
        return

    # Create the operator table with the needed callbacks.
    table = createMyOperatorTable();
    if table is None:
        print("Couldn't create operator table!")
        return

    # Initialize the count of the images.
    totalImages = 0

    # Obtain the total number of pages for the document.
    totPages = Quartz.CGPDFDocumentGetNumberOfPages(pdfDoc)

    # Loop over all the pages in the document, scanning the
    # content stream of each one.
    for i in range(1, totPages+1):
        # Get the PDF page for this page in the document.
        p = Quartz.CGPDFDocumentGetPage(pdfDoc, i)

        # Create a reference to the content stream for this page.
        cs = Quartz.CGPDFContentStreamCreateWithPage(p)

        if cs is None:
            print("Couldn't create content stream for page #%d"%(i,))
            return

        # Initialize the counters of images for this page.
        myData = MyDataScan()

        # Create a scanner for this PDF document page.
        scanner = Quartz.CGPDFScannerCreate(cs, table, 0);
        if scanner is None:
            print("Couldn't create scanner for page #%d!"%(i,))
            return


        # CGPDFScannerScan causes Quartz to scan the content stream,
        # calling the callbacks in the table when the corresponding
        # operator is encountered. Once the content stream for the
        # page has been consumed or Quartz detects a malformed
        # content stream, CGPDFScannerScan returns.
        if not Quartz.CGPDFScannerScan(scanner):
            print("Scanner couldn't scan all of page #%d!"%(i,))

        # Print the results for this page.
        printPageResults(outFile, myData, i);

        # Update the total count of images with the count of the
        # images on this page.
        totalImages += (
                myData.numImagesWithColorThisPage +
                myData.numImageMasksThisPage +
                myData.numImagesMaskedWithMaskThisPage +
                myData.numImagesMaskedWithColorsThisPage)

        # Once the page has been scanned, release the
        # scanner for this page.
        Quartz.CGPDFScannerRelease(scanner)
        # Release the content stream for this page.
        Quartz.CGPDFContentStreamRelease(cs)
        # Done with this page; loop to next page.

    printDocResults(outFile, totPages, totalImages)

def main(args = None):
    if args is None:
        args = sys.argv

    if len(args) < 2:
        print("Usage: %s inputfile ... "%(args[0],))
        return 1

    for inputFileName in args[1:]:
        print("Beginning Document %r"%(inputFileName,))

        if not isinstance(inputFileName, bytes):
            inputFileName = inputFileName.encode('utf-8')

        inURL = Cocoa.CFURLCreateFromFileSystemRepresentation(None, inputFileName,
                                len(inputFileName), False)
        if inURL is None:
            print("Couldn't create URL for input file!")
            return 1

        dumpPageStreams(inURL, sys.stdout)

    return 0

if __name__ == "__main__":
    sys.exit(main())
