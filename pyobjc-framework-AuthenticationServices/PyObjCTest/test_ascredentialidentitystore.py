import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestASCredentialIdentityStore(TestCase):
    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASCredentialIdentityStoreErrorCodeInternalError, 0
        )
        self.assertEqual(
            AuthenticationServices.ASCredentialIdentityStoreErrorCodeStoreDisabled, 1
        )
        self.assertEqual(
            AuthenticationServices.ASCredentialIdentityStoreErrorCodeStoreBusy, 2
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialIdentityStore.getCredentialIdentityStoreStateWithCompletion_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialIdentityStore.saveCredentialIdentities_completion_,
            1,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialIdentityStore.removeCredentialIdentities_completion_,
            1,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialIdentityStore.removeAllCredentialIdentitiesWithCompletion_,
            0,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBlock(
            AuthenticationServices.ASCredentialIdentityStore.replaceCredentialIdentitiesWithIdentities_completion_,
            1,
            b"v" + objc._C_NSBOOL + b"@",
        )
