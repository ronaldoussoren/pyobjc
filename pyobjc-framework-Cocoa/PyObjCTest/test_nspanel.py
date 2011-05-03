
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPanel (TestCase):

    def testFunctions(self):
        self.assertArgIsPrintf(NSRunAlertPanel, 1)
        self.assertArgIsPrintf(NSRunInformationalAlertPanel, 1)
        self.assertArgIsPrintf(NSRunCriticalAlertPanel, 1)
        self.assertArgIsPrintf(NSRunAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(NSRunInformationalAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(NSRunCriticalAlertPanelRelativeToWindow, 1)
        self.assertArgIsPrintf(NSBeginAlertSheet, 9)
        self.assertArgIsSEL(NSBeginAlertSheet, 6, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgIsSEL(NSBeginAlertSheet, 7, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgHasType(NSBeginAlertSheet, 8, b'^v')
        self.assertArgIsPrintf(NSBeginInformationalAlertSheet, 9)
        self.assertArgIsSEL(NSBeginInformationalAlertSheet, 6, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgIsSEL(NSBeginInformationalAlertSheet, 7, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgHasType(NSBeginInformationalAlertSheet, 8, b'^v')
        self.assertArgIsPrintf(NSBeginCriticalAlertSheet, 9)
        self.assertArgIsSEL(NSBeginCriticalAlertSheet, 6, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgIsSEL(NSBeginCriticalAlertSheet, 7, b'v@:@'+objc._C_NSInteger+b'^v')
        self.assertArgHasType(NSBeginCriticalAlertSheet, 8, b'^v')
        self.assertArgIsPrintf(NSGetAlertPanel, 1)
        self.assertArgIsPrintf(NSGetInformationalAlertPanel, 1)
        self.assertArgIsPrintf(NSGetCriticalAlertPanel, 1)

        panel = NSGetInformationalAlertPanel("title", "fmt %d", "ok", "cancel", "help", 10)
        self.assertIsInstance(panel, NSPanel)

        NSReleaseAlertPanel(panel)


    def testConstants(self):
        self.assertEqual(NSAlertDefaultReturn, 1)
        self.assertEqual(NSAlertAlternateReturn, 0)
        self.assertEqual(NSAlertOtherReturn, -1)
        self.assertEqual(NSAlertErrorReturn, -2)
        self.assertEqual(NSOKButton, 1)
        self.assertEqual(NSCancelButton, 0)
        self.assertEqual(NSUtilityWindowMask, 1 << 4)
        self.assertEqual(NSDocModalWindowMask, 1 << 6)
        self.assertEqual(NSNonactivatingPanelMask, 1 << 7)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(NSHUDWindowMask, 1 << 13)

    def testMethods(self):
        self.assertResultIsBOOL(NSPanel.isFloatingPanel)
        self.assertArgIsBOOL(NSPanel.setFloatingPanel_, 0)
        self.assertResultIsBOOL(NSPanel.becomesKeyOnlyIfNeeded)
        self.assertArgIsBOOL(NSPanel.setBecomesKeyOnlyIfNeeded_, 0)
        self.assertResultIsBOOL(NSPanel.worksWhenModal)
        self.assertArgIsBOOL(NSPanel.setWorksWhenModal_, 0)

if __name__ == "__main__":
    main()
