from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCATransaction(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.kCATransactionAnimationDuration, str)
        self.assertIsInstance(Quartz.kCATransactionDisableActions, str)
        self.assertIsInstance(Quartz.kCATransactionAnimationTimingFunction, str)
        self.assertIsInstance(Quartz.kCATransactionCompletionBlock, str)

    def test_methods10_6(self):
        self.assertResultIsBOOL(Quartz.CATransaction.disableActions)
        self.assertArgIsBOOL(Quartz.CATransaction.setDisableActions_, 0)

        self.assertResultIsBlock(Quartz.CATransaction.completionBlock, b"v")
        self.assertArgIsBlock(Quartz.CATransaction.setCompletionBlock_, 0, b"v")
