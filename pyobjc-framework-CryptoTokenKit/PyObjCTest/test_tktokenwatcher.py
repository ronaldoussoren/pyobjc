from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTKTokenWatcher(TestCase):
    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertArgIsBlock(
            CryptoTokenKit.TKTokenWatcher.initWithInsertionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            CryptoTokenKit.TKTokenWatcher.addRemovalHandler_forTokenID_, 0, b"v@"
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertArgIsBlock(
            CryptoTokenKit.TKTokenWatcher.setInsertionHandler_, 0, b"v@"
        )
