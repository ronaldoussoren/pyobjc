import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level


class TestNSPrintInfo(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSPrintInfoAttributeKey, str)
        self.assertIsTypedEnum(AppKit.NSPrintJobDispositionValue, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPaperOrientation)
        self.assertIsEnumType(AppKit.NSPrintingOrientation)
        self.assertIsEnumType(AppKit.NSPrintingPaginationMode)

    def testConstants(self):
        self.assertEqual(AppKit.NSPortraitOrientation, 0)
        self.assertEqual(AppKit.NSLandscapeOrientation, 1)

        self.assertEqual(AppKit.NSPaperOrientationPortrait, 0)
        self.assertEqual(AppKit.NSPaperOrientationLandscape, 1)

        self.assertEqual(AppKit.NSAutoPagination, 0)
        self.assertEqual(AppKit.NSFitPagination, 1)
        self.assertEqual(AppKit.NSClipPagination, 2)

        self.assertIsInstance(AppKit.NSPrintSpoolJob, str)
        self.assertIsInstance(AppKit.NSPrintPreviewJob, str)
        self.assertIsInstance(AppKit.NSPrintSaveJob, str)
        self.assertIsInstance(AppKit.NSPrintCancelJob, str)

        self.assertIsInstance(AppKit.NSPrintPaperName, str)
        self.assertIsInstance(AppKit.NSPrintPaperSize, str)
        self.assertIsInstance(AppKit.NSPrintOrientation, str)
        self.assertIsInstance(AppKit.NSPrintScalingFactor, str)

        self.assertIsInstance(AppKit.NSPrintLeftMargin, str)
        self.assertIsInstance(AppKit.NSPrintRightMargin, str)
        self.assertIsInstance(AppKit.NSPrintTopMargin, str)
        self.assertIsInstance(AppKit.NSPrintBottomMargin, str)
        self.assertIsInstance(AppKit.NSPrintHorizontallyCentered, str)
        self.assertIsInstance(AppKit.NSPrintVerticallyCentered, str)
        self.assertIsInstance(AppKit.NSPrintHorizontalPagination, str)
        self.assertIsInstance(AppKit.NSPrintVerticalPagination, str)

        self.assertIsInstance(AppKit.NSPrintPrinter, str)
        self.assertIsInstance(AppKit.NSPrintCopies, str)
        self.assertIsInstance(AppKit.NSPrintAllPages, str)
        self.assertIsInstance(AppKit.NSPrintFirstPage, str)
        self.assertIsInstance(AppKit.NSPrintLastPage, str)
        self.assertIsInstance(AppKit.NSPrintMustCollate, str)
        self.assertIsInstance(AppKit.NSPrintReversePageOrder, str)
        self.assertIsInstance(AppKit.NSPrintJobDisposition, str)
        self.assertIsInstance(AppKit.NSPrintSavePath, str)
        self.assertIsInstance(AppKit.NSPrintPagesAcross, str)
        self.assertIsInstance(AppKit.NSPrintPagesDown, str)
        self.assertIsInstance(AppKit.NSPrintTime, str)
        self.assertIsInstance(AppKit.NSPrintDetailedErrorReporting, str)
        self.assertIsInstance(AppKit.NSPrintFaxNumber, str)
        self.assertIsInstance(AppKit.NSPrintPrinterName, str)

        self.assertIsInstance(AppKit.NSPrintHeaderAndFooter, str)

        self.assertIsInstance(AppKit.NSPrintFormName, str)
        self.assertIsInstance(AppKit.NSPrintJobFeatures, str)
        self.assertIsInstance(AppKit.NSPrintManualFeed, str)
        self.assertIsInstance(AppKit.NSPrintPagesPerSheet, str)
        self.assertIsInstance(AppKit.NSPrintPaperFeed, str)

        self.assertEqual(AppKit.NSPrintingPaginationModeAutomatic, 0)
        self.assertEqual(AppKit.NSPrintingPaginationModeFit, 1)
        self.assertEqual(AppKit.NSPrintingPaginationModeClip, 2)

    @max_os_level("10.13")
    def testConstants_not10_14(self):
        self.assertIsInstance(AppKit.NSPrintFaxCoverSheetName, str)
        self.assertIsInstance(AppKit.NSPrintFaxHighResolution, str)
        self.assertIsInstance(AppKit.NSPrintFaxModem, str)
        self.assertIsInstance(AppKit.NSPrintFaxReceiverNames, str)
        self.assertIsInstance(AppKit.NSPrintFaxReceiverNumbers, str)
        self.assertIsInstance(AppKit.NSPrintFaxReturnReceipt, str)
        self.assertIsInstance(AppKit.NSPrintFaxSendTime, str)
        self.assertIsInstance(AppKit.NSPrintFaxTrimPageEnds, str)
        self.assertIsInstance(AppKit.NSPrintFaxUseCoverSheet, str)
        self.assertIsInstance(AppKit.NSPrintFaxJob, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSPrintInfo.isHorizontallyCentered)
        self.assertResultIsBOOL(AppKit.NSPrintInfo.isVerticallyCentered)
        self.assertArgIsBOOL(AppKit.NSPrintInfo.setHorizontallyCentered_, 0)
        self.assertArgIsBOOL(AppKit.NSPrintInfo.setVerticallyCentered_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSPrintSelectionOnly, str)
        self.assertIsInstance(AppKit.NSPrintJobSavingURL, str)
        self.assertIsInstance(AppKit.NSPrintJobSavingFileNameExtensionHidden, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSPrintInfo.isSelectionOnly)
        self.assertArgIsBOOL(AppKit.NSPrintInfo.setSelectionOnly_, 0)
