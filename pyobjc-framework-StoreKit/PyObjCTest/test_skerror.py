from PyObjCTools.TestSupport import *

import StoreKit


class TestSKError(TestCase):
    def test_constants(self):
        self.assertIsInstance(StoreKit.SKErrorDomain, unicode)

        self.assertEqual(StoreKit.SKErrorUnknown, 0)
        self.assertEqual(StoreKit.SKErrorClientInvalid, 1)
        self.assertEqual(StoreKit.SKErrorPaymentCancelled, 2)
        self.assertEqual(StoreKit.SKErrorPaymentInvalid, 3)
        self.assertEqual(StoreKit.SKErrorPaymentNotAllowed, 4)

        self.assertEqual(StoreKit.SKErrorPrivacyAcknowledgementRequired, 9)
        self.assertEqual(StoreKit.SKErrorUnauthorizedRequestData, 10)

        self.assertEqual(StoreKit.SKErrorInvalidOfferIdentifier, 11)
        self.assertEqual(StoreKit.SKErrorInvalidSignature, 12)
        self.assertEqual(StoreKit.SKErrorMissingOfferParams, 13)
        self.assertEqual(StoreKit.SKErrorInvalidOfferPrice, 14)

        self.assertEqual(StoreKit.SKErrorStoreProductNotAvailable, 5)


if __name__ == "__main__":
    main()
