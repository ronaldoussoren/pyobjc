from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore  # noqa: F401


class TestSWCollaborationActionHandler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWCollaborationActionHandler")
