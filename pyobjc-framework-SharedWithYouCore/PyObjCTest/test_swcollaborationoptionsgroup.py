from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore


class TestSWCollaborationOptionsGroup(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            SharedWithYouCore.UTCollaborationOptionsTypeIdentifier, str
        )
