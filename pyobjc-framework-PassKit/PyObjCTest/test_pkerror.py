from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKError(TestCase):
    def test_constants(self):
        self.assertIsInstance(PassKit.PKPassKitErrorDomain, str)
        self.assertIsInstance(PassKit.PKPaymentErrorContactFieldUserInfoKey, str)
        self.assertIsInstance(PassKit.PKPaymentErrorPostalAddressUserInfoKey, str)
        self.assertIsInstance(PassKit.PKAddSecureElementPassErrorDomain, str)

        self.assertEqual(PassKit.PKUnknownError, -1)
        self.assertEqual(PassKit.PKInvalidDataError, 1)
        self.assertEqual(PassKit.PKUnsupportedVersionError, 2)
        self.assertEqual(PassKit.PKInvalidSignature, 3)
        self.assertEqual(PassKit.PKNotEntitledError, 4)

        self.assertEqual(PassKit.PKPaymentUnknownError, -1)
        self.assertEqual(PassKit.PKPaymentShippingContactInvalidError, 1)
        self.assertEqual(PassKit.PKPaymentBillingContactInvalidError, 2)
        self.assertEqual(PassKit.PKPaymentShippingAddressUnserviceableError, 3)

        self.assertEqual(PassKit.PKAddPaymentPassErrorUnsupported, 0)
        self.assertEqual(PassKit.PKAddPaymentPassErrorUserCancelled, 1)
        self.assertEqual(PassKit.PKAddPaymentPassErrorSystemCancelled, 2)

        self.assertEqual(PassKit.PKAddSecureElementPassUnknownError, 0)
        self.assertEqual(PassKit.PKAddSecureElementPassUserCanceledError, 1)
        self.assertEqual(PassKit.PKAddSecureElementPassUnavailableError, 2)
        self.assertEqual(PassKit.PKAddSecureElementPassInvalidConfigurationError, 3)
        self.assertEqual(PassKit.PKAddSecureElementPassDeviceNotSupportedError, 4)
        self.assertEqual(PassKit.PKAddSecureElementPassDeviceNotReadyError, 5)
