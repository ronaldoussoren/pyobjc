from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAShapeLayer(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCAFillRuleNonZero, str)
        self.assertIsInstance(Quartz.kCAFillRuleEvenOdd, str)
        self.assertIsInstance(Quartz.kCALineJoinMiter, str)
        self.assertIsInstance(Quartz.kCALineJoinRound, str)
        self.assertIsInstance(Quartz.kCALineJoinBevel, str)
        self.assertIsInstance(Quartz.kCALineCapButt, str)
        self.assertIsInstance(Quartz.kCALineCapRound, str)
        self.assertIsInstance(Quartz.kCALineCapSquare, str)
