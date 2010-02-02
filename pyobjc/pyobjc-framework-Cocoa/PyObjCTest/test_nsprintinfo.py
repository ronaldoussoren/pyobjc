
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintInfo (TestCase):
    def testConstants(self):
        self.assertEqual(NSPortraitOrientation, 0)
        self.assertEqual(NSLandscapeOrientation, 1)

        self.assertEqual(NSAutoPagination, 0)
        self.assertEqual(NSFitPagination, 1)
        self.assertEqual(NSClipPagination, 2)

        self.assertIsInstance(NSPrintSpoolJob, unicode)
        self.assertIsInstance(NSPrintPreviewJob, unicode)
        self.assertIsInstance(NSPrintSaveJob, unicode)
        self.assertIsInstance(NSPrintCancelJob, unicode)
        self.assertIsInstance(NSPrintPaperName, unicode)
        self.assertIsInstance(NSPrintPaperSize, unicode)
        self.assertIsInstance(NSPrintOrientation, unicode)
        self.assertIsInstance(NSPrintScalingFactor, unicode)
        self.assertIsInstance(NSPrintLeftMargin, unicode)
        self.assertIsInstance(NSPrintRightMargin, unicode)
        self.assertIsInstance(NSPrintTopMargin, unicode)
        self.assertIsInstance(NSPrintBottomMargin, unicode)
        self.assertIsInstance(NSPrintHorizontallyCentered, unicode)
        self.assertIsInstance(NSPrintVerticallyCentered, unicode)
        self.assertIsInstance(NSPrintHorizontalPagination, unicode)
        self.assertIsInstance(NSPrintVerticalPagination, unicode)
        self.assertIsInstance(NSPrintPrinter, unicode)
        self.assertIsInstance(NSPrintCopies, unicode)
        self.assertIsInstance(NSPrintAllPages, unicode)
        self.assertIsInstance(NSPrintFirstPage, unicode)
        self.assertIsInstance(NSPrintLastPage, unicode)
        self.assertIsInstance(NSPrintMustCollate, unicode)
        self.assertIsInstance(NSPrintReversePageOrder, unicode)
        self.assertIsInstance(NSPrintJobDisposition, unicode)
        self.assertIsInstance(NSPrintSavePath, unicode)
        self.assertIsInstance(NSPrintPagesAcross, unicode)
        self.assertIsInstance(NSPrintPagesDown, unicode)
        self.assertIsInstance(NSPrintTime, unicode)
        self.assertIsInstance(NSPrintDetailedErrorReporting, unicode)
        self.assertIsInstance(NSPrintFaxNumber, unicode)
        self.assertIsInstance(NSPrintPrinterName, unicode)
        self.assertIsInstance(NSPrintHeaderAndFooter, unicode)

        self.assertIsInstance(NSPrintFormName, unicode)
        self.assertIsInstance(NSPrintJobFeatures, unicode)
        self.assertIsInstance(NSPrintManualFeed, unicode)
        self.assertIsInstance(NSPrintPagesPerSheet, unicode)
        self.assertIsInstance(NSPrintPaperFeed, unicode)
        self.assertIsInstance(NSPrintFaxCoverSheetName, unicode)
        self.assertIsInstance(NSPrintFaxHighResolution, unicode)
        self.assertIsInstance(NSPrintFaxModem, unicode)
        self.assertIsInstance(NSPrintFaxReceiverNames, unicode)
        self.assertIsInstance(NSPrintFaxReceiverNumbers, unicode)
        self.assertIsInstance(NSPrintFaxReturnReceipt, unicode)
        self.assertIsInstance(NSPrintFaxSendTime, unicode)
        self.assertIsInstance(NSPrintFaxTrimPageEnds, unicode)
        self.assertIsInstance(NSPrintFaxUseCoverSheet, unicode)
        self.assertIsInstance(NSPrintFaxJob, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSPrintInfo.isHorizontallyCentered)
        self.assertResultIsBOOL(NSPrintInfo.isVerticallyCentered)
        self.assertArgIsBOOL(NSPrintInfo.setHorizontallyCentered_, 0)
        self.assertArgIsBOOL(NSPrintInfo.setVerticallyCentered_, 0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSPrintSelectionOnly, unicode)
        self.assertIsInstance(NSPrintJobSavingURL, unicode)
        self.assertIsInstance(NSPrintJobSavingFileNameExtensionHidden, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSPrintInfo.isSelectionOnly)
        self.assertArgIsBOOL(NSPrintInfo.setSelectionOnly_, 0)


if __name__ == "__main__":
    main()
