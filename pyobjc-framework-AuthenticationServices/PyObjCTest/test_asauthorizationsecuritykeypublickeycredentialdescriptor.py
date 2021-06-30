import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationSecurityKeyPublicKeyCredentialDescriptor(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportUSB,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportNFC,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationSecurityKeyPublicKeyCredentialDescriptorTransportBluetooth,
            str,
        )

    @min_os_level("12.0")
    def test_functions12_0(self):
        AuthenticationServices.ASAuthorizationAllSupportedPublicKeyCredentialDescriptorTransports
