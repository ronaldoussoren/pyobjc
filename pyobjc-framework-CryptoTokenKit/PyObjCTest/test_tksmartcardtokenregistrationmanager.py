from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTKSmartCardTokenRegistrationManager(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            CryptoTokenKit.TKSmartCardTokenRegistrationManager.registerSmartCardWithTokenID_promptMessage_error_
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCardTokenRegistrationManager.registerSmartCardWithTokenID_promptMessage_error_,
            2,
        )

        self.assertResultIsBOOL(
            CryptoTokenKit.TKSmartCardTokenRegistrationManager.unregisterSmartCardWithTokenID_error_
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKSmartCardTokenRegistrationManager.unregisterSmartCardWithTokenID_error_,
            1,
        )
