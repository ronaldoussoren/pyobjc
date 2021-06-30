import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASCredentialIdentityStoreState(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            AuthenticationServices.ASCredentialIdentityStoreState.isEnabled
        )
        self.assertResultIsBOOL(
            AuthenticationServices.ASCredentialIdentityStoreState.supportsIncrementalUpdates
        )
