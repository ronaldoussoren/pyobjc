import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMGyro(TestCase):
    def test_structs(self):
        v = CoreMotion.CMRotationRate()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)
        self.assertEqual(v.z, 0.0)
