import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASWebAuthenticationSessionCallback(TestCase):
    @min_os_level("14.4")
    def test_methods14_4(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASWebAuthenticationSessionCallback.matchesURL_
        )
