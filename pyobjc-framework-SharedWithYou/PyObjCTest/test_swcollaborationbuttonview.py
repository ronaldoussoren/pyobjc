from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWCollaborationButtonView(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            SharedWithYou._SWCollaborationButtonView.setShowManageButton_, 0
        )
