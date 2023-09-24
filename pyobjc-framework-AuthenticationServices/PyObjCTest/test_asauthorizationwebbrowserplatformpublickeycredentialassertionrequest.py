import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequestHelper(
    AuthenticationServices.NSObject
):
    def shouldShowHybridTransport(self):
        return 1

    def setShouldShowHybridTransport_(self, a):
        pass


class TestASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest(
    TestCase
):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest"
        )

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequestHelper.shouldShowHybridTransport
        )
        self.assertArgIsBOOL(
            TestASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequestHelper.setShouldShowHybridTransport_,
            0,
        )
