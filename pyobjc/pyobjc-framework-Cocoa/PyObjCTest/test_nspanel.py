
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPanel (TestCase):

    def testMethods(self):
        self.fail("APPKIT_EXTERN NSInteger NSRunAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN NSInteger NSRunInformationalAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN NSInteger NSRunCriticalAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN NSInteger NSRunAlertPanelRelativeToWindow(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);")
        self.fail("APPKIT_EXTERN NSInteger NSRunInformationalAlertPanelRelativeToWindow(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);")
        self.fail("APPKIT_EXTERN NSInteger NSRunCriticalAlertPanelRelativeToWindow(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, ...);")
        self.fail("APPKIT_EXTERN void NSBeginAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msgFormat, ...);")
        self.fail("APPKIT_EXTERN void NSBeginInformationalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msgFormat, ...);")
        self.fail("APPKIT_EXTERN void NSBeginCriticalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msgFormat, ...);")
        self.fail("APPKIT_EXTERN id NSGetAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN id NSGetInformationalAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN id NSGetCriticalAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);")
        self.fail("APPKIT_EXTERN void NSReleaseAlertPanel(id panel);")

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

if __name__ == "__main__":
    main()
