from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz
import objc


class TestCGPDFObject(TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFObject.h>")

    def testConstants(self):
        self.assertEqual(Quartz.kCGPDFObjectTypeNull, 1)
        self.assertEqual(Quartz.kCGPDFObjectTypeBoolean, 2)
        self.assertEqual(Quartz.kCGPDFObjectTypeInteger, 3)
        self.assertEqual(Quartz.kCGPDFObjectTypeReal, 4)
        self.assertEqual(Quartz.kCGPDFObjectTypeName, 5)
        self.assertEqual(Quartz.kCGPDFObjectTypeString, 6)
        self.assertEqual(Quartz.kCGPDFObjectTypeArray, 7)
        self.assertEqual(Quartz.kCGPDFObjectTypeDictionary, 8)
        self.assertEqual(Quartz.kCGPDFObjectTypeStream, 9)

    def testFunctions(self):
        Quartz.CGPDFObjectGetType

        self.assertNotIsInstance(Quartz.CGPDFObjectGetValue, objc.function)
        # XXX: Actual tests for ^^^^ (with manual wrapper)
