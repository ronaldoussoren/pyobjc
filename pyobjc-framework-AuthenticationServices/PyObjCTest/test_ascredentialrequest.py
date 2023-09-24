import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestASCredentialRequestHelper(AuthenticationServices.NSObject):
    def type(self):  # noqa: A003
        return 1

    def setType_(self, a):
        pass


class TestASCredentialRequest(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AuthenticationServices.ASCredentialRequestType)
        self.assertEqual(AuthenticationServices.ASCredentialRequestTypePassword, 0)
        self.assertEqual(
            AuthenticationServices.ASCredentialRequestTypePasskeyAssertion, 1
        )

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("ASCredentialRequest")

    def test_protocol_methods(self):
        self.assertResultHasType(TestASCredentialRequestHelper.type, objc._C_NSInteger)
