
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int

class TestNSApplicationHelper (NSObject):
    def copyWithZone_(self, zone):
        return self

    def writeSelectionToPasteboard_types_(self, pb, tp):
        return 1
    def readSelectionFromPasteboard_(self, pb):
        return 1
    def application_openFile_(self, sender, file):
        return 1
    def application_openTempFile_(self, sender, file):
        return 1
    def applicationShouldOpenUntitledFile_(self, sender):
        return 1
    def application_openFileWithoutUI_(self, sender, file):
        return 1
    def application_printFile_(self, sender, file):
        return 1
    def application_printFiles_withSettings_showPrintPanels_(
            self, a, f, s, sh):
        return 1
    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return 1
    def applicationShouldHandleReopen_hasVisibleWindows_(self, sender, flag):
        return 1


class TestNSApplication (TestCase):
    def testConstants(self):
        self.assertEqual(NSAppKitVersionNumber10_0, 577)
        self.assertEqual(NSAppKitVersionNumber10_1, 620)
        self.assertEqual(NSAppKitVersionNumber10_2, 663)
        self.assertEqual(NSAppKitVersionNumber10_2_3, 663.6)
        self.assertEqual(NSAppKitVersionNumber10_3, 743)
        self.assertEqual(NSAppKitVersionNumber10_3_2, 743.14)
        self.assertEqual(NSAppKitVersionNumber10_3_3, 743.2)
        self.assertEqual(NSAppKitVersionNumber10_3_5, 743.24)
        self.assertEqual(NSAppKitVersionNumber10_3_7, 743.33)
        self.assertEqual(NSAppKitVersionNumber10_3_9, 743.36)
        self.assertEqual(NSAppKitVersionNumber10_4, 824)
        self.assertEqual(NSAppKitVersionNumber10_4_1, 824.1)
        self.assertEqual(NSAppKitVersionNumber10_4_3, 824.23)
        self.assertEqual(NSAppKitVersionNumber10_4_4,824.33)
        self.assertEqual(NSAppKitVersionNumber10_4_7, 824.41)
        self.assertEqual(NSAppKitVersionNumber10_5, 949)
        self.assertEqual(NSAppKitVersionNumber10_5_2, 949.27)
        self.assertEqual(NSAppKitVersionNumber10_5_3, 949.33)
        self.assertEqual(NSAppKitVersionNumber10_6, 1038)


        self.assertIsInstance(NSModalPanelRunLoopMode, unicode)
        self.assertIsInstance(NSEventTrackingRunLoopMode, unicode)

        self.assertEqual(NSRunStoppedResponse, -1000)
        self.assertEqual(NSRunAbortedResponse, -1001)
        self.assertEqual(NSRunContinuesResponse, -1002)

        self.assertEqual(NSUpdateWindowsRunLoopOrdering, 500000)

        self.assertEqual(NSCriticalRequest, 0)
        self.assertEqual(NSInformationalRequest, 10)

        self.assertEqual(NSApplicationDelegateReplySuccess, 0)
        self.assertEqual(NSApplicationDelegateReplyCancel, 1)
        self.assertEqual(NSApplicationDelegateReplyFailure, 2)

        self.assertEqual(NSTerminateCancel, 0)
        self.assertEqual(NSTerminateNow, 1)
        self.assertEqual(NSTerminateLater, 2)

        self.assertEqual(NSPrintingCancelled, 0)
        self.assertEqual(NSPrintingSuccess, 1)
        self.assertEqual(NSPrintingFailure, 3)
        self.assertEqual(NSPrintingReplyLater, 2)

        self.assertIsInstance(NSApplicationDidBecomeActiveNotification, unicode)
        self.assertIsInstance(NSApplicationDidHideNotification, unicode)
        self.assertIsInstance(NSApplicationDidFinishLaunchingNotification, unicode)
        self.assertIsInstance(NSApplicationDidResignActiveNotification, unicode)
        self.assertIsInstance(NSApplicationDidUnhideNotification, unicode)
        self.assertIsInstance(NSApplicationDidUpdateNotification, unicode)
        self.assertIsInstance(NSApplicationWillBecomeActiveNotification, unicode)
        self.assertIsInstance(NSApplicationWillHideNotification, unicode)
        self.assertIsInstance(NSApplicationWillFinishLaunchingNotification, unicode)
        self.assertIsInstance(NSApplicationWillResignActiveNotification, unicode)
        self.assertIsInstance(NSApplicationWillUnhideNotification, unicode)
        self.assertIsInstance(NSApplicationWillUpdateNotification, unicode)
        self.assertIsInstance(NSApplicationWillTerminateNotification, unicode)
        self.assertIsInstance(NSApplicationDidChangeScreenParametersNotification, unicode)


    def testFunctions(self):
        # Testing the next function is not doable in this context...
        NSApplicationMain
        self.assertResultIsBOOL(NSApplicationLoad)
        self.assertIsInstance(NSApplicationLoad(), bool)

        self.assertResultIsBOOL(NSShowsServicesMenuItem)
        self.assertIsInstance(NSShowsServicesMenuItem("foobar"), bool)

        self.assertIsInstance(NSSetShowsServicesMenuItem("foobar", 1), (int, long))
        self.assertArgIsBOOL(NSSetShowsServicesMenuItem, 1)

        NSUpdateDynamicServices()

        pboard = NSPasteboard.pasteboardWithName_("pyobjctest")
        self.assertIsInstance(pboard, NSPasteboard)
        self.assertIsInstance(NSPerformService("help", pboard), bool)

        v = TestNSApplicationHelper.alloc().init()
        NSRegisterServicesProvider("foobar", v)
        NSUnregisterServicesProvider("foobar")

    def testNSApp(self):
        self.assertIsNot(NSApp, None)
        self.assertEqual(type(NSApp).__name__, "_NSApp")
        self.assertHasAttr(NSApp, '__call__')
        app = NSApp()
        if app is not None:
            self.assertIsInstance(app, NSApplication)

    def testNSModalSession(self):
        self.assertIsOpaquePointer(NSModalSession)

        app = NSApplication.sharedApplication()
        window = NSWindow.alloc().init()
        session = app.beginModalSessionForWindow_(window)
        self.assertIsInstance(session, NSModalSession)
        app.endModalSession_(session)

    def testMethods(self):
        self.assertResultIsBOOL(NSApplication.isActive)
        self.assertResultIsBOOL(NSApplication.isHidden)
        self.assertResultIsBOOL(NSApplication.isRunning)
        self.assertArgIsBOOL(NSApplication.activateIgnoringOtherApps_, 0)

        self.assertArgIsSEL(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 4, b'^v')


        self.assertArgIsBOOL(NSApplication.postEvent_atStart_, 1)
        self.assertArgIsBOOL(NSApplication.makeWindowsPerform_inOrder_, 1)
        self.assertArgIsBOOL(NSApplication.setWindowsNeedUpdate_, 0)
        self.assertResultIsBOOL(NSApplication.sendAction_to_from_)
        self.assertResultIsBOOL(NSApplication.tryToPerform_with_)
        self.assertArgIsBOOL(NSApplication.replyToApplicationShouldTerminate_, 0)
        self.assertArgIsBOOL(NSApplication.addWindowsItem_title_filename_, 2)
        self.assertArgIsBOOL(NSApplication.changeWindowsItem_title_filename_, 2)

    def testDelegateMethods(self):
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openFile_)
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openTempFile_)
        self.assertResultIsBOOL(TestNSApplicationHelper.applicationShouldOpenUntitledFile_)
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openFileWithoutUI_)
        self.assertResultIsBOOL(TestNSApplicationHelper.application_printFile_)
        self.assertArgIsBOOL(TestNSApplicationHelper.application_printFiles_withSettings_showPrintPanels_, 3)
        self.assertResultIsBOOL(TestNSApplicationHelper.applicationShouldTerminateAfterLastWindowClosed_)
        self.assertResultIsBOOL(TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_)
        self.assertArgIsBOOL(TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_, 1)

        self.assertResultIsBOOL(TestNSApplicationHelper.writeSelectionToPasteboard_types_)
        self.assertResultIsBOOL(TestNSApplicationHelper.readSelectionFromPasteboard_)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSAppKitVersionNumber10_4_1, 824.1)
        self.assertEqual(NSAppKitVersionNumber10_4_3, 824.23)
        self.assertEqual(NSAppKitVersionNumber10_4_4, 824.33)
        self.assertEqual(NSAppKitVersionNumber10_4_7, 824.41)
        self.assertEqual(NSAppKitVersionNumber10_5, 949)
        self.assertEqual(NSAppKitVersionNumber10_5_2, 949.27)
        self.assertEqual(NSAppKitVersionNumber10_5_3, 949.33)
        self.assertEqual(NSAppKitVersionNumber10_5_3, 949.33)

        self.assertEqual(NSApplicationPresentationDefault, 0)
        self.assertEqual(NSApplicationPresentationAutoHideDock, (1 <<  0))
        self.assertEqual(NSApplicationPresentationHideDock, (1 <<  1))
        self.assertEqual(NSApplicationPresentationAutoHideMenuBar, (1 <<  2))
        self.assertEqual(NSApplicationPresentationHideMenuBar, (1 <<  3))
        self.assertEqual(NSApplicationPresentationDisableAppleMenu, (1 <<  4))
        self.assertEqual(NSApplicationPresentationDisableProcessSwitching, (1 <<  5))
        self.assertEqual(NSApplicationPresentationDisableForceQuit, (1 <<  6))
        self.assertEqual(NSApplicationPresentationDisableSessionTermination, (1 <<  7))
        self.assertEqual(NSApplicationPresentationDisableHideApplication, (1 <<  8))
        self.assertEqual(NSApplicationPresentationDisableMenuBarTransparency, (1 <<  9))

        self.assertEqual(NSUserInterfaceLayoutDirectionLeftToRight, 0)
        self.assertEqual(NSUserInterfaceLayoutDirectionRightToLeft, 1)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSApplicationPresentationFullScreen, 1<<10)
        self.assertEqual(NSApplicationPresentationAutoHideToolbar, 1<<11)
        self.assertEqual(NSRemoteNotificationTypeNone, 0)
        self.assertEqual(NSRemoteNotificationTypeBadge, 1)

        self.assertEqual(NSAppKitVersionNumber10_7, 1138)
        self.assertEqual(NSAppKitVersionNumber10_7_2, 1138.23)

        self.assertIsInstance(NSApplicationLaunchRemoteNotificationKey, unicode)
        self.assertIsInstance(NSApplicationLaunchIsDefaultLaunchKey, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(NSApplicationLaunchUserNotificationKey, unicode)
        self.assertIsInstance(NSTextAlternativesAttributeName, unicode)
        self.assertIsInstance(NSUsesScreenFontsDocumentAttribute, unicode)

        self.assertEqual(NSRemoteNotificationTypeSound, 2)
        self.assertEqual(NSRemoteNotificationTypeAlert, 4)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSApplication.setActivationPolicy_)
        self.assertResultIsBOOL(NSApplication.isFullKeyboardAccessEnabled)



if __name__ == "__main__":
    main()
