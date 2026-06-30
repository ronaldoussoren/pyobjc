import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFontAssetRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSFontAssetRequestOptions)
        self.assertEqual(AppKit.NSFontAssetRequestOptionUsesStandardUI, 1 << 0)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsBlock(
            AppKit.NSFontAssetRequest.downloadFontAssetsWithCompletionHandler_, 0, b"Z@"
        )
