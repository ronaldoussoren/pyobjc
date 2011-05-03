
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFString (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFString.h>")

if __name__ == "__main__":
    main()
