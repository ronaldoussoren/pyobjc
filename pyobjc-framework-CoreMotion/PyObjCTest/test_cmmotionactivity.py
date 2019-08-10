from PyObjCTools.TestSupport import *

import CoreMotion


class TestCMMotionActivity(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMotion.CMMotionActivityConfidenceLow, 0)
        self.assertEqual(CoreMotion.CMMotionActivityConfidenceMedium, 1)
        self.assertEqual(CoreMotion.CMMotionActivityConfidenceHigh, 2)
