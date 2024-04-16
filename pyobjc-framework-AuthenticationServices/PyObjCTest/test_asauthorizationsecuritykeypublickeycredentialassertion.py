import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationSecurityKeyPublicKeyCredentialAssertion(TestCase):
    @min_os_level("14.5")
    def test_methods14_5(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationSecurityKeyPublicKeyCredentialAssertion.appID
        )
