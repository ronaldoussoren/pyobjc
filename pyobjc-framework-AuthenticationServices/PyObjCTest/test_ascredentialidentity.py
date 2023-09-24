import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestASCredentialIdentityHelper(AuthenticationServices.NSObject):
    def rank(self):
        return 1

    def setRank_(self, a):
        pass


class TestASCredentialIdentity(TestCase):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("ASCredentialIdentity")

    def test_protocol_methods(self):
        self.assertResultHasType(TestASCredentialIdentityHelper.rank, objc._C_NSInteger)
        self.assertArgHasType(
            TestASCredentialIdentityHelper.setRank_, 0, objc._C_NSInteger
        )
