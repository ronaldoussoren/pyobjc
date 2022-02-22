import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSApplicationHelper(AppKit.NSObject):
    def applicationShouldAutomaticallyLocalizeKeyEquivalents_(self, a):
        pass

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

    def application_printFiles_withSettings_showPrintPanels_(self, a, f, s, sh):
        return 1

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return 1

    def applicationShouldHandleReopen_hasVisibleWindows_(self, sender, flag):
        return 1

    def application_willContinueUserActivityWithType_(self, sender, tp):
        return 1

    def application_continueUserActivity_restorationHandler_(self, sender, tp, h):
        return 1

    def application_delegateHandlesKey_(self, a, k):
        return 1

    def applicationSupportsSecureRestorableState_(self, a):
        return 1


class TestNSApplication(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSAboutPanelOptionKey, str)
        self.assertIsTypedEnum(AppKit.NSAppKitVersion, float)
        self.assertIsTypedEnum(AppKit.NSModalResponse, int)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSApplicationDelegateReply)
        self.assertIsEnumType(AppKit.NSApplicationOcclusionState)
        self.assertIsEnumType(AppKit.NSApplicationPresentationOptions)
        self.assertIsEnumType(AppKit.NSApplicationPrintReply)
        self.assertIsEnumType(AppKit.NSApplicationTerminateReply)
        self.assertIsEnumType(AppKit.NSRemoteNotificationType)
        self.assertIsEnumType(AppKit.NSRequestUserAttentionType)
        self.assertIsEnumType(AppKit.NSWindowListOptions)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSAppKitVersionNumber, float)

        self.assertEqual(AppKit.NSAppKitVersionNumber10_0, 577)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_1, 620)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_2, 663)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_2_3, 663.6)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3, 743)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3_2, 743.14)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3_3, 743.2)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3_5, 743.24)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3_7, 743.33)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_3_9, 743.36)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4, 824)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_1, 824.1)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_3, 824.23)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_4, 824.33)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_7, 824.41)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5, 949)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5_2, 949.27)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5_3, 949.33)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_6, 1038)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_7, 1138)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_7_2, 1138.23)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_7_3, 1138.32)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_7_4, 1138.47)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_8, 1187)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_9, 1265)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10, 1343)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10_2, 1344)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10_3, 1347)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10_4, 1348)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10_5, 1348)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_10_Max, 1349)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_11, 1404)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_11_1, 1404.13)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_11_2, 1404.34)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_11_3, 1404.34)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_12, 1504)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_12_1, 1504.60)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_12_2, 1504.76)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_13, 1561)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_13_1, 1561.1)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_13_2, 1561.2)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_13_4, 1561.4)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14, 1671)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14_1, 1671.1)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14_2, 1671.2)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14_3, 1671.3)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14_4, 1671.4)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_14_5, 1671.5)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15, 1894)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_1, 1894.1)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_2, 1894.2)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_3, 1894.3)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_4, 1894.4)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_5, 1894.5)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_15_6, 1894.6)
        self.assertEqual(AppKit.NSAppKitVersionNumber11_0, 2022)
        self.assertEqual(AppKit.NSAppKitVersionNumber11_1, 2022.2)
        self.assertEqual(AppKit.NSAppKitVersionNumber11_2, 2022.3)
        self.assertEqual(AppKit.NSAppKitVersionNumber11_3, 2022.4)
        self.assertEqual(AppKit.NSAppKitVersionNumber11_4, 2022.5)

        self.assertIsInstance(AppKit.NSModalPanelRunLoopMode, str)
        self.assertIsInstance(AppKit.NSEventTrackingRunLoopMode, str)

        self.assertEqual(AppKit.NSRunStoppedResponse, -1000)
        self.assertEqual(AppKit.NSRunAbortedResponse, -1001)
        self.assertEqual(AppKit.NSRunContinuesResponse, -1002)

        self.assertEqual(AppKit.NSUpdateWindowsRunLoopOrdering, 500_000)

        self.assertEqual(AppKit.NSCriticalRequest, 0)
        self.assertEqual(AppKit.NSInformationalRequest, 10)

        self.assertEqual(AppKit.NSApplicationDelegateReplySuccess, 0)
        self.assertEqual(AppKit.NSApplicationDelegateReplyCancel, 1)
        self.assertEqual(AppKit.NSApplicationDelegateReplyFailure, 2)

        self.assertEqual(AppKit.NSTerminateCancel, 0)
        self.assertEqual(AppKit.NSTerminateNow, 1)
        self.assertEqual(AppKit.NSTerminateLater, 2)

        self.assertEqual(AppKit.NSPrintingCancelled, 0)
        self.assertEqual(AppKit.NSPrintingSuccess, 1)
        self.assertEqual(AppKit.NSPrintingFailure, 3)
        self.assertEqual(AppKit.NSPrintingReplyLater, 2)

        self.assertIsInstance(AppKit.NSApplicationDidBecomeActiveNotification, str)
        self.assertIsInstance(AppKit.NSApplicationDidHideNotification, str)
        self.assertIsInstance(AppKit.NSApplicationDidFinishLaunchingNotification, str)
        self.assertIsInstance(AppKit.NSApplicationDidResignActiveNotification, str)
        self.assertIsInstance(AppKit.NSApplicationDidUnhideNotification, str)
        self.assertIsInstance(AppKit.NSApplicationDidUpdateNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillBecomeActiveNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillHideNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillFinishLaunchingNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillResignActiveNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillUnhideNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillUpdateNotification, str)
        self.assertIsInstance(AppKit.NSApplicationWillTerminateNotification, str)
        self.assertIsInstance(
            AppKit.NSApplicationDidChangeScreenParametersNotification, str
        )

        self.assertEqual(AppKit.NSWindowListOrderedFrontToBack, 1 << 0)

        self.assertEqual(AppKit.NSModalResponseStop, -1000)
        self.assertEqual(AppKit.NSModalResponseAbort, -1001)
        self.assertEqual(AppKit.NSModalResponseContinue, -1002)

    def testFunctions(self):
        # Testing the next function is not doable in this context...
        AppKit.NSApplicationMain
        self.assertResultIsBOOL(AppKit.NSApplicationLoad)
        self.assertIsInstance(AppKit.NSApplicationLoad(), bool)

        self.assertResultIsBOOL(AppKit.NSShowsServicesMenuItem)
        self.assertIsInstance(AppKit.NSShowsServicesMenuItem("foobar"), bool)

        self.assertIsInstance(AppKit.NSSetShowsServicesMenuItem("foobar", 1), int)
        self.assertArgIsBOOL(AppKit.NSSetShowsServicesMenuItem, 1)

        AppKit.NSUpdateDynamicServices()

        pboard = AppKit.NSPasteboard.pasteboardWithName_("pyobjctest")
        self.assertIsInstance(pboard, AppKit.NSPasteboard)
        self.assertIsInstance(AppKit.NSPerformService("help", pboard), bool)

        v = TestNSApplicationHelper.alloc().init()
        AppKit.NSRegisterServicesProvider(v, "foobar")
        AppKit.NSUnregisterServicesProvider("foobar")

    def testNSApp(self):
        self.assertIsNot(AppKit.NSApp, None)
        self.assertEqual(type(AppKit.NSApp).__name__, "_NSApp")
        self.assertHasAttr(AppKit.NSApp, "__call__")
        app = AppKit.NSApp()
        if app is not None:
            self.assertIsInstance(app, AppKit.NSApplication)

            self.assertIsInstance(AppKit.NSApp.description(), str)

            self.assertRaises(AttributeError, setattr, AppKit.NSApp, "foo", 42)

    def testNSModalSession(self):
        self.assertIsOpaquePointer(AppKit.NSModalSession)

        app = AppKit.NSApplication.sharedApplication()
        window = AppKit.NSWindow.alloc().init()
        session = app.beginModalSessionForWindow_(window)
        self.assertIsInstance(session, AppKit.NSModalSession)
        app.endModalSession_(session)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSApplication.isActive)
        self.assertResultIsBOOL(AppKit.NSApplication.isHidden)
        self.assertResultIsBOOL(AppKit.NSApplication.isRunning)
        self.assertArgIsBOOL(AppKit.NSApplication.activateIgnoringOtherApps_, 0)

        self.assertArgIsSEL(
            AppKit.NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )

        self.assertArgIsBOOL(AppKit.NSApplication.postEvent_atStart_, 1)
        self.assertArgIsBOOL(AppKit.NSApplication.makeWindowsPerform_inOrder_, 1)
        self.assertArgIsBOOL(AppKit.NSApplication.setWindowsNeedUpdate_, 0)
        self.assertResultIsBOOL(AppKit.NSApplication.sendAction_to_from_)
        self.assertResultIsBOOL(AppKit.NSApplication.tryToPerform_with_)
        self.assertArgIsBOOL(AppKit.NSApplication.replyToApplicationShouldTerminate_, 0)
        self.assertArgIsBOOL(AppKit.NSApplication.addWindowsItem_title_filename_, 2)
        self.assertArgIsBOOL(AppKit.NSApplication.changeWindowsItem_title_filename_, 2)

        self.assertArgIsBOOL(
            AppKit.NSApplication.nextEventMatchingMask_untilDate_inMode_dequeue_, 3
        )

    def testDelegateMethods(self):
        self.assertResultIsBOOL(
            TestNSApplicationHelper.applicationShouldAutomaticallyLocalizeKeyEquivalents_
        )
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openFile_)
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openTempFile_)
        self.assertResultIsBOOL(
            TestNSApplicationHelper.applicationShouldOpenUntitledFile_
        )
        self.assertResultIsBOOL(TestNSApplicationHelper.application_openFileWithoutUI_)
        self.assertResultIsBOOL(TestNSApplicationHelper.application_printFile_)
        self.assertArgIsBOOL(
            TestNSApplicationHelper.application_printFiles_withSettings_showPrintPanels_,
            3,
        )
        self.assertResultIsBOOL(
            TestNSApplicationHelper.applicationShouldTerminateAfterLastWindowClosed_
        )
        self.assertResultIsBOOL(
            TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_
        )
        self.assertArgIsBOOL(
            TestNSApplicationHelper.applicationShouldHandleReopen_hasVisibleWindows_, 1
        )

        self.assertResultIsBOOL(
            TestNSApplicationHelper.writeSelectionToPasteboard_types_
        )
        self.assertResultIsBOOL(TestNSApplicationHelper.readSelectionFromPasteboard_)

        self.assertResultIsBOOL(
            TestNSApplicationHelper.application_willContinueUserActivityWithType_
        )
        self.assertResultIsBOOL(
            TestNSApplicationHelper.application_continueUserActivity_restorationHandler_
        )
        self.assertArgIsBlock(
            TestNSApplicationHelper.application_continueUserActivity_restorationHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(TestNSApplicationHelper.application_delegateHandlesKey_)
        self.assertResultIsBOOL(
            TestNSApplicationHelper.applicationSupportsSecureRestorableState_
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_1, 824.1)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_3, 824.23)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_4, 824.33)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_4_7, 824.41)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5, 949)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5_2, 949.27)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5_3, 949.33)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_5_3, 949.33)

        self.assertEqual(AppKit.NSApplicationPresentationDefault, 0)
        self.assertEqual(AppKit.NSApplicationPresentationAutoHideDock, (1 << 0))
        self.assertEqual(AppKit.NSApplicationPresentationHideDock, (1 << 1))
        self.assertEqual(AppKit.NSApplicationPresentationAutoHideMenuBar, (1 << 2))
        self.assertEqual(AppKit.NSApplicationPresentationHideMenuBar, (1 << 3))
        self.assertEqual(AppKit.NSApplicationPresentationDisableAppleMenu, (1 << 4))
        self.assertEqual(
            AppKit.NSApplicationPresentationDisableProcessSwitching, (1 << 5)
        )
        self.assertEqual(AppKit.NSApplicationPresentationDisableForceQuit, (1 << 6))
        self.assertEqual(
            AppKit.NSApplicationPresentationDisableSessionTermination, (1 << 7)
        )
        self.assertEqual(
            AppKit.NSApplicationPresentationDisableHideApplication, (1 << 8)
        )
        self.assertEqual(
            AppKit.NSApplicationPresentationDisableMenuBarTransparency, (1 << 9)
        )

        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionRightToLeft, 1)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSApplicationPresentationFullScreen, 1 << 10)
        self.assertEqual(AppKit.NSApplicationPresentationAutoHideToolbar, 1 << 11)
        self.assertEqual(AppKit.NSRemoteNotificationTypeNone, 0)
        self.assertEqual(AppKit.NSRemoteNotificationTypeBadge, 1)

        self.assertEqual(AppKit.NSAppKitVersionNumber10_7, 1138)
        self.assertEqual(AppKit.NSAppKitVersionNumber10_7_2, 1138.23)

        self.assertIsInstance(AppKit.NSApplicationLaunchRemoteNotificationKey, str)
        self.assertIsInstance(AppKit.NSApplicationLaunchIsDefaultLaunchKey, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSApplicationLaunchUserNotificationKey, str)
        self.assertIsInstance(AppKit.NSTextAlternativesAttributeName, str)
        self.assertIsInstance(AppKit.NSUsesScreenFontsDocumentAttribute, str)

        self.assertEqual(AppKit.NSRemoteNotificationTypeSound, 2)
        self.assertEqual(AppKit.NSRemoteNotificationTypeAlert, 4)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(AppKit.NSApplicationOcclusionStateVisible, 1 << 1)

        self.assertIsInstance(
            AppKit.NSApplicationDidChangeOcclusionStateNotification, str
        )

    @min_os_level("10.11.2")
    def testConstants10_11_2(self):
        self.assertEqual(
            AppKit.NSApplicationPresentationDisableCursorLocationAssistance, 1 << 12
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSAboutPanelOptionCredits, str)
        self.assertIsInstance(AppKit.NSAboutPanelOptionApplicationName, str)
        self.assertIsInstance(AppKit.NSAboutPanelOptionApplicationIcon, str)
        self.assertIsInstance(AppKit.NSAboutPanelOptionVersion, str)
        self.assertIsInstance(AppKit.NSAboutPanelOptionApplicationVersion, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(AppKit.NSAppearanceDocumentAttribute, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(
            AppKit.NSApplicationProtectedDataWillBecomeUnavailableNotification, str
        )
        self.assertIsInstance(
            AppKit.NSApplicationProtectedDataDidBecomeAvailableNotification, str
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSApplication.setActivationPolicy_)
        self.assertResultIsBOOL(AppKit.NSApplication.isFullKeyboardAccessEnabled)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            AppKit.NSApplication.enumerateWindowsWithOptions_usingBlock_, 1, b"v@o^Z"
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(AppKit.NSApplication.isRegisteredForRemoteNotifications)

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(AppKit.NSApplication.isProtectedDataAvailable)
        self.assertResultIsBOOL(AppKit.NSApplication.isProtectedDataAvailable)

    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("NSApplicationDelegate")
