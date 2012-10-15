from Quartz import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


class TestCAShapeLayer (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAFillRuleNonZero, unicode)
        self.assertIsInstance(kCAFillRuleEvenOdd, unicode)
        self.assertIsInstance(kCALineJoinMiter, unicode)
        self.assertIsInstance(kCALineJoinRound, unicode)
        self.assertIsInstance(kCALineJoinBevel, unicode)
        self.assertIsInstance(kCALineCapButt, unicode)
        self.assertIsInstance(kCALineCapRound, unicode)
        self.assertIsInstance(kCALineCapSquare, unicode)

if __name__ == "__main__":
    main()
