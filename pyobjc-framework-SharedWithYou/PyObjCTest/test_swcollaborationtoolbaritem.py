from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWCollaborationToolbarItem(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            SharedWithYou._SWCollaborationToolbarItem.dismissPopoverAnimated_completion_,
            0,
        )
        self.assertArgIsBlock(
            SharedWithYou._SWCollaborationToolbarItem.dismissPopoverAnimated_completion_,
            1,
            b"v",
        )
