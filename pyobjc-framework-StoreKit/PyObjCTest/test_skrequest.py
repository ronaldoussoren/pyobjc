import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestSKRequest(TestCase):
    def test_protocols(self):
        self.assertIsInstance(
            objc.protocolNamed("SKRequestDelegate"), objc.formal_protocol
        )
