import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionUserLoginConfiguration(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomAssertionRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomAssertionRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomAssertionRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomAssertionRequestBodyClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomLoginRequestHeaderClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomLoginRequestHeaderClaims_returningError_,
            1,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomLoginRequestBodyClaims_returningError_
        )
        self.assertArgIsOut(
            AuthenticationServices.ASAuthorizationProviderExtensionUserLoginConfiguration.setCustomLoginRequestBodyClaims_returningError_,
            1,
        )
