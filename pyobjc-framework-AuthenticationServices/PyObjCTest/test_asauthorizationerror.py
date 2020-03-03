import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorization(TestCase):
    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASAuthorizationErrorUnknown, 1000)
        self.assertEqual(AuthenticationServices.ASAuthorizationErrorCanceled, 1001)
        self.assertEqual(
            AuthenticationServices.ASAuthorizationErrorInvalidResponse, 1002
        )
        self.assertEqual(AuthenticationServices.ASAuthorizationErrorNotHandled, 1003)
        self.assertEqual(AuthenticationServices.ASAuthorizationErrorFailed, 1004)
