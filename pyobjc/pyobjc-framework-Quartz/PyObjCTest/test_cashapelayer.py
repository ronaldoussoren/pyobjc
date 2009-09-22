from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAShapeLayer (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCAFillRuleNonZero, unicode)
        self.failUnlessIsInstance(kCAFillRuleEvenOdd, unicode)
        self.failUnlessIsInstance(kCALineJoinMiter, unicode)
        self.failUnlessIsInstance(kCALineJoinRound, unicode)
        self.failUnlessIsInstance(kCALineJoinRound, unicode)
        self.failUnlessIsInstance(kCALineCapButt, unicode)
        self.failUnlessIsInstance(kCALineCapRound, unicode)
        self.failUnlessIsInstance(kCALineCapSquare, unicode)

if __name__ == "__main__":
    main()
