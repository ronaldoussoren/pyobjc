from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXTransaction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXTransaction.isComplete)
