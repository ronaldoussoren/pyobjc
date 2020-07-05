import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionAuthorizationRequest(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationProviderAuthorizationOperationConfigurationRemoved,
            str,
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthorizationRequest.isCallerManaged
        )
