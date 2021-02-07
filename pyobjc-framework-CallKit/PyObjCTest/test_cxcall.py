from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXCall(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXCall.isOutgoing)
        self.assertResultIsBOOL(CallKit.CXCall.isOnHold)
        self.assertResultIsBOOL(CallKit.CXCall.hasConnected)
        self.assertResultIsBOOL(CallKit.CXCall.hasEnded)
