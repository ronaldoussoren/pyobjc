from PyObjCTools.TestSupport import *

import StoreKit
import objc

class TestSKProductsRequest (TestCase):
    def test_protocols(self):
        self.assertIsInstance(objc.protocolNamed("SKProductsRequestDelegate"), objc.formal_protocol)

if __name__ == "__main__":
    main()

