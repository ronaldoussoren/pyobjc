
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFString (TestCase):

    def test_types(self):
        self.assertIsOpaquePointer(CGPDFStringRef)

    def testFunctions(self):
        CGPDFStringGetLength

        self.assertResultIsVariableSize(CGPDFStringGetBytePtr)

        self.assertResultIsCFRetained(CGPDFStringCopyTextString)
        self.assertResultIsCFRetained(CGPDFStringCopyDate)


if __name__ == "__main__":
    main()
