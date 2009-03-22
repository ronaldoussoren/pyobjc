
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPanel (TestCase):

    def testFunctions(self):
        self.failUnlessArgIsPrintf(NSRunAlertPanel, 1)
        self.failUnlessArgIsPrintf(NSRunInformationalAlertPanel, 1)
        self.failUnlessArgIsPrintf(NSRunCriticalAlertPanel, 1)
        self.failUnlessArgIsPrintf(NSRunAlertPanelRelativeToWindow, 1)
        self.failUnlessArgIsPrintf(NSRunInformationalAlertPanelRelativeToWindow, 1)
        self.failUnlessArgIsPrintf(NSRunCriticalAlertPanelRelativeToWindow, 1)
        self.failUnlessArgIsPrintf(NSBeginAlertSheet, 9)
        self.failUnlessArgIsSEL(NSBeginAlertSheet, 6, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgIsSEL(NSBeginAlertSheet, 7, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgHasType(NSBeginAlertSheet, 8, '^v')
        self.failUnlessArgIsPrintf(NSBeginInformationalAlertSheet, 9)
        self.failUnlessArgIsSEL(NSBeginInformationalAlertSheet, 6, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgIsSEL(NSBeginInformationalAlertSheet, 7, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgHasType(NSBeginInformationalAlertSheet, 8, '^v')
        self.failUnlessArgIsPrintf(NSBeginCriticalAlertSheet, 9)
        self.failUnlessArgIsSEL(NSBeginCriticalAlertSheet, 6, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgIsSEL(NSBeginCriticalAlertSheet, 7, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgHasType(NSBeginCriticalAlertSheet, 8, '^v')
        self.failUnlessArgIsPrintf(NSGetAlertPanel, 1)
        self.failUnlessArgIsPrintf(NSGetInformationalAlertPanel, 1)
        self.failUnlessArgIsPrintf(NSGetCriticalAlertPanel, 1)

        panel = NSGetInformationalAlertPanel("title", "fmt %d", "ok", "cancel", "help", 10)
        self.failUnlessIsInstance(panel, NSPanel)

        NSReleaseAlertPanel(panel)


    def testConstants(self):
        self.failUnlessEqual(NSAlertDefaultReturn, 1)
        self.failUnlessEqual(NSAlertAlternateReturn, 0)
        self.failUnlessEqual(NSAlertOtherReturn, -1)
        self.failUnlessEqual(NSAlertErrorReturn, -2)
        self.failUnlessEqual(NSOKButton, 1)
        self.failUnlessEqual(NSCancelButton, 0)
        self.failUnlessEqual(NSUtilityWindowMask, 1 << 4)
        self.failUnlessEqual(NSDocModalWindowMask, 1 << 6)
        self.failUnlessEqual(NSNonactivatingPanelMask, 1 << 7)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(NSHUDWindowMask, 1 << 13)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPanel.isFloatingPanel)
        self.failUnlessArgIsBOOL(NSPanel.setFloatingPanel_, 0)
        self.failUnlessResultIsBOOL(NSPanel.becomesKeyOnlyIfNeeded)
        self.failUnlessArgIsBOOL(NSPanel.setBecomesKeyOnlyIfNeeded_, 0)
        self.failUnlessResultIsBOOL(NSPanel.worksWhenModal)
        self.failUnlessArgIsBOOL(NSPanel.setWorksWhenModal_, 0)

if __name__ == "__main__":
    main()
