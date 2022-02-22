import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationOpenIDRequest(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(
            AuthenticationServices.ASAuthorizationOpenIDOperation, str
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationImplicit, str
        )
        self.assertIsInstance(AuthenticationServices.ASAuthorizationOperationLogin, str)
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationRefresh, str
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationLogout, str
        )
