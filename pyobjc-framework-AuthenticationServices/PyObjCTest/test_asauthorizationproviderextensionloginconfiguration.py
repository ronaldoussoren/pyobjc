import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionLoginConfiguration(TestCase):
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
