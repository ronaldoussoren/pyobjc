from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore


class TestSWAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(SharedWithYouCore.SWAction.isComplete)
