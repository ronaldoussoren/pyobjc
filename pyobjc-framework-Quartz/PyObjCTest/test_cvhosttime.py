from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCVHostTime(TestCase):
    def testFunctions(self):
        v = Quartz.CVGetCurrentHostTime()
        self.assertIsInstance(v, int)

        v = Quartz.CVGetHostClockFrequency()
        self.assertIsInstance(v, float)

        v = Quartz.CVGetHostClockMinimumTimeDelta()
        self.assertIsInstance(v, int)
