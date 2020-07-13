from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKAddPaymentPassRequest(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKAddPaymentPassStylePayment, 0)
        self.assertEqual(PassKit.PKAddPaymentPassStyleAccess, 1)

    def test_methods(self):
        self.assertResultIsBOOL(
            PassKit.PKAddPaymentPassRequestConfiguration.requiresFelicaSecureElement
        )
        self.assertArgIsBOOL(
            PassKit.PKAddPaymentPassRequestConfiguration.setRequiresFelicaSecureElement_,
            0,
        )
