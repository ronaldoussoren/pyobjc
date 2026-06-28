from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAScrollLayer(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(Quartz.CAScrollLayerScrollMode, str)

    def test_constants(self):
        self.assertIsInstance(Quartz.kCAScrollNone, str)
        self.assertIsInstance(Quartz.kCAScrollVertically, str)
        self.assertIsInstance(Quartz.kCAScrollHorizontally, str)
        self.assertIsInstance(Quartz.kCAScrollBoth, str)
