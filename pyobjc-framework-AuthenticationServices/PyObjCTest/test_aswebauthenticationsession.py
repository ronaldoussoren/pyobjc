from PyObjCTools.TestSupport import *

import AuthenticationServices

ASWebAuthenticationSessionCompletionHandler = b"v@@"


class TestASWebAuthenticationSession(TestCase):
    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodeCanceledLogin, 1
        )
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodePresentationContextNotProvided,
            2,
        )
        self.assertEqual(
            AuthenticationServices.ASWebAuthenticationSessionErrorCodePresentationContextInvalid,
            3,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASWebAuthenticationPresentationContextProviding")

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASWebAuthenticationSession.initWithURL_callbackURLScheme_completionHandler_,
            2,
            ASWebAuthenticationSessionCompletionHandler,
        )

        self.assertResultIsBOOL(
            AuthenticationServices.ASWebAuthenticationSession.prefersEphemeralWebBrowserSession
        )
        self.assertArgIsBOOL(
            AuthenticationServices.ASWebAuthenticationSession.setPrefersEphemeralWebBrowserSession_,
            0,
        )

        self.assertResultIsBOOL(AuthenticationServices.ASWebAuthenticationSession.start)
