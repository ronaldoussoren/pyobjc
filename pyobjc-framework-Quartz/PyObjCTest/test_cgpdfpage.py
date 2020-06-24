from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCGPDFPage(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGPDFMediaBox, 0)
        self.assertEqual(Quartz.kCGPDFCropBox, 1)
        self.assertEqual(Quartz.kCGPDFBleedBox, 2)
        self.assertEqual(Quartz.kCGPDFTrimBox, 3)
        self.assertEqual(Quartz.kCGPDFArtBox, 4)

    def testFunctions(self):
        Quartz.CGPDFPageRetain
        Quartz.CGPDFPageRelease
        Quartz.CGPDFPageGetDocument
        Quartz.CGPDFPageGetPageNumber
        Quartz.CGPDFPageGetBoxRect
        Quartz.CGPDFPageGetRotationAngle
        self.assertArgHasType(Quartz.CGPDFPageGetDrawingTransform, 4, objc._C_BOOL)
        Quartz.CGPDFPageGetDictionary
        Quartz.CGPDFPageGetTypeID
