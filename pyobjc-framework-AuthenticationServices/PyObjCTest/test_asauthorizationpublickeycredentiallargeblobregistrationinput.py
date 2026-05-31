import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobSupportRequirement
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobSupportRequirementRequired,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobSupportRequirementPreferred,
            1,
        )
