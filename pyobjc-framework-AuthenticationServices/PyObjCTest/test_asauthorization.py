from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASAuthorization(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationScopeFullName, unicode
        )
        self.assertIsInstance(AuthenticationServices.ASAuthorizationScopeEmail, unicode)
