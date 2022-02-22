from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAMediaTimingFunction(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CAMediaTimingFunctionName, str)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionLinear, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseIn, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseOut, str)
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionEaseInEaseOut, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCAMediaTimingFunctionDefault, str)
