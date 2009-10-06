
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFStream (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFStream.h>")

if __name__ == "__main__":
    main()
