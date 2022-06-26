from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401


class TestSWHighlightCenter(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWHighlightCenterDelegate")

    def test_methods(self):
        self.assertArgIsOut(SharedWithYou.collaborationHighlightForURL_error_, 1)
        self.assertArgIsOut(SharedWithYou.collaborationHighlightForIdentifier_error_, 1)
        self.assertArgIsBlock(
            SharedWithYou.getSignedIdentityProofForCollaborationHighlight_usingData_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsOut(SharedWithYou.highlightForURL_error_, 1)
