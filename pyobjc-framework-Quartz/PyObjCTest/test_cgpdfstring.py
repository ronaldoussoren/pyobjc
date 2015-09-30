
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFString (TestCase):

    @expectedFailure
    def testIncomplete(self):
        CGPDFStringGetBytePtr
        self.fail("Add header tests for <CoreGraphics/CGPDFString.h>")
        # XXX: type of CGPDFStringRef

    def testFunctions(self):
        CGPDFStringGetLength

        self.assertResultIsCFRetained(CGPDFStringCopyTextString)
        self.assertResultIsCFRetained(CGPDFStringCopyDate)


if __name__ == "__main__":
    main()
