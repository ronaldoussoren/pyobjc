
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGRemoteOperation (TestCase):
    def testConstants(self):
        self.failUnlessEqual(CGEventNoErr, kCGErrorSuccess)

    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGRemoteOperation.h>")

if __name__ == "__main__":
    main()
