
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFDocument (TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFDocument.h>")
        # See XXX below

    def testFunctions(self):
        self.assertResultIsCFRetained(CGPDFDocumentCreateWithProvider)
        self.assertResultIsCFRetained(CGPDFDocumentCreateWithURL)

        CGPDFDocumentRetain
        CGPDFDocumentRelease

        self.assertArgIsOut(CGPDFDocumentGetVersion, 1)
        self.assertArgIsOut(CGPDFDocumentGetVersion, 2)

        self.assertResultHasType(CGPDFDocumentIsEncrypted, objc._C_BOOL)

        self.assertResultHasType(CGPDFDocumentUnlockWithPassword, objc._C_BOOL)
        # XXX: CGPDFDocumentUnlockWithPassword 'password' needs test

        self.assertResultHasType(CGPDFDocumentIsUnlocked, objc._C_BOOL)
        self.assertResultHasType(CGPDFDocumentAllowsPrinting, objc._C_BOOL)
        self.assertResultHasType(CGPDFDocumentAllowsCopying, objc._C_BOOL)

        CGPDFDocumentGetNumberOfPages
        CGPDFDocumentGetPage
        CGPDFDocumentGetCatalog
        CGPDFDocumentGetInfo
        CGPDFDocumentGetID
        CGPDFDocumentGetTypeID
        CGPDFDocumentGetMediaBox
        CGPDFDocumentGetCropBox
        CGPDFDocumentGetBleedBox
        CGPDFDocumentGetTrimBox
        CGPDFDocumentGetArtBox
        CGPDFDocumentGetRotationAngle

    @min_os_level('10.13')
    def testFunctions(self):
        CGPDFDocumentGetOutline
        CGPDFDocumentGetAccessPermissions

    def testConstants(self):
        self.assertEqual(kCGPDFAllowsLowQualityPrinting, 1 << 0)
        self.assertEqual(kCGPDFAllowsHighQualityPrinting, 1 << 1)
        self.assertEqual(kCGPDFAllowsDocumentChanges, 1 << 2)
        self.assertEqual(kCGPDFAllowsDocumentAssembly, 1 << 3)
        self.assertEqual(kCGPDFAllowsContentCopying, 1 << 4)
        self.assertEqual(kCGPDFAllowsContentAccessibility, 1 << 5)
        self.assertEqual(kCGPDFAllowsCommenting, 1 << 6)
        self.assertEqual(kCGPDFAllowsFormFieldEntry, 1 << 7)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCGPDFOutlineTitle, unicode)
        self.assertIsInstance(kCGPDFOutlineChildren, unicode)
        self.assertIsInstance(kCGPDFOutlineDestination, unicode)
        self.assertIsInstance(kCGPDFOutlineDestinationRect, unicode)

if __name__ == "__main__":
    main()
