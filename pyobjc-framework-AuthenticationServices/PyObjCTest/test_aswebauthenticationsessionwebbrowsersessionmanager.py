from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASWebAuthenticationSessionWebBrowserSessionManager(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASWebAuthenticationSessionWebBrowserSessionManager.wasLaunchedByAuthenticationServices
        )
