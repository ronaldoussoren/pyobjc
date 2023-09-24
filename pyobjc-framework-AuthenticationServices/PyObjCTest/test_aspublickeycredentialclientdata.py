import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASPublicKeyCredentialClientData(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASPublicKeyCredentialClientDataCrossOriginValue
        )
        self.assertEqual(
            AuthenticationServices.ASPublicKeyCredentialClientDataCrossOriginValueNotSet,
            0,
        )
        self.assertEqual(
            AuthenticationServices.ASPublicKeyCredentialClientDataCrossOriginValueCrossOrigin,
            1,
        )
        self.assertEqual(
            AuthenticationServices.ASPublicKeyCredentialClientDataCrossOriginValueSameOriginWithAncestors,
            2,
        )
