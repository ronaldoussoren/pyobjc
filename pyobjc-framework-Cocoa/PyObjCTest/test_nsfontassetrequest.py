import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFontAssetRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSFontAssetRequestOptions)

    def testConstants(self):
        self.assertEqual(AppKit.NSFontAssetRequestOptionUsesStandardUI, 1 << 0)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            AppKit.NSFontAssetRequest.downloadFontAssetsWithCompletionHandler_, 0, b"Z@"
        )
