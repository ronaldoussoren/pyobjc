from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWAttributionViewHelper(SharedWithYou.NSObject):
    def collaborationViewShouldPresentPopover_(self, a):
        return 1


class TestSWAttributionView(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWCollaborationViewDelegate")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestSWAttributionViewHelper.collaborationViewShouldPresentPopover_
        )

    def test_methods(self):
        self.assertArgIsBlock(
            SharedWithYou.SWCollaborationView.dismissPopover_, 0, b"v"
        )
        self.assertArgIsBOOL(SharedWithYou.SWCollaborationView.setShowManageButton_, 0)
