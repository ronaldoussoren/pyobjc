
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCATransaction (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCATransactionAnimationDuration, unicode)
        self.failUnlessIsInstance(kCATransactionDisableActions, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(CATransaction.disableActions)
        self.failUnlessArgIsBOOL(CATransaction.setDisableActions_, 0)

        self.failUnlessResultIsBlock(CATransaction.completionBlock, 'v')
        self.failUnlessArgIsBlock(CATransaction.setCompletionBlock_, 0, 'v')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCATransactionAnimationTimingFunction, unicode)
        self.failUnlessIsInstance(kCATransactionCompletionBlock, unicode)


if __name__ == "__main__":
    main()
