from PyObjCTools.TestSupport import TestCase
import objc
import PassKit  # noqa: F401


class TestPKDisbursementAuthorizationController(TestCase):
    def test_protocols(self):
        objc.protocolNamed("PKDisbursementAuthorizationControllerDelegate")
