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
        self.assertEqual(
            AuthenticationServices.ASAuthorizationErrorNotInteractive, 1005
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationErrorMatchedExcludedCredential, 1006
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationErrorCredentialImport, 1007
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationErrorCredentialExport, 1008
        )
