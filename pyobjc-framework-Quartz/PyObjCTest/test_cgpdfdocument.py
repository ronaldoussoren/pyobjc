
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFDocument (TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFDocument.h>")

if __name__ == "__main__":
    main()
