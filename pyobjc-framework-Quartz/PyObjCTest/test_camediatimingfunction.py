from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAMediaTimingFunction(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(Quartz.CAMediaTimingFunctionName, str)

    def test_constants(self):
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionLinear, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseIn, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseOut, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseInEaseOut, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionDefault, str)
