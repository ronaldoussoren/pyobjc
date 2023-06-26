import sys

import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level, skipUnless
import objc

try:
    import Quartz
except ImportError:
    Quartz = None


class TestNSWindowHelper(AppKit.NSObject):
    def window_willUseFullScreenContentSize_(self, a, b):
        pass

    def window_willUseFullScreenPresentationOptions_(self, a, b):
        pass

    def window_startCustomAnimationToEnterFullScreenWithDuration_(self, a, b):
        pass

    def window_startCustomAnimationToExitFullScreenWithDuration_(self, a, b):
        pass

    def window_willResizeForVersionBrowserWithMaxPreferredSize_maxAllowedSize_(
        self, a, b, c
    ):
        pass

    def windowShouldClose_(self, w):
        return 1

    def windowWillResize_toSize_(self, w, a):
        return 1

    def windowWillUseStandardFrame_defaultFrame_(self, w, a):
        return 1

    def windowShouldZoom_toFrame_(self, w, a):
        return 1

    def window_willPositionSheet_usingRect_(self, w, a, b):
        return 1

    def window_shouldPopUpDocumentPathMenu_(self, w, a):
        return 1

    def window_shouldDragDocumentWithEvent_from_withPasteboard_(self, w, a, b, c):
        return 1

    def window_startCustomAnimationToEnterFullScreenOnScreen_withDuration_(
        self, w, a, d
    ):
        pass


