import AuthenticationServices  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest(
    TestCase
):
    @min_sdk_level("14.4")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest"
        )
