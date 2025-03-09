import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSPasteboardItem(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setDataProvider_forTypes_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setData_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setString_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setPropertyList_forType_)

    @min_os_level("15.4")
    def testMethods15_4(self):
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

    @min_sdk_level("10.6")
    def testProtocols(self):
        self.assertProtocolExists("NSPasteboardItemDataProvider")
