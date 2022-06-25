from PyObjCTools.TestSupport import TestCase
import PassKit  # noqa: F401


class TestPKDisbursementAuthorizationController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("PKDisbursementAuthorizationControllerDelegate")
