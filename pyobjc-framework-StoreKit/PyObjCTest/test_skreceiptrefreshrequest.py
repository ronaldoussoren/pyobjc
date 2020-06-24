import StoreKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSKReceiptRefreshRequest(TestCase):
    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsExpired, str)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsRevoked, str)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsVolumePurchase, str)

    @min_os_level("10.14")
    def test_functions(self):
        StoreKit.SKTerminateForInvalidReceipt
