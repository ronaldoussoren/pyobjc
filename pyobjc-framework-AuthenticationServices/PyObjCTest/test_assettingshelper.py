import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASSettingsHelper(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASSettingsHelper.openCredentialProviderAppSettingsWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASSettingsHelper.openVerificationCodeAppSettingsWithCompletionHandler_,
            0,
            b"v@",
        )
