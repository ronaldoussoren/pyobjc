import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASCredentialServiceIdentifier(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AuthenticationServices.ASCredentialServiceIdentifierType)

    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASCredentialServiceIdentifierTypeDomain, 0
        )
        self.assertEqual(AuthenticationServices.ASCredentialServiceIdentifierTypeURL, 1)
