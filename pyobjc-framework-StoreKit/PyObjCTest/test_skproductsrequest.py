import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestSKProductsRequest(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SKProductsRequestDelegate")
