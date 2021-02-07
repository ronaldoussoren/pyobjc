import objc
import StoreKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestSKPaymentQueueHelper(StoreKit.NSObject):
    def paymentQueue_shouldContinueTransaction_inStorefront_(self, a, b, c):
        return 1

    def paymentQueue_shouldAddStorePayment_forProduct_(self, a, b, c):
        return 1


class TestSKPaymentQueue(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(StoreKit.SKPaymentQueue.canMakePayments)

        self.assertResultIsBOOL(
            TestSKPaymentQueueHelper.paymentQueue_shouldContinueTransaction_inStorefront_
        )

        self.assertResultIsBOOL(
            TestSKPaymentQueueHelper.paymentQueue_shouldAddStorePayment_forProduct_
        )

    def test_protocols(self):
        self.assertIsInstance(
            objc.protocolNamed("SKPaymentTransactionObserver"), objc.formal_protocol
        )

    @min_sdk_level("10.15")
    def test_protocols10_15(self):
        self.assertIsInstance(
            objc.protocolNamed("SKPaymentQueueDelegate"), objc.formal_protocol
        )
