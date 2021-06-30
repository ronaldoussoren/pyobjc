import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASExtensionErrors(TestCase):
    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASExtensionErrorCodeFailed, 0)
        self.assertEqual(AuthenticationServices.ASExtensionErrorCodeUserCanceled, 1)
        self.assertEqual(
            AuthenticationServices.ASExtensionErrorCodeUserInteractionRequired, 100
        )
        self.assertEqual(
            AuthenticationServices.ASExtensionErrorCodeCredentialIdentityNotFound, 101
        )

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(AuthenticationServices.ASExtensionErrorDomain, str)
        self.assertIsInstance(
            AuthenticationServices.ASExtensionLocalizedFailureReasonErrorKey, str
        )
