from PyObjCTools.TestSupport import *

import AuthenticationServices

class TestASAuthorizationAppleIDButton (TestCase):
    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeDefault, 0)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignUp, 1)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeContinue, 2)

        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhite, 0)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhiteOutline, 1)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleBlack, 2)
