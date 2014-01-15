import AppDrawing
import FrameworkUtilities
import Utilities
import DataProvidersAndConsumers
import Cocoa
import Quartz

import sys

def createNewPDFRefFromPasteBoard():
    # Create a reference to the PDF data on the pasteboard.
    # The implementation of myCreatePDFDataFromPasteBoard depends
    # on the application framework you are using for your application.
    #
    # myCreatePDFDataFromPasteBoard creates a reference that is owned
    # by the calling application.
    pasteBoardData = FrameworkUtilities.myCreatePDFDataFromPasteBoard()

    if pasteBoardData is None:
        print("There is no PDF data on pasteboard!")
        return None

    # Create a data provider from the pasteboard data.
    dataProvider = myCGDataProviderCreateWithCFData(pasteBoardData)
    # Release the pasteboard data since the data provider retains
    # it and this code owns a reference but no longer requires it.
    del pasteBoardData

    if dataProvider is None:
        print("Couldn't create data provider.")
        return None

    pasteBoardPDFDocument = Quartz.CGPDFDocumentCreateWithProvider(dataProvider)
    # Release the data provider now that the code is done with it.
    del dataProvider

    if pasteBoardPDFDocument is None:
        print("Couldn't create PDF document from pasteboard data provider.")
        return None
    return pasteBoardPDFDocument

_pdfDoc = None
def getPasteBoardPDFDoc(reset):
    global _pdfDoc
    if reset:
        # Release any existing document.
        _pdfDoc = createNewPDFRefFromPasteBoard()
    else:
        # If there isn't already one, create it fresh.
        if _pdfDoc is None:
            _pdfDoc = createNewPDFRefFromPasteBoard()
    return _pdfDoc


def drawPasteBoardPDF(context):
    pdfDoc = getPasteBoardPDFDoc(False)   # Obtain the existing one.
    if pdfDoc is None:
        print("Quartz couldn't create CGPDFDocumentRef from pasteboard.")
        return

    # The media box is the bounding box of the PDF document.
    pdfRect = Quartz.CGPDFDocumentGetMediaBox(pdfDoc , 1);   # page 1
    # Make the destination rect origin at the Quartz origin.
    pdfRect.origin.x = pdfRect.origin.y = 0.;
    Quartz.CGContextDrawPDFDocument(context, pdfRect, pdfDoc, 1);  # page 1

def cfDataCreatePDFDocumentFromCommand( command):
    # Media rect for the drawing. In a real application this
    # should be the bounding rectangle of the graphics
    # that will be the PDF content.
    mediaRect = Quartz.CGRectMake(0, 0, 612, 792)

    # Create a dictionary to hold the optional information describing the PDF data.
    dict = {}

    # Add the creator and title information to the PDF content.
    dict[Quartz.kCGPDFContextTitle] = "Pasted From Sample Quartz Application"
    dict[Quartz.kCGPDFContextCreator] = "Sample Quartz Application"

    # Create a mutable CFData object with unlimited capacity.
    data = Cocoa.CFDataCreateMutable(None, 0)
    if data is None:
        print("Couldn't make CFData!")
        return None

    # Create the data consumer to capture the PDF data.
    consumer = DataProvidersAndConsumers.myCGDataConsumerCreateWithCFData(data)
    if consumer is None:
        print("Couldn't create data consumer!")
        return None

    pdfContext, mediaRect = Quartz.CGPDFContextCreate(consumer, None, dict)
    del consumer
    del dict

    if pdfContext is None:
        print("Couldn't create pdf context!")
        return None

    mediaRect = Quartz.CGContextBeginPage(pdfContext)
    if 1:
        Quartz.CGContextSaveGState(pdfContext)
        if 1:
            Quartz.CGContextClipToRect(pdfContext, mediaRect)
            AppDrawing.DispatchDrawing(pdfContext, command)
        Quartz.CGContextRestoreGState(pdfContext)
    Quartz.CGContextEndPage(pdfContext)

    return data

def MakePDFDocument(url, exportInfo):
    # Use this as the media box for the document.
    # In a real application this should be the bounding
    # rectangle of the graphics that will be the PDF content.
    mediaRect = Quartz.CGRectMake(0, 0, 612, 792)

    info = {
        # Add the title information for this document.
        Quartz.kCGPDFContextTitle: "BasicDrawing Sample Graphics",

        # Add the author information for this document. This is typically
        # the user creating the document.
        Quartz.kCGPDFContextAuthor: "David Gelphman and Bunny Laden",

        # The creator is the application creating the document.
        Quartz.kCGPDFContextCreator: "BasicDrawing Application",
    }

    if 0:
        # Before using the kCGPDFContextCropBox key, check to ensure that it
        # is available.
        if hasattr(Quartz, 'kCFPDFContextCropBox'):
            # Prepare the crop box entry. Use this rectangle as the crop box for
            # this example.

            # XXX:fixme: need to encode as CFData!!!
            info[Quartz.kCGPDFContextCropBox] = Quartz.CGRectMake(100, 100, 200, 200)

    if url is not None:
        pdfContext = Quartz.CGPDFContextCreateWithURL(url, mediaRect, info)
        if pdfContext is not None:
            Quartz.CGContextBeginPage(pdfContext, mediaRect)
            if 1:
                Quartz.CGContextSaveGState(pdfContext)
                if 1:
                    Quartz.CGContextClipToRect(pdfContext, mediaRect)
                    AppDrawing.DispatchDrawing(pdfContext, exportInfo.command)
                Quartz.CGContextRestoreGState(pdfContext)
            Quartz.CGContextEndPage(pdfContext)
            del pdfContext
        else:
            print("Can't create PDF document!")
