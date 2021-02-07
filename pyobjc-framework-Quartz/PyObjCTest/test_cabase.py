from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCABase(TestCase):
    @min_os_level("10.5")
    def testFunctions(self):
        v = Quartz.CACurrentMediaTime()
        self.assertIsInstance(v, float)
