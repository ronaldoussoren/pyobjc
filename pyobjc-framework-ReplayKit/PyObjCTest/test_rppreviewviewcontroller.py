from PyObjCTools.TestSupport import TestCase

import ReplayKit  # noqa: F401
import objc


class TestRPPreviewViewController(TestCase):
    def test_protocols(self):
        objc.protocolNamed("RPPreviewViewControllerDelegate")
