from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWCollaborationBarButtonItem(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            SharedWithYou._SWCollaborationBarButtonItem.isContentShared
        )
        self.assertArgIsBOOL(
            SharedWithYou._SWCollaborationBarButtonItem.setIsContentShared_, 0
        )

        self.assertArgIsBOOL(
            SharedWithYou._SWCollaborationBarButtonItem.dismissPopoverAnimated_completion_,
            0,
        )
        self.assertArgIsBlock(
            SharedWithYou._SWCollaborationBarButtonItem.dismissPopoverAnimated_completion_,
            1,
            b"v",
        )