class TestNSWindow(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSWindowLevel, int)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSSelectionDirection)
        self.assertIsEnumType(AppKit.NSTitlebarSeparatorStyle)
        self.assertIsEnumType(AppKit.NSWindowAnimationBehavior)
        self.assertIsEnumType(AppKit.NSWindowBackingLocation)
        self.assertIsEnumType(AppKit.NSWindowButton)
        self.assertIsEnumType(AppKit.NSWindowCollectionBehavior)
        self.assertIsEnumType(AppKit.NSWindowNumberListOptions)
        self.assertIsEnumType(AppKit.NSWindowOcclusionState)
        self.assertIsEnumType(AppKit.NSWindowSharingType)
        self.assertIsEnumType(AppKit.NSWindowStyleMask)
        self.assertIsEnumType(AppKit.NSWindowTabbingMode)
        self.assertIsEnumType(AppKit.NSWindowTitleVisibility)
        self.assertIsEnumType(AppKit.NSWindowToolbarStyle)
        self.assertIsEnumType(AppKit.NSWindowUserTabbingPreference)

    def testConstants(self):
        self.assertEqual(AppKit.NSEventDurationForever, sys.float_info.max)
        self.assertEqual(AppKit.NSAppKitVersionNumberWithCustomSheetPosition, 686.0)
        self.assertEqual(
            AppKit.NSAppKitVersionNumberWithDeferredWindowDisplaySupport, 1019.0
        )

        self.assertEqual(AppKit.NSBorderlessWindowMask, 0)
        self.assertEqual(AppKit.NSTitledWindowMask, 1 << 0)
        self.assertEqual(AppKit.NSClosableWindowMask, 1 << 1)
        self.assertEqual(AppKit.NSMiniaturizableWindowMask, 1 << 2)
        self.assertEqual(AppKit.NSResizableWindowMask, 1 << 3)

        self.assertEqual(AppKit.NSWindowStyleMaskBorderless, 0)
        self.assertEqual(AppKit.NSWindowStyleMaskTitled, 1 << 0)
        self.assertEqual(AppKit.NSWindowStyleMaskClosable, 1 << 1)
        self.assertEqual(AppKit.NSWindowStyleMaskMiniaturizable, 1 << 2)
        self.assertEqual(AppKit.NSWindowStyleMaskResizable, 1 << 3)
        self.assertEqual(AppKit.NSWindowStyleMaskTexturedBackground, 1 << 8)
        self.assertEqual(AppKit.NSWindowStyleMaskUnifiedTitleAndToolbar, 1 << 12)
        self.assertEqual(AppKit.NSWindowStyleMaskFullScreen, 1 << 14)
        self.assertEqual(AppKit.NSWindowStyleMaskFullSizeContentView, 1 << 15)
        self.assertEqual(AppKit.NSWindowStyleMaskUtilityWindow, 1 << 4)
        self.assertEqual(AppKit.NSWindowStyleMaskDocModalWindow, 1 << 6)
        self.assertEqual(AppKit.NSWindowStyleMaskNonactivatingPanel, 1 << 7)
        self.assertEqual(AppKit.NSWindowStyleMaskHUDWindow, 1 << 13)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorFullScreenNone, 1 << 9)

        self.assertEqual(AppKit.NSWindowUserTabbingPreferenceManual, 0)
        self.assertEqual(AppKit.NSWindowUserTabbingPreferenceAlways, 1)
        self.assertEqual(AppKit.NSWindowUserTabbingPreferenceInFullScreen, 2)

        self.assertEqual(AppKit.NSWindowTabbingModeAutomatic, 0)
        self.assertEqual(AppKit.NSWindowTabbingModePreferred, 1)
        self.assertEqual(AppKit.NSWindowTabbingModeDisallowed, 2)

        self.assertEqual(AppKit.NSTexturedBackgroundWindowMask, 1 << 8)

        self.assertEqual(AppKit.NSUnscaledWindowMask, 1 << 11)

        self.assertEqual(AppKit.NSUnifiedTitleAndToolbarWindowMask, 1 << 12)

        self.assertEqual(AppKit.NSDisplayWindowRunLoopOrdering, 600_000)
        self.assertEqual(AppKit.NSResetCursorRectsRunLoopOrdering, 700_000)

        self.assertEqual(AppKit.NSWindowSharingNone, 0)
        self.assertEqual(AppKit.NSWindowSharingReadOnly, 1)
        self.assertEqual(AppKit.NSWindowSharingReadWrite, 2)

        self.assertEqual(AppKit.NSWindowBackingLocationDefault, 0)
        self.assertEqual(AppKit.NSWindowBackingLocationVideoMemory, 1)
        self.assertEqual(AppKit.NSWindowBackingLocationMainMemory, 2)

        self.assertEqual(AppKit.NSWindowCollectionBehaviorDefault, 0)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorCanJoinAllSpaces, 1 << 0)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorMoveToActiveSpace, 1 << 1)

        self.assertEqual(AppKit.NSDirectSelection, 0)
        self.assertEqual(AppKit.NSSelectingNext, 1)
        self.assertEqual(AppKit.NSSelectingPrevious, 2)

        self.assertEqual(AppKit.NSWindowCloseButton, 0)
        self.assertEqual(AppKit.NSWindowMiniaturizeButton, 1)
        self.assertEqual(AppKit.NSWindowZoomButton, 2)
        self.assertEqual(AppKit.NSWindowToolbarButton, 3)
        self.assertEqual(AppKit.NSWindowDocumentIconButton, 4)

        self.assertIsInstance(AppKit.NSWindowDidBecomeKeyNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidBecomeMainNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidChangeScreenNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidDeminiaturizeNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidExposeNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidMiniaturizeNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidMoveNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidResignKeyNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidResignMainNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidResizeNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidUpdateNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillCloseNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillMiniaturizeNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillMoveNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillBeginSheetNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidEndSheetNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidChangeScreenProfileNotification, str)

        self.assertEqual(AppKit.NSWindowToolbarStyleAutomatic, 0)
        self.assertEqual(AppKit.NSWindowToolbarStyleExpanded, 1)
        self.assertEqual(AppKit.NSWindowToolbarStylePreference, 2)
        self.assertEqual(AppKit.NSWindowToolbarStyleUnified, 3)
        self.assertEqual(AppKit.NSWindowToolbarStyleUnifiedCompact, 4)

        self.assertEqual(AppKit.NSTitlebarSeparatorStyleAutomatic, 0)
        self.assertEqual(AppKit.NSTitlebarSeparatorStyleNone, 1)
        self.assertEqual(AppKit.NSTitlebarSeparatorStyleLine, 2)
        self.assertEqual(AppKit.NSTitlebarSeparatorStyleShadow, 3)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(
            AppKit.NSAppKitVersionNumberWithDeferredWindowDisplaySupport, 1019.0
        )

        self.assertEqual(AppKit.NSWindowCollectionBehaviorManaged, 1 << 2)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorTransient, 1 << 3)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorStationary, 1 << 4)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorParticipatesInCycle, 1 << 5)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorIgnoresCycle, 1 << 6)
        self.assertEqual(AppKit.NSWindowNumberListAllApplications, 1 << 0)
        self.assertEqual(AppKit.NSWindowNumberListAllSpaces, 1 << 4)

        self.assertIsInstance(AppKit.NSWindowWillStartLiveResizeNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidEndLiveResizeNotification, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSFullScreenWindowMask, 1 << 14)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorFullScreenPrimary, 1 << 7)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorFullScreenAuxiliary, 1 << 8)
        self.assertEqual(AppKit.NSWindowAnimationBehaviorDefault, 0)
        self.assertEqual(AppKit.NSWindowAnimationBehaviorNone, 2)
        self.assertEqual(AppKit.NSWindowAnimationBehaviorDocumentWindow, 3)
        self.assertEqual(AppKit.NSWindowAnimationBehaviorUtilityWindow, 4)
        self.assertEqual(AppKit.NSWindowAnimationBehaviorAlertPanel, 5)
        self.assertEqual(AppKit.NSWindowDocumentVersionsButton, 6)
        self.assertEqual(AppKit.NSWindowFullScreenButton, 7)

        self.assertIsInstance(
            AppKit.NSWindowDidChangeBackingPropertiesNotification, str
        )
        self.assertIsInstance(AppKit.NSBackingPropertyOldScaleFactorKey, str)
        self.assertIsInstance(AppKit.NSBackingPropertyOldColorSpaceKey, str)
        self.assertIsInstance(AppKit.NSWindowWillEnterFullScreenNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidEnterFullScreenNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillExitFullScreenNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidExitFullScreenNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillEnterVersionBrowserNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidEnterVersionBrowserNotification, str)
        self.assertIsInstance(AppKit.NSWindowWillExitVersionBrowserNotification, str)
        self.assertIsInstance(AppKit.NSWindowDidExitVersionBrowserNotification, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(AppKit.NSModalResponseOK, 1)
        self.assertEqual(AppKit.NSModalResponseCancel, 0)

        self.assertEqual(AppKit.NSWindowOcclusionStateVisible, 2)

        self.assertIsInstance(AppKit.NSWindowDidChangeOcclusionStateNotification, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NSFullSizeContentViewWindowMask, 1 << 15)

        self.assertEqual(AppKit.NSWindowTitleVisible, 0)
        self.assertEqual(AppKit.NSWindowTitleHidden, 1)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(
            AppKit.NSWindowCollectionBehaviorFullScreenAllowsTiling, 1 << 11
        )
        self.assertEqual(
            AppKit.NSWindowCollectionBehaviorFullScreenDisallowsTiling, 1 << 12
        )
        self.assertEqual(AppKit.NSWindowCollectionBehaviorPrimary, 1 << 16)
        self.assertEqual(AppKit.NSWindowCollectionBehaviorAuxiliary, 1 << 17)
        self.assertEqual(
            AppKit.NSWindowCollectionBehaviorCanJoinAllApplications, 1 << 18
        )

    @skipUnless(Quartz is not None, "test requires Quartz")
    def testMagicConstants(self):
        self.assertEqual(AppKit.NSNormalWindowLevel, Quartz.kCGNormalWindowLevel)
        self.assertEqual(AppKit.NSFloatingWindowLevel, Quartz.kCGFloatingWindowLevel)
        self.assertEqual(AppKit.NSSubmenuWindowLevel, Quartz.kCGTornOffMenuWindowLevel)
        self.assertEqual(
            AppKit.NSTornOffMenuWindowLevel, Quartz.kCGTornOffMenuWindowLevel
        )
        self.assertEqual(AppKit.NSMainMenuWindowLevel, Quartz.kCGMainMenuWindowLevel)
        self.assertEqual(AppKit.NSStatusWindowLevel, Quartz.kCGStatusWindowLevel)
        self.assertEqual(AppKit.NSDockWindowLevel, Quartz.kCGDockWindowLevel)
        self.assertEqual(
            AppKit.NSModalPanelWindowLevel, Quartz.kCGModalPanelWindowLevel
        )
        self.assertEqual(AppKit.NSPopUpMenuWindowLevel, Quartz.kCGPopUpMenuWindowLevel)
        self.assertEqual(
            AppKit.NSScreenSaverWindowLevel, Quartz.kCGScreenSaverWindowLevel
        )

    def testMethods(self):
        self.assertArgIsBOOL(
            AppKit.NSWindow.nextEventMatchingMask_untilDate_inMode_dequeue_, 3
        )
        self.assertArgIsBOOL(
            AppKit.NSWindow.initWithContentRect_styleMask_backing_defer_, 3
        )
        self.assertArgIsBOOL(
            AppKit.NSWindow.initWithContentRect_styleMask_backing_defer_screen_, 3
        )
        self.assertArgIsBOOL(AppKit.NSWindow.setExcludedFromWindowsMenu_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isExcludedFromWindowsMenu)
        self.assertArgIsBOOL(AppKit.NSWindow.fieldEditor_forObject_, 0)
        self.assertArgIsBOOL(AppKit.NSWindow.setFrame_display_, 1)
        self.assertArgIsBOOL(AppKit.NSWindow.setFrame_display_animate_, 1)
        self.assertArgIsBOOL(AppKit.NSWindow.setFrame_display_animate_, 2)
        self.assertArgIsBOOL(AppKit.NSWindow.setShowsResizeIndicator_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.showsResizeIndicator)
        self.assertArgIsBOOL(AppKit.NSWindow.useOptimizedDrawing_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isFlushWindowDisabled)
        self.assertResultIsBOOL(AppKit.NSWindow.viewsNeedDisplay)
        self.assertArgIsBOOL(AppKit.NSWindow.setViewsNeedDisplay_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isAutodisplay)
        self.assertArgIsBOOL(AppKit.NSWindow.setAutodisplay_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.preservesContentDuringLiveResize)
        self.assertArgIsBOOL(AppKit.NSWindow.setPreservesContentDuringLiveResize_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.makeFirstResponder_)
        self.assertArgIsBOOL(AppKit.NSWindow.setReleasedWhenClosed_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isReleasedWhenClosed)
        self.assertResultIsBOOL(AppKit.NSWindow.isZoomed)
        self.assertResultIsBOOL(AppKit.NSWindow.isMiniaturized)
        self.assertResultIsBOOL(AppKit.NSWindow.tryToPerform_with_)
        self.assertResultIsBOOL(AppKit.NSWindow.isMovableByWindowBackground)
        self.assertArgIsBOOL(AppKit.NSWindow.setMovableByWindowBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.hidesOnDeactivate)
        self.assertArgIsBOOL(AppKit.NSWindow.setHidesOnDeactivate_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.canHide)
        self.assertArgIsBOOL(AppKit.NSWindow.setCanHide_, 0)
        self.assertArgIsBOOL(AppKit.NSWindow.setDocumentEdited_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isDocumentEdited)
        self.assertResultIsBOOL(AppKit.NSWindow.isVisible)
        self.assertResultIsBOOL(AppKit.NSWindow.isKeyWindow)
        self.assertResultIsBOOL(AppKit.NSWindow.isMainWindow)
        self.assertResultIsBOOL(AppKit.NSWindow.canBecomeKeyWindow)
        self.assertResultIsBOOL(AppKit.NSWindow.canBecomeMainWindow)
        self.assertResultIsBOOL(AppKit.NSWindow.worksWhenModal)
        self.assertResultIsBOOL(AppKit.NSWindow.isOneShot)
        self.assertArgIsBOOL(AppKit.NSWindow.setOneShot_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.areCursorRectsEnabled)
        self.assertArgIsBOOL(
            AppKit.NSWindow.setAllowsToolTipsWhenApplicationIsInactive_, 0
        )
        self.assertResultIsBOOL(AppKit.NSWindow.allowsToolTipsWhenApplicationIsInactive)
        self.assertArgIsBOOL(AppKit.NSWindow.setDynamicDepthLimit_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.hasDynamicDepthLimit)
        self.assertArgIsBOOL(AppKit.NSWindow.setHasShadow_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.hasShadow)
        self.assertResultIsBOOL(AppKit.NSWindow.canStoreColor)
        self.assertArgIsBOOL(AppKit.NSWindow.setOpaque_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isOpaque)
        self.assertArgIsBOOL(AppKit.NSWindow.setDisplaysWhenScreenProfileChanges_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.displaysWhenScreenProfileChanges)
        self.assertResultIsBOOL(AppKit.NSWindow.setFrameUsingName_force_)
        self.assertArgIsBOOL(AppKit.NSWindow.setFrameUsingName_force_, 1)
        self.assertResultIsBOOL(AppKit.NSWindow.setFrameUsingName_)
        self.assertResultIsBOOL(AppKit.NSWindow.setFrameAutosaveName_)
        self.assertArgIsBOOL(AppKit.NSWindow.postEvent_atStart_, 1)
        self.assertResultIsBOOL(AppKit.NSWindow.acceptsMouseMovedEvents)
        self.assertArgIsBOOL(AppKit.NSWindow.setAcceptsMouseMovedEvents_, 0)
        self.assertArgIsBOOL(AppKit.NSWindow.setIgnoresMouseEvents_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.ignoresMouseEvents)
        self.assertResultIsBOOL(AppKit.NSWindow.isSheet)
        self.assertArgIsBOOL(AppKit.NSWindow.setAutorecalculatesKeyViewLoop_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.autorecalculatesKeyViewLoop)
        self.assertArgIsBOOL(AppKit.NSWindow.setShowsToolbarButton_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.showsToolbarButton)
        self.assertArgIsBOOL(
            AppKit.NSWindow.dragImage_at_offset_event_pasteboard_source_slideBack_, 6
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(
            AppKit.NSWindow.autorecalculatesContentBorderThicknessForEdge_
        )
        self.assertArgIsBOOL(
            AppKit.NSWindow.setAutorecalculatesContentBorderThickness_forEdge_, 0
        )
        self.assertArgIsBOOL(AppKit.NSWindow.setCanBecomeVisibleWithoutLogin_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.canBecomeVisibleWithoutLogin)
        self.assertResultIsBOOL(AppKit.NSWindow.canBeVisibleOnAllSpaces)
        self.assertArgIsBOOL(AppKit.NSWindow.setCanBeVisibleOnAllSpaces_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSWindow.inLiveResize)
        self.assertResultIsBOOL(AppKit.NSWindow.isOnActiveSpace)
        self.assertResultIsBOOL(AppKit.NSWindow.isMovable)
        self.assertArgIsBOOL(AppKit.NSWindow.setMovable_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.preventsApplicationTerminationWhenModal)
        self.assertArgIsBOOL(
            AppKit.NSWindow.setPreventsApplicationTerminationWhenModal_, 0
        )
        self.assertResultIsBOOL(AppKit.NSWindow.allowsConcurrentViewDrawing)
        self.assertArgIsBOOL(AppKit.NSWindow.setAllowsConcurrentViewDrawing_, 0)

        self.assertArgHasType(
            AppKit.NSWindow.windowNumberAtPoint_belowWindowWithWindowNumber_,
            0,
            AppKit.NSPoint.__typestr__,
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            AppKit.NSWindow.beginSheet_completionHandler_, 1, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            AppKit.NSWindow.beginCriticalSheet_completionHandler_,
            1,
            b"v" + objc._C_NSInteger,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSWindow.titlebarAppearsTransparent)
        self.assertArgIsBOOL(AppKit.NSWindow.setTitlebarAppearsTransparent_, 0)

        self.assertArgIsBlock(
            AppKit.NSWindow.trackEventsMatchingMask_timeout_mode_handler_, 3, b"v@o^Z"
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSWindow.canRepresentDisplayGamut_)

        self.assertResultIsBOOL(AppKit.NSWindow.allowsAutomaticWindowTabbing)
        self.assertArgIsBOOL(AppKit.NSWindow.setAllowsAutomaticWindowTabbing_, 0)

    @min_os_level("13.3")
    def testMethods13_3(self):
        self.assertResultIsBOOL(AppKit.NSWindow.hasActiveWindowSharingSession)

        self.assertArgIsBlock(
            AppKit.NSWindow.transferWindowSharingToWindow_completionHandler_, 1, b"v@"
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertArgIsSEL(AppKit.NSWindow.displayLinkWithTarget_selector_, 1, b"v@:@")

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSWindowDelegate")

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSWindowHelper.windowShouldClose_)
        self.assertResultHasType(
            TestNSWindowHelper.windowWillResize_toSize_, AppKit.NSSize.__typestr__
        )
        self.assertArgHasType(
            TestNSWindowHelper.windowWillResize_toSize_, 1, AppKit.NSSize.__typestr__
        )
        self.assertResultHasType(
            TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(TestNSWindowHelper.windowShouldZoom_toFrame_)
        self.assertArgHasType(
            TestNSWindowHelper.windowShouldZoom_toFrame_, 1, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(
            TestNSWindowHelper.window_willPositionSheet_usingRect_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_willPositionSheet_usingRect_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(TestNSWindowHelper.window_shouldPopUpDocumentPathMenu_)
        self.assertResultIsBOOL(
            TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_,
            2,
            AppKit.NSPoint.__typestr__,
        )

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertArgHasType(
            TestNSWindowHelper.window_willUseFullScreenContentSize_,
            1,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_willUseFullScreenPresentationOptions_,
            1,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestNSWindowHelper.window_willUseFullScreenPresentationOptions_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_startCustomAnimationToEnterFullScreenWithDuration_,
            1,
            objc._C_DBL,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_startCustomAnimationToExitFullScreenWithDuration_,
            1,
            objc._C_DBL,
        )
        self.assertResultHasType(
            TestNSWindowHelper.window_willResizeForVersionBrowserWithMaxPreferredSize_maxAllowedSize_,  # noqa: B950
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_willResizeForVersionBrowserWithMaxPreferredSize_maxAllowedSize_,  # noqa: B950
            1,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSWindowHelper.window_willResizeForVersionBrowserWithMaxPreferredSize_maxAllowedSize_,  # noqa: B950
            2,
            AppKit.NSSize.__typestr__,
        )

    @min_os_level("10.9")
    def testProtocols10_9(self):
        self.assertArgHasType(
            TestNSWindowHelper.window_startCustomAnimationToEnterFullScreenOnScreen_withDuration_,  # noqa: B950
            2,
            objc._C_DBL,
        )
