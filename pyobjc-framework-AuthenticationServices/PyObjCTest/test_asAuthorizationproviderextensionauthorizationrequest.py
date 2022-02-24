import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationProviderExtensionAuthorizationRequest(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationProviderAuthorizationOperationConfigurationRemoved,
            str,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthorizationRequest.isCallerManaged
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthorizationRequest.isUserInterfaceEnabled
        )
