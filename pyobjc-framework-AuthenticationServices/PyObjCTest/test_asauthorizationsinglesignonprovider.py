from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASAuthorizationSingleSignOnProvider(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationSingleSignOnProvider.canPerformAuthorization
        )
