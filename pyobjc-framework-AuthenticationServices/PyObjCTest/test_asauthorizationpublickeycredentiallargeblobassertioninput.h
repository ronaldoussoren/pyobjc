import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationPublicKeyCredentialLargeBlobAssertionInput(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperation)
        self.assertEqual(AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperationRead, 0)
        self.assertEqual(AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperationWrite, 1)
