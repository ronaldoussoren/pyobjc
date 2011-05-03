
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCATransaction (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCATransactionAnimationDuration, unicode)
        self.assertIsInstance(kCATransactionDisableActions, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CATransaction.disableActions)
        self.assertArgIsBOOL(CATransaction.setDisableActions_, 0)

        self.assertResultIsBlock(CATransaction.completionBlock, b'v')
        self.assertArgIsBlock(CATransaction.setCompletionBlock_, 0, b'v')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCATransactionAnimationTimingFunction, unicode)
        self.assertIsInstance(kCATransactionCompletionBlock, unicode)


if __name__ == "__main__":
    main()
