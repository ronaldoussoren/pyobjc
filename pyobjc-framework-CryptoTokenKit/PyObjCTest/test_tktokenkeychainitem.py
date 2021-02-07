from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTKTokenKeychainItem(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeychainKey.canDecrypt)
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeychainKey.canSign)
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeychainKey.canPerformKeyExchange)
        self.assertResultIsBOOL(CryptoTokenKit.TKTokenKeychainKey.isSuitableForLogin)

        self.assertArgIsBOOL(CryptoTokenKit.TKTokenKeychainKey.setCanDecrypt_, 0)
        self.assertArgIsBOOL(CryptoTokenKit.TKTokenKeychainKey.setCanSign_, 0)
        self.assertArgIsBOOL(
            CryptoTokenKit.TKTokenKeychainKey.setCanPerformKeyExchange_, 0
        )
        self.assertArgIsBOOL(CryptoTokenKit.TKTokenKeychainKey.setSuitableForLogin_, 0)

        self.assertArgIsOut(
            CryptoTokenKit.TKTokenKeychainContents.keyForObjectID_error_, 1
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKTokenKeychainContents.certificateForObjectID_error_, 1
        )
