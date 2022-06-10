import AuthenticationServices
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorization(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASAuthorizationControllerDelegate")
        objc.protocolNamed("ASAuthorizationControllerPresentationContextProviding")

    def test_constants(self):
        self.assertIsEnumType(
            AuthenticationServices.ASAuthorizationControllerRequestOptions
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationControllerRequestOptionPreferImmediatelyAvailableCredentials,
            1 << 0,
        )
