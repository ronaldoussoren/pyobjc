import AuthenticationServices  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider(TestCase):
    @min_sdk_level("13.5")
    def test_protocols(self):
        self.assertProtocolExists(
            "ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider"
        )
