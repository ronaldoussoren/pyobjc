import SecurityUI
from PyObjCTools.TestSupport import TestCase


class TestCFCertificatePresentation(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            SecurityUI.SFCertificatePresentation.presentSheetInWindow_dismissHandler_,
            1,
            b"v",
        )
