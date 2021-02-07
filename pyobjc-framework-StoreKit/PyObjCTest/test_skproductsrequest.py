import objc
import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestSKProductsRequest(TestCase):
    def test_protocols(self):
        self.assertIsInstance(
            objc.protocolNamed("SKProductsRequestDelegate"), objc.formal_protocol
        )
