from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401


class TestSWHighlightCenter(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWHighlightCenterDelegate")

    def test_methods(self):
        self.assertArgIsOut(
            SharedWithYou.SWHighlightCenter.collaborationHighlightForURL_error_, 1
        )
        self.assertArgIsOut(
            SharedWithYou.SWHighlightCenter.collaborationHighlightForIdentifier_error_,
            1,
        )
        self.assertArgIsBlock(
            SharedWithYou.SWHighlightCenter.getSignedIdentityProofForCollaborationHighlight_usingData_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsOut(SharedWithYou.SWHighlightCenter.highlightForURL_error_, 1)
