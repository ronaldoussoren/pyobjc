import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorization(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(AuthenticationServices.ASAuthorizationScopeFullName, str)
        self.assertIsInstance(AuthenticationServices.ASAuthorizationScopeEmail, str)
