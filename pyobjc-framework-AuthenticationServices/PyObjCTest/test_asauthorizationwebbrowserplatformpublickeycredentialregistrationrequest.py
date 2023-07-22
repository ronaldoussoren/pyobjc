import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequestHelper(
    AuthenticationServices.NSObject
):
    def shouldShowHybridTransport(self):
        return 1

    def setShouldShowHybridTransport_(self, a):
        pass


class TestASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest(
    TestCase
):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest"
        )

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequestHelper.shouldShowHybridTransport
        )
        self.assertArgIsBOOL(
            TestASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequestHelper.setShouldShowHybridTransport_,
            0,
        )
