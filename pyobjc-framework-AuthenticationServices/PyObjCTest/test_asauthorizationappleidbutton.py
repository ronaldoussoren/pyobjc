import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorizationAppleIDButton(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AuthenticationServices.ASAuthorizationAppleIDButtonStyle)
        self.assertIsEnumType(AuthenticationServices.ASAuthorizationAppleIDButtonType)

    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignIn, 0
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonTypeContinue, 1
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignUp, 2
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonTypeDefault,
            AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignIn,
        )

        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhite, 0
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhiteOutline, 1
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDButtonStyleBlack, 2
        )
