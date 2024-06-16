import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorizationPlatformPublicKeyCredentialRegistrationRequest(TestCase):
    def test_enum(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationPlatformPublicKeyCredentialRegistrationRequestStyle
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationPlatformPublicKeyCredentialRegistrationRequestStyleStandard,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationPlatformPublicKeyCredentialRegistrationRequestStyleConditional,
            1,
        )
