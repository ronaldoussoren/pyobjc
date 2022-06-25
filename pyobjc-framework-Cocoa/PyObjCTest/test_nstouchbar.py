import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTouchBar(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTouchBar.isVisible)
        # self.assertArgIsBOOL(AppKit.NSTouchBar.setVisible_, 0)

        self.assertResultIsBOOL(
            AppKit.NSApplication.isAutomaticCustomizeTouchBarMenuItemEnabled
        )
        self.assertArgIsBOOL(
            AppKit.NSApplication.setAutomaticCustomizeTouchBarMenuItemEnabled_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            AppKit.NSTouchBar.isAutomaticCustomizeTouchBarMenuItemEnabled
        )
        self.assertArgIsBOOL(
            AppKit.NSTouchBar.setAutomaticCustomizeTouchBarMenuItemEnabled_, 0
        )

    @min_sdk_level("10.12")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSTouchBarDelegate")
        self.assertProtocolExists("NSTouchBarProvider")
