from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGPDFStream(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFStreamRef)

    def testConstants(self):
        self.assertEqual(Quartz.CGPDFDataFormatRaw, 0)
        self.assertEqual(Quartz.CGPDFDataFormatJPEGEncoded, 1)
        self.assertEqual(Quartz.CGPDFDataFormatJPEG2000, 2)

    def testFunctions(self):
        Quartz.CGPDFStreamGetDictionary
        self.assertResultIsCFRetained(Quartz.CGPDFStreamCopyData)
        self.assertArgIsOut(Quartz.CGPDFStreamCopyData, 1)
