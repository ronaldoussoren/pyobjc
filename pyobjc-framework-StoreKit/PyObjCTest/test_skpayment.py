from PyObjCTools.TestSupport import *

import StoreKit


class TestSKPayment(TestCase):
    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(StoreKit.SKPayment.simulatesAskToBuyInSandbox)
        self.assertArgIsBOOL(
            StoreKit.SKMutablePayment.setSimulatesAskToBuyInSandbox_, 0
        )


if __name__ == "__main__":
    main()
