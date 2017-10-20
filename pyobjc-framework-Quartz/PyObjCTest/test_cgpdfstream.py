
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFStream (TestCase):

    def test_types(self):
        self.assertIsOpaquePointer(CGPDFStreamRef)

    def testConstants(self):
        self.assertEqual(CGPDFDataFormatRaw, 0)
        self.assertEqual(CGPDFDataFormatJPEGEncoded, 1)
        self.assertEqual(CGPDFDataFormatJPEG2000, 2)

    def testFunctions(self):
        CGPDFStreamGetDictionary
        self.assertResultIsCFRetained(CGPDFStreamCopyData)
        self.assertArgIsOut(CGPDFStreamCopyData, 1)


if __name__ == "__main__":
    main()
