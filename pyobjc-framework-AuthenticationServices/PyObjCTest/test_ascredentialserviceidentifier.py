import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASCredentialServiceIdentifier(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AuthenticationServices.ASCredentialServiceIdentifierType)
        self.assertEqual(
            AuthenticationServices.ASCredentialServiceIdentifierTypeDomain, 0
        )
        self.assertEqual(AuthenticationServices.ASCredentialServiceIdentifierTypeURL, 1)
        self.assertEqual(AuthenticationServices.ASCredentialServiceIdentifierTypeApp, 2)
