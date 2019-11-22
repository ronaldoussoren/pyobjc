from PyObjCTools.TestSupport import *

import StoreKit


class TestSKReceiptRefreshRequest(TestCase):
    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsExpired, unicode)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsRevoked, unicode)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsVolumePurchase, unicode)

    @min_os_level("10.14")
    def test_functions(self):
        StoreKit.SKTerminateForInvalidReceipt


if __name__ == "__main__":
    main()
