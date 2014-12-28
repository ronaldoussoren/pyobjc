from PyObjCTools.TestSupport import *

import StoreKit

class TestSKPaymentTransaction (TestCase):

    def test_constants(self):
        self.assertEqual(StoreKit.SKPaymentTransactionStatePurchasing, 0)
        self.assertEqual(StoreKit.SKPaymentTransactionStatePurchased, 1)
        self.assertEqual(StoreKit.SKPaymentTransactionStateFailed, 2)
        self.assertEqual(StoreKit.SKPaymentTransactionStateRestored, 3)
        self.assertEqual(StoreKit.SKPaymentTransactionStateDeferred, 4)

if __name__ == "__main__":
    main()

