from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQuartzFilter(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QuartzFilter.applyToContext_)
