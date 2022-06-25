from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401
import objc


class TestSWCollaborationButtonView(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            objc.lookUpClass("_SWCollaborationButtonView").setShowManageButton_, 0
        )


# SharedWithYou._SWCollaborationButtonView.setShowManageButton_, 0
