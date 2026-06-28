import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorization(TestCase):
    def test_enums(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationControllerRequestOptions
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationControllerRequestOptionPreferImmediatelyAvailableCredentials,
            1 << 0,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationControllerDelegate", AuthenticationServices
        )
        self.assertProtocolExists(
            "ASAuthorizationControllerPresentationContextProviding",
            AuthenticationServices,
        )
