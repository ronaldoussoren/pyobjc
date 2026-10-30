from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCABase(TestCase):
    def test_functions(self):
        v = Quartz.CACurrentMediaTime()
        self.assertIsInstance(v, float)
