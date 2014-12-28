from PyObjCTools.TestSupport import *

import StoreKit
import objc

class TestSKRequest (TestCase):
    def test_protocols(self):
        self.assertIsInstance(objc.protocolNamed("SKRequestDelegate"), objc.formal_protocol)

if __name__ == "__main__":
    main()

