from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore


class TestSWAction(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(SharedWithYouCore.SWCollaborationIdentifier, str)
        self.assertIsTypedEnum(SharedWithYouCore.SWLocalCollaborationIdentifier, str)
