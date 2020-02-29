from PyObjCTools.TestSupport import *
from Quartz import CoreGraphics
from Quartz.CoreGraphics import *


class TestCGDirectDisplayMetal(TestCase):
    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertResultIsCFRetained(CGDirectDisplayCopyCurrentMetalDevice)
        v = CGDirectDisplayCopyCurrentMetalDevice(CGMainDisplayID())


if __name__ == "__main__":
    main()
