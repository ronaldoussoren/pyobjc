from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore


class TestSWCollaborationOption(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(SharedWithYouCore.SWCollaborationOption.isSelected)
