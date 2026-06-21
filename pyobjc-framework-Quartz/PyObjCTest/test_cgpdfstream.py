from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGPDFStream(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFStreamRef)

    def test_constants(self):
        self.assertEqual(Quartz.CGPDFDataFormatRaw, 0)
        self.assertEqual(Quartz.CGPDFDataFormatJPEGEncoded, 1)
        self.assertEqual(Quartz.CGPDFDataFormatJPEG2000, 2)

    def test_functions(self):
        Quartz.CGPDFStreamGetDictionary
        self.assertResultIsCFRetained(Quartz.CGPDFStreamCopyData)
        self.assertArgIsOut(Quartz.CGPDFStreamCopyData, 1)
