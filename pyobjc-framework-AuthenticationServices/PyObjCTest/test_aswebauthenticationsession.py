import AuthenticationServices
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

ASWebAuthenticationSessionCompletionHandler = b"v@@"


class TestASWebAuthenticationSession(TestCase):
    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodeCanceledLogin, 1
        )
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodePresentationContextNotProvided,  # noqa: B950
            2,
        )
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodePresentationContextInvalid,  # noqa: B950
            3,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASWebAuthenticationPresentationContextProviding")

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASWebAuthenticationSession.initWithURL_callbackURLScheme_completionHandler_,  # noqa: B950
            2,
            ASWebAuthenticationSessionCompletionHandler,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASWebAuthenticationSession.prefersEphemeralWebBrowserSession
        )
        self.assertArgIsBOOL(
            AuthenticationServices.ASWebAuthenticationSession.setPrefersEphemeralWebBrowserSession_,  # noqa: B950
            0,
        )

        self.assertResultIsBOOL(AuthenticationServices.ASWebAuthenticationSession.start)

    @min_os_level("10.15.4")
    def test_methods10_15_4(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASWebAuthenticationSession.canStart
        )
