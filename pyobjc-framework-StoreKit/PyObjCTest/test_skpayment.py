import StoreKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSKPayment(TestCase):
    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(StoreKit.SKPayment.simulatesAskToBuyInSandbox)
        self.assertArgIsBOOL(
            StoreKit.SKMutablePayment.setSimulatesAskToBuyInSandbox_, 0
        )
