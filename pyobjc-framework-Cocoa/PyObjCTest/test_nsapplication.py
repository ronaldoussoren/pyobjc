
from PyObjCTools.TestSupport import *
from AppKit import *

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
        self.failUnlessEqual(NSAppKitVersionNumber10_0, 577)
        self.failUnlessEqual(NSAppKitVersionNumber10_1, 620)
        self.failUnlessEqual(NSAppKitVersionNumber10_2, 663)
        self.failUnlessEqual(NSAppKitVersionNumber10_2_3, 663.6)
        self.failUnlessEqual(NSAppKitVersionNumber10_3, 743)
        self.failUnlessEqual(NSAppKitVersionNumber10_3_2, 743.14)
        self.failUnlessEqual(NSAppKitVersionNumber10_3_3, 743.2)
        self.failUnlessEqual(NSAppKitVersionNumber10_3_5, 743.24)
        self.failUnlessEqual(NSAppKitVersionNumber10_3_7, 743.33)
        self.failUnlessEqual(NSAppKitVersionNumber10_3_9, 743.36)
        self.failUnlessEqual(NSAppKitVersionNumber10_4, 824)

        self.failUnlessIsInstance(NSModalPanelRunLoopMode, unicode)
        self.failUnlessIsInstance(NSEventTrackingRunLoopMode, unicode)

        self.failUnlessEqual(NSRunStoppedResponse, -1000)
        self.failUnlessEqual(NSRunAbortedResponse, -1001)
        self.failUnlessEqual(NSRunContinuesResponse, -1002)

        self.failUnlessEqual(NSUpdateWindowsRunLoopOrdering, 500000)

        self.failUnlessEqual(NSCriticalRequest, 0)
        self.failUnlessEqual(NSInformationalRequest, 10)

        self.failUnlessEqual(NSApplicationDelegateReplySuccess, 0)
        self.failUnlessEqual(NSApplicationDelegateReplyCancel, 1)
        self.failUnlessEqual(NSApplicationDelegateReplyFailure, 2)

        self.failUnlessEqual(NSTerminateCancel, 0)
        self.failUnlessEqual(NSTerminateNow, 1)
        self.failUnlessEqual(NSTerminateLater, 2)

        self.failUnlessEqual(NSPrintingCancelled, 0)
        self.failUnlessEqual(NSPrintingSuccess, 1)
        self.failUnlessEqual(NSPrintingFailure, 3)
        self.failUnlessEqual(NSPrintingReplyLater, 2)

        self.failUnlessIsInstance(NSApplicationDidBecomeActiveNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidHideNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidFinishLaunchingNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidResignActiveNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidUnhideNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidUpdateNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillBecomeActiveNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillHideNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillFinishLaunchingNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillResignActiveNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillUnhideNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillUpdateNotification, unicode)
        self.failUnlessIsInstance(NSApplicationWillTerminateNotification, unicode)
        self.failUnlessIsInstance(NSApplicationDidChangeScreenParametersNotification, unicode)


    def testFunctions(self):
        # Testing the next function is not doable in this context...
        NSApplicationMain
        self.failUnlessResultIsBOOL(NSApplicationLoad)
        self.failUnlessIsInstance(NSApplicationLoad(), bool)

        self.failUnlessResultIsBOOL(NSShowsServicesMenuItem)
        self.failUnlessIsInstance(NSShowsServicesMenuItem("foobar"), bool)

        self.failUnlessIsInstance(NSSetShowsServicesMenuItem("foobar", 1), (int, long))
        self.failUnlessArgIsBOOL(NSSetShowsServicesMenuItem, 1)

        NSUpdateDynamicServices()

        pboard = NSPasteboard.pasteboardWithName_("pyobjctest")
        self.failUnlessIsInstance(pboard, NSPasteboard)
        self.failUnlessIsInstance(NSPerformService("help", pboard), bool)

        objc.setVerbose(1)
        v = TestNSApplicationHelper.alloc().init()
        NSRegisterServicesProvider("foobar", v)
        NSUnregisterServicesProvider("foobar")

    def testNSApp(self):
        self.failIf(NSApp is None)
        self.failUnlessEqual(type(NSApp).__name__, "_NSApp")
        self.failUnless(hasattr(NSApp, '__call__'))
        app = NSApp()
        self.failUnless(app is None or isinstance(app, NSApplication))

    def testNSModalSession(self):
        self.failUnlessIsOpaquePointer(NSModalSession)

        app = NSApplication.sharedApplication()
        window = NSWindow.alloc().init()
        session = app.beginModalSessionForWindow_(window)
        self.failUnlessIsInstance(session, NSModalSession)
        app.endModalSession_(session)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSApplication.isActive)
        self.failUnlessResultIsBOOL(NSApplication.isHidden)
        self.failUnlessResultIsBOOL(NSApplication.isRunning)
        self.failUnlessArgIsBOOL(NSApplication.activateIgnoringOtherApps_, 0)

        self.failUnlessArgIsSEL(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgHasType(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 4, '^v')


        self.failUnlessArgIsBOOL(NSApplication.postEvent_atStart_, 1)
        self.failUnlessArgIsBOOL(NSApplication.makeWindowsPerform_inOrder_, 1)
        self.failUnlessArgIsBOOL(NSApplication.setWindowsNeedUpdate_, 0)
        self.failUnlessResultIsBOOL(NSApplication.sendAction_to_from_)
        self.failUnlessResultIsBOOL(NSApplication.tryToPerform_with_)
        self.failUnlessArgIsBOOL(NSApplication.replyToApplicationShouldTerminate_, 0)
        self.failUnlessArgIsBOOL(NSApplication.addWindowsItem_title_filename_, 2)
        self.failUnlessArgIsBOOL(NSApplication.changeWindowsItem_title_filename_, 2)
   
    def testDelegateMethods(self):
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.application_openFile_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.application_openTempFile_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.applicationShouldOpenUntitledFile_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.application_openFileWithoutUI_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.application_printFile_)
        self.failUnlessArgIsBOOL(TestNSApplicationHelper.application_printFiles_withSettings_showPrintPanels_, 3)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.applicationShouldTerminateAfterLastWindowClosed_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_)
        self.failUnlessArgIsBOOL(TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_, 1)

        self.failUnlessResultIsBOOL(TestNSApplicationHelper.writeSelectionToPasteboard_types_)
        self.failUnlessResultIsBOOL(TestNSApplicationHelper.readSelectionFromPasteboard_)


if __name__ == "__main__":
    main()
