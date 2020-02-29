import AuthenticationServices
from PyObjCTools.TestSupport import *


class TestASAuthorizationOpenIDRequest(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationImplicit, unicode
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationLogin, unicode
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationRefresh, unicode
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationOperationLogout, unicode
        )
