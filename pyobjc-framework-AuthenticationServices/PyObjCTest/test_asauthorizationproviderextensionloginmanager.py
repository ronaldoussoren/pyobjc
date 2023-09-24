import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionLoginManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyType
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeUserDeviceSigning,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeUserDeviceEncryption,
            2,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeUserSecureEnclaveKey,
            3,
        )

        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeSharedDeviceSigning,
            4,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeSharedDeviceEncryption,
            5,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeCurrentDeviceSigning,
            10,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeCurrentDeviceEncryption,
            11,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionKeyTypeUserSmartCard,
            20,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.isDeviceRegistered
        )
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.isUserRegistered
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.saveLoginConfiguration_error_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.saveLoginConfiguration_error_,
            1,
        )

        self.assertResultIsCFRetained(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.copyKeyForKeyType_
        )
        self.assertResultIsCFRetained(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.copyIdentityForKeyType_
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.userNeedsReauthenticationWithCompletion_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.presentRegistrationViewControllerWithCompletion_,
            0,
            b"v@",
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.saveUserLoginConfiguration_error_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginManager.saveUserLoginConfiguration_error_,
            1,
        )
