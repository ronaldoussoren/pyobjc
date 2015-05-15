
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFObject (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFObject.h>")

    def testConstants(self):
        self.assertEqual(kCGPDFObjectTypeNull, 1)
        self.assertEqual(kCGPDFObjectTypeBoolean, 2)
        self.assertEqual(kCGPDFObjectTypeInteger, 3)
        self.assertEqual(kCGPDFObjectTypeReal, 4)
        self.assertEqual(kCGPDFObjectTypeName, 5)
        self.assertEqual(kCGPDFObjectTypeString, 6)
        self.assertEqual(kCGPDFObjectTypeArray, 7)
        self.assertEqual(kCGPDFObjectTypeDictionary, 8)
        self.assertEqual(kCGPDFObjectTypeStream, 9)

    def testFunctions(self):
        CGPDFObjectGetType

        self.assertIsNotInstance(CGPDFObjectGetValue, objc.function)
        # XXX: Actual tests for ^^^^ (with manual wrapper)



if __name__ == "__main__":
    main()
