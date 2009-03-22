
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintInfo (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPortraitOrientation, 0)
        self.failUnlessEqual(NSLandscapeOrientation, 1)

        self.failUnlessEqual(NSAutoPagination, 0)
        self.failUnlessEqual(NSFitPagination, 1)
        self.failUnlessEqual(NSClipPagination, 2)

        self.failUnlessIsInstance(NSPrintSpoolJob, unicode)
        self.failUnlessIsInstance(NSPrintPreviewJob, unicode)
        self.failUnlessIsInstance(NSPrintSaveJob, unicode)
        self.failUnlessIsInstance(NSPrintCancelJob, unicode)
        self.failUnlessIsInstance(NSPrintPaperName, unicode)
        self.failUnlessIsInstance(NSPrintPaperSize, unicode)
        self.failUnlessIsInstance(NSPrintOrientation, unicode)
        self.failUnlessIsInstance(NSPrintScalingFactor, unicode)
        self.failUnlessIsInstance(NSPrintLeftMargin, unicode)
        self.failUnlessIsInstance(NSPrintRightMargin, unicode)
        self.failUnlessIsInstance(NSPrintTopMargin, unicode)
        self.failUnlessIsInstance(NSPrintBottomMargin, unicode)
        self.failUnlessIsInstance(NSPrintHorizontallyCentered, unicode)
        self.failUnlessIsInstance(NSPrintVerticallyCentered, unicode)
        self.failUnlessIsInstance(NSPrintHorizontalPagination, unicode)
        self.failUnlessIsInstance(NSPrintVerticalPagination, unicode)
        self.failUnlessIsInstance(NSPrintPrinter, unicode)
        self.failUnlessIsInstance(NSPrintCopies, unicode)
        self.failUnlessIsInstance(NSPrintAllPages, unicode)
        self.failUnlessIsInstance(NSPrintFirstPage, unicode)
        self.failUnlessIsInstance(NSPrintLastPage, unicode)
        self.failUnlessIsInstance(NSPrintMustCollate, unicode)
        self.failUnlessIsInstance(NSPrintReversePageOrder, unicode)
        self.failUnlessIsInstance(NSPrintJobDisposition, unicode)
        self.failUnlessIsInstance(NSPrintSavePath, unicode)
        self.failUnlessIsInstance(NSPrintPagesAcross, unicode)
        self.failUnlessIsInstance(NSPrintPagesDown, unicode)
        self.failUnlessIsInstance(NSPrintTime, unicode)
        self.failUnlessIsInstance(NSPrintDetailedErrorReporting, unicode)
        self.failUnlessIsInstance(NSPrintFaxNumber, unicode)
        self.failUnlessIsInstance(NSPrintPrinterName, unicode)
        self.failUnlessIsInstance(NSPrintHeaderAndFooter, unicode)

        self.failUnlessIsInstance(NSPrintFormName, unicode)
        self.failUnlessIsInstance(NSPrintJobFeatures, unicode)
        self.failUnlessIsInstance(NSPrintManualFeed, unicode)
        self.failUnlessIsInstance(NSPrintPagesPerSheet, unicode)
        self.failUnlessIsInstance(NSPrintPaperFeed, unicode)
        self.failUnlessIsInstance(NSPrintFaxCoverSheetName, unicode)
        self.failUnlessIsInstance(NSPrintFaxHighResolution, unicode)
        self.failUnlessIsInstance(NSPrintFaxModem, unicode)
        self.failUnlessIsInstance(NSPrintFaxReceiverNames, unicode)
        self.failUnlessIsInstance(NSPrintFaxReceiverNumbers, unicode)
        self.failUnlessIsInstance(NSPrintFaxReturnReceipt, unicode)
        self.failUnlessIsInstance(NSPrintFaxSendTime, unicode)
        self.failUnlessIsInstance(NSPrintFaxTrimPageEnds, unicode)
        self.failUnlessIsInstance(NSPrintFaxUseCoverSheet, unicode)
        self.failUnlessIsInstance(NSPrintFaxJob, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPrintInfo.isHorizontallyCentered)
        self.failUnlessResultIsBOOL(NSPrintInfo.isVerticallyCentered)
        self.failUnlessArgIsBOOL(NSPrintInfo.setHorizontallyCentered_, 0)
        self.failUnlessArgIsBOOL(NSPrintInfo.setVerticallyCentered_, 0)


if __name__ == "__main__":
    main()
