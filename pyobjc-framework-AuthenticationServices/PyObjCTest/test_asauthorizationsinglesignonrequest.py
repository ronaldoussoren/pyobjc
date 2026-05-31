import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationSingleSignOnRequest(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationSingleSignOnRequest.isUserInterfaceEnabled
        )
        self.assertArgIsBOOL(
            AuthenticationServices.ASAuthorizationSingleSignOnRequest.setUserInterfaceEnabled_,
            0,
        )
