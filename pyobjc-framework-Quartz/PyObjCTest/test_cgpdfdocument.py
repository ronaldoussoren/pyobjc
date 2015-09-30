
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



if __name__ == "__main__":
    main()
