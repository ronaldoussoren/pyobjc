import objc
import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestProtocols(TestCase):
    def test_formal_protocols(self):
        self.assertIsInstance(
            objc.protocolNamed("SKPaymentTransactionObserver"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("SKProductsRequestDelegate"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("SKRequestDelegate"), objc.formal_protocol
        )
