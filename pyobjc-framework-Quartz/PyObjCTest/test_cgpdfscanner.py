
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFScanner (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFScanner.h>")

if __name__ == "__main__":
    main()
