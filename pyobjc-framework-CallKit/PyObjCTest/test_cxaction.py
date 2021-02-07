from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXAction.isComplete)
