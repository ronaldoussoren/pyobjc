import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionLoginConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionFederationType
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionFederationTypeNone, 0
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionFederationTypeWSTrust,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionFederationTypeDynamicWSTrust,
            2,
        )

        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicy
        )

        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyNone,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyTouchIDOrWatchCurrentSet,
            1 << 0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyTouchIDOrWatchAny,
            1 << 1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyReuseDuringUnlock,
            1 << 2,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyPasswordFallback,
            1 << 3,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.configurationWithOpenIDConfigurationURL_clientID_issuer_completion_,
            3,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomAssertionRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomAssertionRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomAssertionRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomAssertionRequestBodyClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.includePreviousRefreshTokenInLoginRequest
        )
        self.assertArgIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setIncludePreviousRefreshTokenInLoginRequest_,
            0,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomLoginRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomLoginRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomLoginRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomLoginRequestBodyClaims_returningError_,
            1,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomRefreshRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomRefreshRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomRefreshRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomRefreshRequestBodyClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyExchangeRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyExchangeRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyExchangeRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyExchangeRequestBodyClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionLoginConfiguration.setCustomKeyRequestBodyClaims_returningError_,
            1,
        )
