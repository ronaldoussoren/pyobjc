
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFOperatorTable (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFOperatorTable.h>")

if __name__ == "__main__":
    main()
