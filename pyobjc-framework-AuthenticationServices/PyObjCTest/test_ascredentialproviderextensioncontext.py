import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestASCredentialProviderExtensionContext(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialProviderExtensionContext.completeRequestWithSelectedCredential_completionHandler_,
            1,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialProviderExtensionContext.completeRequestReturningItems_completionHandler_,
            1,
            b"v" + objc._C_NSBOOL,
        )
