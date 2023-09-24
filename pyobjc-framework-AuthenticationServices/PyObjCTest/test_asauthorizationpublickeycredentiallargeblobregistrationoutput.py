import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput.isSupported
        )
