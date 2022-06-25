import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestProtocols(TestCase):
    def test_formal_protocols(self):
        self.assertProtocolExists("SKPaymentTransactionObserver")
        self.assertProtocolExists("SKProductsRequestDelegate")
        self.assertProtocolExists("SKRequestDelegate")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(StoreKit)
