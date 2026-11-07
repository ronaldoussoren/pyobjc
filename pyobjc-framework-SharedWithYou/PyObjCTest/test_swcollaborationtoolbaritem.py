from PyObjCTools.TestSupport import TestCase, min_os_level

import SharedWithYou


class TestSWCollaborationToolbarItem(TestCase):
    @min_os_level("27.3")
    def test_methods(self):
        self.assertResultIsBOOL(
            SharedWithYou.SWCollaborationToolbarItem.showsParticipantCount
        )
        self.assertArgIsBOOL(
            SharedWithYou.SWCollaborationToolbarItem.setShowsParticipantCount_, 0
        )

        self.assertResultIsBOOL(
            SharedWithYou.SWCollaborationToolbarItem.showManageButton
        )
        self.assertArgIsBOOL(
            SharedWithYou.SWCollaborationToolbarItem.setShowManageButton_, 0
        )

        self.assertArgIsBOOL(
            SharedWithYou.SWCollaborationToolbarItem.dismissPopoverAnimated_completion_,
            0,
        )
        self.assertArgIsBlock(
            SharedWithYou.SWCollaborationToolbarItem.dismissPopoverAnimated_completion_,
            1,
            b"v",
        )
