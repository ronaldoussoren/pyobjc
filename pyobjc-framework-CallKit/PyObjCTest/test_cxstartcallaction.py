from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXStartCallAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXStartCallAction.isVideo)
        self.assertArgIsBOOL(CallKit.CXStartCallAction.setVideo_, 0)
