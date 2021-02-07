from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXSetMutedCallAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXSetMutedCallAction.isMuted)
        self.assertArgIsBOOL(CallKit.CXSetMutedCallAction.setMuted_, 0)
