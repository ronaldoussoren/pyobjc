import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSPanel(TestCase):
    def testFunctions(self):
        self.assertArgIsPrintf(AppKit.NSRunAlertPanel, 1)
        self.assertArgIsPrintf(AppKit.NSRunInformationalAlertPanel, 1)
        self.assertArgIsPrintf(AppKit.NSRunCriticalAlertPanel, 1)
        self.assertArgIsPrintf(AppKit.NSRunAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(AppKit.NSRunInformationalAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(AppKit.NSRunCriticalAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(AppKit.NSBeginAlertSheet, 9)
        self.assertArgIsSEL(
            AppKit.NSBeginAlertSheet, 6, b"v@:@" + objc._C_NSInteger + b"^v"
        )
        self.assertArgIsSEL(
            AppKit.NSBeginAlertSheet, 7, b"v@:@" + objc._C_NSInteger + b"^v"
        )
        self.assertArgHasType(AppKit.NSBeginAlertSheet, 8, b"^v")
        self.assertArgIsPrintf(AppKit.NSBeginInformationalAlertSheet, 9)
        self.assertArgIsSEL(
            AppKit.NSBeginInformationalAlertSheet,
            6,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSBeginInformationalAlertSheet,
            7,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(AppKit.NSBeginInformationalAlertSheet, 8, b"^v")
        self.assertArgIsPrintf(AppKit.NSBeginCriticalAlertSheet, 9)
        self.assertArgIsSEL(
            AppKit.NSBeginCriticalAlertSheet, 6, b"v@:@" + objc._C_NSInteger + b"^v"
        )
        self.assertArgIsSEL(
            AppKit.NSBeginCriticalAlertSheet, 7, b"v@:@" + objc._C_NSInteger + b"^v"
        )
        self.assertArgHasType(AppKit.NSBeginCriticalAlertSheet, 8, b"^v")
        self.assertArgIsPrintf(AppKit.NSGetAlertPanel, 1)
        self.assertArgIsPrintf(AppKit.NSGetInformationalAlertPanel, 1)
        self.assertArgIsPrintf(AppKit.NSGetCriticalAlertPanel, 1)

        panel = AppKit.NSGetInformationalAlertPanel(
            "title", "fmt %d", "ok", "cancel", "help", 10
        )
        self.assertIsInstance(panel, AppKit.NSPanel)

        AppKit.NSReleaseAlertPanel(panel)

    def testConstants(self):
        self.assertEqual(AppKit.NSAlertDefaultReturn, 1)
        self.assertEqual(AppKit.NSAlertAlternateReturn, 0)
        self.assertEqual(AppKit.NSAlertOtherReturn, -1)
        self.assertEqual(AppKit.NSAlertErrorReturn, -2)
        self.assertEqual(AppKit.NSOKButton, 1)
        self.assertEqual(AppKit.NSCancelButton, 0)
        self.assertEqual(AppKit.NSUtilityWindowMask, 1 << 4)
        self.assertEqual(AppKit.NSDocModalWindowMask, 1 << 6)
        self.assertEqual(AppKit.NSNonactivatingPanelMask, 1 << 7)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSHUDWindowMask, 1 << 13)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSPanel.isFloatingPanel)
        self.assertArgIsBOOL(AppKit.NSPanel.setFloatingPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSPanel.becomesKeyOnlyIfNeeded)
        self.assertArgIsBOOL(AppKit.NSPanel.setBecomesKeyOnlyIfNeeded_, 0)
        self.assertResultIsBOOL(AppKit.NSPanel.worksWhenModal)
        self.assertArgIsBOOL(AppKit.NSPanel.setWorksWhenModal_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSOpenPanel.isAccessoryViewDisclosed)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setAccessoryViewDisclosed_, 0)
