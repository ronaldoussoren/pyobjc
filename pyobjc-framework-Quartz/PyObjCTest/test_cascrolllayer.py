from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAScrollLayer(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCAScrollNone, str)
        self.assertIsInstance(Quartz.kCAScrollVertically, str)
        self.assertIsInstance(Quartz.kCAScrollHorizontally, str)
        self.assertIsInstance(Quartz.kCAScrollBoth, str)
