from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz
import objc


class TestCGPDFDocument(TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFDocument.h>")
        # See XXX below

    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGPDFDocumentCreateWithProvider)
        self.assertResultIsCFRetained(Quartz.CGPDFDocumentCreateWithURL)

        Quartz.CGPDFDocumentRetain
        Quartz.CGPDFDocumentRelease

        self.assertArgIsOut(Quartz.CGPDFDocumentGetVersion, 1)
        self.assertArgIsOut(Quartz.CGPDFDocumentGetVersion, 2)

        self.assertResultHasType(Quartz.CGPDFDocumentIsEncrypted, objc._C_BOOL)

        self.assertResultHasType(Quartz.CGPDFDocumentUnlockWithPassword, objc._C_BOOL)
        # XXX: CGPDFDocumentUnlockWithPassword 'password' needs test

        self.assertResultHasType(Quartz.CGPDFDocumentIsUnlocked, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGPDFDocumentAllowsPrinting, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGPDFDocumentAllowsCopying, objc._C_BOOL)

        Quartz.CGPDFDocumentGetNumberOfPages
        Quartz.CGPDFDocumentGetPage
        Quartz.CGPDFDocumentGetCatalog
        Quartz.CGPDFDocumentGetInfo
        Quartz.CGPDFDocumentGetID
        Quartz.CGPDFDocumentGetTypeID
        Quartz.CGPDFDocumentGetMediaBox
        Quartz.CGPDFDocumentGetCropBox
        Quartz.CGPDFDocumentGetBleedBox
        Quartz.CGPDFDocumentGetTrimBox
        Quartz.CGPDFDocumentGetArtBox
        Quartz.CGPDFDocumentGetRotationAngle

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGPDFDocumentGetOutline
        Quartz.CGPDFDocumentGetAccessPermissions

    def testConstants(self):
        self.assertEqual(Quartz.kCGPDFAllowsLowQualityPrinting, 1 << 0)
        self.assertEqual(Quartz.kCGPDFAllowsHighQualityPrinting, 1 << 1)
        self.assertEqual(Quartz.kCGPDFAllowsDocumentChanges, 1 << 2)
        self.assertEqual(Quartz.kCGPDFAllowsDocumentAssembly, 1 << 3)
        self.assertEqual(Quartz.kCGPDFAllowsContentCopying, 1 << 4)
        self.assertEqual(Quartz.kCGPDFAllowsContentAccessibility, 1 << 5)
        self.assertEqual(Quartz.kCGPDFAllowsCommenting, 1 << 6)
        self.assertEqual(Quartz.kCGPDFAllowsFormFieldEntry, 1 << 7)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCGPDFOutlineTitle, str)
        self.assertIsInstance(Quartz.kCGPDFOutlineChildren, str)
        self.assertIsInstance(Quartz.kCGPDFOutlineDestination, str)
        self.assertIsInstance(Quartz.kCGPDFOutlineDestinationRect, str)
