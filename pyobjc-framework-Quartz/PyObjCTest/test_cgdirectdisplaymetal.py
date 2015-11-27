from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz import CoreGraphics

class TestCGDirectDisplayMetal (TestCase):

    @min_os_level('10.11')
    def testFunctions10_11(self):
        self.assertResultIsCFRetained(CGDirectDisplayCopyCurrentMetalDevice)
        v = CGDirectDisplayCopyCurrentMetalDevice(CGMainDisplayID())


if __name__ == "__main__":
    main()
