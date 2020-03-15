import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit


class TestNSFontAssetRequest(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSFontAssetRequestOptionUsesStandardUI, 1 << 0)

    @onlyOn64Bit
    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            AppKit.NSFontAssetRequest.downloadFontAssetsWithCompletionHandler_, 0, b"Z@"
        )
