import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPasteboardItem(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setDataProvider_forTypes_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setData_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setString_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setPropertyList_forType_)

    @min_os_level("15.4")
    def test_methods15_4(self):
        self.assertArgIsBlock(
            AppKit.NSPasteboardItem.detectPatternsForPatterns_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AppKit.NSPasteboardItem.detectValuesForPatterns_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AppKit.NSPasteboardItem.detectMetadataForTypes_completionHandler_, 1, b"v@@"
        )

    def test_protocols(self):
        self.assertProtocolExists("NSPasteboardItemDataProvider", AppKit)
