import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestASAuthorizationWebBrowserPublicKeyCredentialManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationState
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationStateAuthorized,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationStateDenied,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManagerAuthorizationStateNotDetermined,
            2,
        )

    @min_sdk_level("14.4")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest"
        )

    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManager.requestAuthorizationForPublicKeyCredentials_,
            0,
            b"vq",
        )

        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationWebBrowserPublicKeyCredentialManager.platformCredentialsForRelyingParty_completionHandler_,
            1,
            b"v@",
        )
