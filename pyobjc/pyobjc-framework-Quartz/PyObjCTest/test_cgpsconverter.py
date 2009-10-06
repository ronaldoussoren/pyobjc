
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPSConverter (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPSConverter.h>")

if __name__ == "__main__":
    main()
