from PyObjCTools.TestSupport import *

import StoreKit

try:
    unicode
except NameError:
    unicode = str

class TestSKReceiptRefreshRequest (TestCase):
    @min_os_level('10.9')
    def test_constants(self):
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsExpired, unicode)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsRevoked, unicode)
        self.assertIsInstance(StoreKit.SKReceiptPropertyIsVolumePurchase, unicode)

if __name__ == "__main__":
    main()

