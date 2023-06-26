import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestASCredentialProviderExtensionContext(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
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

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialProviderExtensionContext.completeAssertionRequestWithSelectedPasskeyCredential_completionHandler_,
            1,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialProviderExtensionContext.completeRegistrationRequestWithSelectedPasskeyCredential_completionHandler_,
            1,
            b"v" + objc._C_NSBOOL,
        )
