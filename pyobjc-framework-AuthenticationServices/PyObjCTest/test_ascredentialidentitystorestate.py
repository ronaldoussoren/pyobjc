import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASCredentialIdentityStoreState(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASCredentialIdentityStoreState.isEnabled
        )
        self.assertResultIsBOOL(
            AuthenticationServices.ASCredentialIdentityStoreState.supportsIncrementalUpdates
        )
