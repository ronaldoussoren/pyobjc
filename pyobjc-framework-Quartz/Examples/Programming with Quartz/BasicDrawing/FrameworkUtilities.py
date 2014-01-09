import Cocoa

import AppDrawing

def myCreatePDFDataFromPasteBoard():
    # Obtain the pasteboard to examine.
    pboard = Cocoa.NSPasteboard.generalPasteboard()

    # Scan the types of data on the pasteboard and return the first type available that is
    # listed in the array supplied. Here the array of requested types contains only one type,
    # that of PDF data. If your application could handle more types, you would list them in
    # the creation of this array.
    type = pboard.availableTypeFromArray_([Cocoa.NSPDFPboardType])

    # If the string is non-nil, there was data of one of our requested types
        # on the pasteboard that can be obtained.
    if type is not None:
        # Test that the type is the PDF data type. This code is not strictly necessary
        # for this example since we only said we could handle PDF data, but is appropriate
        # if you can handle more types than just PDF.
        if type == Cocoa.NSPDFPboardType:
            # Get the PDF data from the pasteboard.
            pdfData = pboard.dataForType_(type)
            if pdfData is not None:
                return pdfData
            else:
                Cocoa.NSLog("Couldn't get PDF data from pasteboard!")
    else:
        Cocoa.NSLog("Pasteboard doesn't contain PDF data!")
    return None

def addPDFDataToPasteBoard(command):
    pdfData = cfDataCreatePDFDocumentFromCommand(command)
    if pdfData is not None:
        pboard = Cocoa.NSPasteboard.generalPasteboard()
        pboard.declareTypes_owner_(Cocoa.NSPDFPboardType, None)
        pboard.setData_forType_(pdfData, Cocoa.NSPDFPboardType)
