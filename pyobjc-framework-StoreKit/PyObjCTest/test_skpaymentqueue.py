from PyObjCTools.TestSupport import *

import StoreKit

class TestSKDownload (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(StoreKit.SKPaymentQueue.canMakePayments)

if __name__ == "__main__":
    main()

