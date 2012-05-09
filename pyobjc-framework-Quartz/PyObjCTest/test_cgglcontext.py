
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGGLContext (TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGGLContext.h>")

if __name__ == "__main__":
    main()
