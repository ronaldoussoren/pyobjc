import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASAuthorizationPublicKeyCredentialConstants(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialUserVerificationPreferencePreferred,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialUserVerificationPreferenceRequired,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialUserVerificationPreferenceDiscouraged,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialAttestationKindNone,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialAttestationKindDirect,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialAttestationKindIndirect,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialAttestationKindEnterprise,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialResidentKeyPreferenceDiscouraged,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialResidentKeyPreferencePreferred,
            str,
        )
        self.assertIsInstance(
            AuthenticationServices.ASAuthorizationPublicKeyCredentialResidentKeyPreferenceRequired,
            str,
        )
