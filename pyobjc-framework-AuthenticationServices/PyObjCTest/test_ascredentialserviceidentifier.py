import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASCredentialServiceIdentifier(TestCase):
    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASCredentialServiceIdentifierTypeDomain, 0
        )
        self.assertEqual(AuthenticationServices.ASCredentialServiceIdentifierTypeURL, 1)
