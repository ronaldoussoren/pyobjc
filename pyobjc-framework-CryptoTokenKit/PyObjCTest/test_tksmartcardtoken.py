from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import CryptoTokenKit


class TestTKSmartCardTokenHelper(CryptoTokenKit.NSObject):
    def tokenDriver_createTokenForSmartCard_AID_error_(self, d, sc, a, e):
        return 1


class TestTKSmartCardToken(TestCase):
    @min_sdk_level("10.12")
    def test_protocols(self):
        self.assertProtocolExists("TKSmartCardTokenDriverDelegate", CryptoTokenKit)

    @min_sdk_level("10.12")
    def test_methods(self):
        self.assertArgHasType(
            TestTKSmartCardTokenHelper.tokenDriver_createTokenForSmartCard_AID_error_,
            3,
            b"o^@",
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCardTokenSession.getSmartCardWithError_, 0
        )
