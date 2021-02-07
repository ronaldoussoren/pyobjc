from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXCallController(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            CallKit.CXCallController.requestTransaction_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            CallKit.CXCallController.requestTransactionWithActions_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            CallKit.CXCallController.requestTransactionWithAction_completion_, 1, b"v@"
        )
