from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCACIFilterAdditions(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CIFilter.isEnabled)
        self.assertArgIsBOOL(Quartz.CIFilter.setEnabled_, 0)
