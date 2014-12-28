from PyObjCTools.TestSupport import *

import StoreKit
import objc

class TestSKDownload (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(StoreKit.SKPaymentQueue.canMakePayments)

    def test_protocols(self):
        self.assertIsInstance(objc.protocolNamed("SKPaymentTransactionObserver"), objc.formal_protocol)

if __name__ == "__main__":
    main()

