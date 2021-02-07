from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCATransaction(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCATransactionAnimationDuration, str)
        self.assertIsInstance(Quartz.kCATransactionDisableActions, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.CATransaction.disableActions)
        self.assertArgIsBOOL(Quartz.CATransaction.setDisableActions_, 0)

        self.assertResultIsBlock(Quartz.CATransaction.completionBlock, b"v")
        self.assertArgIsBlock(Quartz.CATransaction.setCompletionBlock_, 0, b"v")

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCATransactionAnimationTimingFunction, str)
        self.assertIsInstance(Quartz.kCATransactionCompletionBlock, str)
