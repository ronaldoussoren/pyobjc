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
