from PyObjCTools.TestSupport import *

import StoreKit

class TestSKDownload (TestCase):

    def test_methods(self):
        self.assertResultIsBOOL(StoreKit.SKProduct.downloadable)

if __name__ == "__main__":
    main()

