
from PyObjCTools.TestSupport import *
from AppKit import *

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
        self.fail("NSApplicationMain")
        self.fail("NSApplicationLoad")
        self.fail("NSShowsServicesMenuItem")
        self.fail("NSSetShowsServicesMenuItem")
        self.fail("NSUpdateDynamicServices")
        self.fail("NSPerformService")
        self.fail("NSRegisterServicesProvider")
        self.fail("NSUnregisterServicesProvider")

    def testNSApp(self):
        self.failIf(NSApp is None)
        self.failIfIsInstance(NSApp, NSObject)
        self.failUnless(hasattr(NSApp, '__call__'))
        app = NSApp()
        self.failUnless(app is None or isinstance(app, NSApplication))

    def testNSModalSession(self):
        self.fail("NSModalSession")
        self.fail("-beginModalSessionForWindow")
        self.fail("-endModalSession")

    def testMethods(self):
        self.fail("- (void)beginSheet:(NSWindow *)sheet modalForWindow:(NSWindow *)docWindow modalDelegate:(id)modalDelegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo;")


    


if __name__ == "__main__":
    main()
