from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXSetHeldCallAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXSetHeldCallAction.isOnHold)
        self.assertArgIsBOOL(CallKit.CXSetHeldCallAction.setOnHold_, 0)
