import objc

from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CryptoTokenKit


class TestTKSmartCardTokenHelper(CryptoTokenKit.NSObject):
    def tokenDriver_createTokenForSmartCard_AID_error_(self, d, sc, a, e):
        return 1


class TestTKSmartCardToken(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("TKSmartCardTokenDriverDelegate")

    @min_sdk_level("10.12")
    def testMethods(self):
        self.assertArgHasType(
            TestTKSmartCardTokenHelper.tokenDriver_createTokenForSmartCard_AID_error_,
            3,
            b"o^@",
        )
