import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSSharingServicePickerTouchBarItem(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSSharingServicePickerTouchBarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSSharingServicePickerTouchBarItem.setEnabled_, 0)

    @min_sdk_level("10.12")
    def testProtocols10_12(self):
        self.assertProtocolExists("NSSharingServicePickerTouchBarItemDelegate")
