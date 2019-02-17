from PyObjCTools.TestSupport import *

import StoreKit

class TestSKError (TestCase):

    def test_constants(self):
        self.assertIsInstance(StoreKit.SKErrorDomain, unicode)

        self.assertEqual(StoreKit.SKErrorUnknown, 0)
        self.assertEqual(StoreKit.SKErrorClientInvalid, 1)
        self.assertEqual(StoreKit.SKErrorPaymentCancelled, 2)
        self.assertEqual(StoreKit.SKErrorPaymentInvalid, 3)
        self.assertEqual(StoreKit.SKErrorPaymentNotAllowed, 4)

        self.assertEqual(StoreKit.SKErrorPrivacyAcknowledgementRequired, 9)
        self.assertEqual(StoreKit.SKErrorUnauthorizedRequestData, 10)


if __name__ == "__main__":
    main()

