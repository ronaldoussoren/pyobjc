from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import PassKit


class TestPKPassLibrary(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(PassKit.PKPassLibraryNotificationKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKAutomaticPassPresentationSuppressionResult)
        self.assertIsEnumType(PassKit.PKPassLibraryAddPassesStatus)

    def test_constants(self):
        self.assertEqual(PassKit.PKPassLibraryDidAddPasses, 0)
        self.assertEqual(PassKit.PKPassLibraryShouldReviewPasses, 1)
        self.assertEqual(PassKit.PKPassLibraryDidCancelAddPasses, 2)

        self.assertEqual(
            PassKit.PKAutomaticPassPresentationSuppressionResultNotSupported, 0
        )
        self.assertEqual(
            PassKit.PKAutomaticPassPresentationSuppressionResultAlreadyPresenting, 1
        )
        self.assertEqual(PassKit.PKAutomaticPassPresentationSuppressionResultDenied, 2)
        self.assertEqual(
            PassKit.PKAutomaticPassPresentationSuppressionResultCancelled, 3
        )
        self.assertEqual(PassKit.PKAutomaticPassPresentationSuppressionResultSuccess, 4)

        self.assertIsInstance(PassKit.PKPassLibraryDidChangeNotification, str)
        self.assertIsInstance(
            PassKit.PKPassLibraryRemotePaymentPassesDidChangeNotification, str
        )

        self.assertIsInstance(PassKit.PKPassLibraryAddedPassesUserInfoKey, str)
        self.assertIsInstance(PassKit.PKPassLibraryReplacementPassesUserInfoKey, str)
        self.assertIsInstance(PassKit.PKPassLibraryRemovedPassInfosUserInfoKey, str)

        self.assertIsInstance(PassKit.PKPassLibraryPassTypeIdentifierUserInfoKey, str)
        self.assertIsInstance(PassKit.PKPassLibrarySerialNumberUserInfoKey, str)

        self.assertIsEnumType(PassKit.PKPassLibraryCapability)
        self.assertEqual(PassKit.PKPassLibraryCapabilityBackgroundAddPasses, 0)

        self.assertIsEnumType(PassKit.PKPassLibraryAuthorizationStatus)
        self.assertEqual(PassKit.PKPassLibraryAuthorizationStatusNotDetermined, -1)
        self.assertEqual(PassKit.PKPassLibraryAuthorizationStatusDenied, 0)
        self.assertEqual(PassKit.PKPassLibraryAuthorizationStatusAuthorized, 1)
        self.assertEqual(PassKit.PKPassLibraryAuthorizationStatusRestricted, 2)

    def test_methods(self):
        self.assertResultIsBOOL(PassKit.PKPassLibrary.isPassLibraryAvailable)

        self.assertArgIsBlock(
            PassKit.PKPassLibrary.requestAutomaticPassPresentationSuppressionWithResponseHandler_,
            0,
            b"v" + objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            PassKit.PKPassLibrary.isSuppressingAutomaticPassPresentation
        )
        self.assertResultIsBOOL(PassKit.PKPassLibrary.isPaymentPassActivationAvailable)
        self.assertResultIsBOOL(PassKit.PKPassLibrary.isPaymentPassActivationAvailable)
        self.assertResultIsBOOL(PassKit.PKPassLibrary.containsPass_)
        self.assertResultIsBOOL(PassKit.PKPassLibrary.replacePassWithPass_)

        self.assertArgIsBlock(
            PassKit.PKPassLibrary.addPasses_withCompletionHandler_,
            1,
            b"v" + objc._C_NSInteger,
        )

        self.assertResultIsBOOL(
            PassKit.PKPassLibrary.canAddPaymentPassWithPrimaryAccountIdentifier_
        )
        self.assertResultIsBOOL(
            PassKit.PKPassLibrary.canAddSecureElementPassWithPrimaryAccountIdentifier_
        )
        self.assertResultIsBOOL(PassKit.PKPassLibrary.canAddFelicaPass)

        self.assertArgIsBlock(
            PassKit.PKPassLibrary.activatePaymentPass_withActivationData_completion_,
            2,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            PassKit.PKPassLibrary.activatePaymentPass_withActivationCode_completion_,
            2,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            PassKit.PKPassLibrary.activateSecureElementPass_withActivationData_completion_,
            2,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            PassKit.PKPassLibrary.signData_withSecureElementPass_completion_, 2, b"v@@@"
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            PassKit.PKPassLibrary.encryptedServiceProviderDataForSecureElementPass_completion_,
            1,
            b"v@@",
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            PassKit.PKPassLibrary.requestAuthorizationForCapability_completion_,
            1,
            b"vq",
        )
