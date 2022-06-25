from PyObjCTools.TestSupport import TestCase

import ReplayKit  # noqa: F401


class TestRPPreviewViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("RPPreviewViewControllerDelegate")
