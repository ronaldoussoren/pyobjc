
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFPage (TestCase):
    def testConstants(self):
        self.assertEqual(kCGPDFMediaBox, 0)
        self.assertEqual(kCGPDFCropBox, 1)
        self.assertEqual(kCGPDFBleedBox, 2)
        self.assertEqual(kCGPDFTrimBox, 3)
        self.assertEqual(kCGPDFArtBox, 4)

    def testFunctions(self):
        CGPDFPageRetain
        CGPDFPageRelease
        CGPDFPageGetDocument
        CGPDFPageGetPageNumber
        CGPDFPageGetBoxRect
        CGPDFPageGetRotationAngle
        self.assertArgHasType(CGPDFPageGetDrawingTransform, 4, objc._C_BOOL)
        CGPDFPageGetDictionary
        CGPDFPageGetTypeID



if __name__ == "__main__":
    main()
