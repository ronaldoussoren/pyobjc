from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGBase(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.CGFLOAT_MIN, float)
        self.assertIsInstance(Quartz.CGFLOAT_MAX, float)
        self.assertIsInstance(Quartz.CGFLOAT_IS_DOUBLE, int)
