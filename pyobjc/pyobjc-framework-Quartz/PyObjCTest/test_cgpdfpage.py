
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFPage (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFPage.h>")

if __name__ == "__main__":
    main()
