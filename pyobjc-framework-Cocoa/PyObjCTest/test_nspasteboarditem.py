import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSPasteboardItem(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setDataProvider_forTypes_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setData_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setString_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboardItem.setPropertyList_forType_)

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("NSPasteboardItemDataProvider")
