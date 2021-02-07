from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGDirectDisplayMetal(TestCase):
    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertResultIsCFRetained(Quartz.CGDirectDisplayCopyCurrentMetalDevice)
        Quartz.CGDirectDisplayCopyCurrentMetalDevice(Quartz.CGMainDisplayID())
