from PyObjCTools.TestSupport import *
from AppKit import *

try:
    from Quartz.CoreGraphics import *
    have_Quartz = 1
except ImportError:
    have_Quartz = 0

class TestNSWindowHelper (NSObject):
    def windowShouldClose_(self, w): return 1
    def windowWillResize_toSize_(self, w, a): return 1
    def windowWillUseStandardFrame_defaultFrame_(self, w, a): return 1
    def windowShouldZoom_toFrame_(self, w, a): return 1
    def window_willPositionSheet_usingRect_(self, w, a, b): return 1
    def window_shouldPopUpDocumentPathMenu_(self, w, a): return 1
    def window_shouldDragDocumentWithEvent_from_withPasteboard_(self, w, a, b, c): return 1

class TestNSWindow (TestCase):
    def testConstants(self):
        self.assertEqual(NSBorderlessWindowMask, 0)
        self.assertEqual(NSTitledWindowMask, 1 << 0)
        self.assertEqual(NSClosableWindowMask, 1 << 1)
        self.assertEqual(NSMiniaturizableWindowMask, 1 << 2)
        self.assertEqual(NSResizableWindowMask, 1 << 3)

        self.assertEqual(NSTexturedBackgroundWindowMask, 1 << 8)

        self.assertEqual(NSUnscaledWindowMask, 1 << 11)

        self.assertEqual(NSUnifiedTitleAndToolbarWindowMask, 1 << 12)

        self.assertEqual(NSDisplayWindowRunLoopOrdering, 600000)
        self.assertEqual(NSResetCursorRectsRunLoopOrdering, 700000)

        self.assertEqual(NSWindowSharingNone, 0)
        self.assertEqual(NSWindowSharingReadOnly, 1)
        self.assertEqual(NSWindowSharingReadWrite, 2)

        self.assertEqual(NSWindowBackingLocationDefault, 0)
        self.assertEqual(NSWindowBackingLocationVideoMemory, 1)
        self.assertEqual(NSWindowBackingLocationMainMemory, 2)

        self.assertEqual(NSWindowCollectionBehaviorDefault, 0)
        self.assertEqual(NSWindowCollectionBehaviorCanJoinAllSpaces, 1 << 0)
        self.assertEqual(NSWindowCollectionBehaviorMoveToActiveSpace, 1 << 1)


        self.assertEqual(NSDirectSelection, 0)
        self.assertEqual(NSSelectingNext, 1)
        self.assertEqual(NSSelectingPrevious, 2)

        self.assertEqual(NSWindowCloseButton, 0)
        self.assertEqual(NSWindowMiniaturizeButton, 1)
        self.assertEqual(NSWindowZoomButton, 2)
        self.assertEqual(NSWindowToolbarButton, 3)
        self.assertEqual(NSWindowDocumentIconButton, 4)

        self.assertIsInstance(NSWindowDidBecomeKeyNotification, unicode)
        self.assertIsInstance(NSWindowDidBecomeMainNotification, unicode)
        self.assertIsInstance(NSWindowDidChangeScreenNotification, unicode)
        self.assertIsInstance(NSWindowDidDeminiaturizeNotification, unicode)
        self.assertIsInstance(NSWindowDidExposeNotification, unicode)
        self.assertIsInstance(NSWindowDidMiniaturizeNotification, unicode)
        self.assertIsInstance(NSWindowDidMoveNotification, unicode)
        self.assertIsInstance(NSWindowDidResignKeyNotification, unicode)
        self.assertIsInstance(NSWindowDidResignMainNotification, unicode)
        self.assertIsInstance(NSWindowDidResizeNotification, unicode)
        self.assertIsInstance(NSWindowDidUpdateNotification, unicode)
        self.assertIsInstance(NSWindowWillCloseNotification, unicode)
        self.assertIsInstance(NSWindowWillMiniaturizeNotification, unicode)
        self.assertIsInstance(NSWindowWillMoveNotification, unicode)
        self.assertIsInstance(NSWindowWillBeginSheetNotification, unicode)
        self.assertIsInstance(NSWindowDidEndSheetNotification, unicode)
        self.assertIsInstance(NSWindowDidChangeScreenProfileNotification, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSAppKitVersionNumberWithDeferredWindowDisplaySupport, 1019.0)

        self.assertEqual(NSWindowCollectionBehaviorManaged, 1<<2)
        self.assertEqual(NSWindowCollectionBehaviorTransient, 1<<3)
        self.assertEqual(NSWindowCollectionBehaviorStationary, 1<<4)
        self.assertEqual(NSWindowCollectionBehaviorParticipatesInCycle, 1<<5)
        self.assertEqual(NSWindowCollectionBehaviorIgnoresCycle, 1<<6)
        self.assertEqual(NSWindowNumberListAllApplications, 1<<0)
        self.assertEqual(NSWindowNumberListAllSpaces, 1<<4)

        self.assertIsInstance(NSWindowWillStartLiveResizeNotification, unicode)
        self.assertIsInstance(NSWindowDidEndLiveResizeNotification, unicode)

    @onlyIf(have_Quartz)
    def testMagicConstants(self):
        self.assertEqual(NSNormalWindowLevel, kCGNormalWindowLevel)
        self.assertEqual(NSFloatingWindowLevel, kCGFloatingWindowLevel)
        self.assertEqual(NSSubmenuWindowLevel, kCGTornOffMenuWindowLevel)
        self.assertEqual(NSTornOffMenuWindowLevel, kCGTornOffMenuWindowLevel)
        self.assertEqual(NSMainMenuWindowLevel, kCGMainMenuWindowLevel)
        self.assertEqual(NSStatusWindowLevel, kCGStatusWindowLevel)
        self.assertEqual(NSDockWindowLevel, kCGDockWindowLevel)
        self.assertEqual(NSModalPanelWindowLevel, kCGModalPanelWindowLevel)
        self.assertEqual(NSPopUpMenuWindowLevel, kCGPopUpMenuWindowLevel)
        self.assertEqual(NSScreenSaverWindowLevel, kCGScreenSaverWindowLevel)

    def testMethods(self):
        self.assertArgIsBOOL(NSWindow.initWithContentRect_styleMask_backing_defer_, 3)
        self.assertArgIsBOOL(NSWindow.initWithContentRect_styleMask_backing_defer_screen_, 3)
        self.assertArgIsBOOL(NSWindow.setExcludedFromWindowsMenu_, 0)
        self.assertResultIsBOOL(NSWindow.isExcludedFromWindowsMenu)
        self.assertArgIsBOOL(NSWindow.fieldEditor_forObject_, 0)
        self.assertArgIsBOOL(NSWindow.setFrame_display_, 1)
        self.assertArgIsBOOL(NSWindow.setFrame_display_animate_, 1)
        self.assertArgIsBOOL(NSWindow.setFrame_display_animate_, 2)
        self.assertArgIsBOOL(NSWindow.setShowsResizeIndicator_, 0)
        self.assertResultIsBOOL(NSWindow.showsResizeIndicator)
        self.assertArgIsBOOL(NSWindow.useOptimizedDrawing_, 0)
        self.assertResultIsBOOL(NSWindow.isFlushWindowDisabled)
        self.assertResultIsBOOL(NSWindow.viewsNeedDisplay)
        self.assertArgIsBOOL(NSWindow.setViewsNeedDisplay_, 0)
        self.assertResultIsBOOL(NSWindow.isAutodisplay)
        self.assertArgIsBOOL(NSWindow.setAutodisplay_, 0)
        self.assertResultIsBOOL(NSWindow.preservesContentDuringLiveResize)
        self.assertArgIsBOOL(NSWindow.setPreservesContentDuringLiveResize_, 0)
        self.assertResultIsBOOL(NSWindow.makeFirstResponder_)
        self.assertArgIsBOOL(NSWindow.setReleasedWhenClosed_, 0)
        self.assertResultIsBOOL(NSWindow.isReleasedWhenClosed)
        self.assertResultIsBOOL(NSWindow.isZoomed)
        self.assertResultIsBOOL(NSWindow.isMiniaturized)
        self.assertResultIsBOOL(NSWindow.tryToPerform_with_)
        self.assertResultIsBOOL(NSWindow.isMovableByWindowBackground)
        self.assertArgIsBOOL(NSWindow.setMovableByWindowBackground_, 0)
        self.assertResultIsBOOL(NSWindow.hidesOnDeactivate)
        self.assertArgIsBOOL(NSWindow.setHidesOnDeactivate_, 0)
        self.assertResultIsBOOL(NSWindow.canHide)
        self.assertArgIsBOOL(NSWindow.setCanHide_, 0)
        self.assertResultIsBOOL(NSWindow.isDocumentEdited)
        self.assertArgIsBOOL(NSWindow.setDocumentEdited_, 0)
        self.assertResultIsBOOL(NSWindow.isDocumentEdited)
        self.assertResultIsBOOL(NSWindow.isVisible)
        self.assertResultIsBOOL(NSWindow.isKeyWindow)
        self.assertResultIsBOOL(NSWindow.isMainWindow)
        self.assertResultIsBOOL(NSWindow.canBecomeKeyWindow)
        self.assertResultIsBOOL(NSWindow.canBecomeMainWindow)
        self.assertResultIsBOOL(NSWindow.worksWhenModal)
        self.assertResultIsBOOL(NSWindow.isOneShot)
        self.assertArgIsBOOL(NSWindow.setOneShot_, 0)
        self.assertResultIsBOOL(NSWindow.areCursorRectsEnabled)
        self.assertArgIsBOOL(NSWindow.setAllowsToolTipsWhenApplicationIsInactive_, 0)
        self.assertResultIsBOOL(NSWindow.allowsToolTipsWhenApplicationIsInactive)
        self.assertArgIsBOOL(NSWindow.setDynamicDepthLimit_, 0)
        self.assertResultIsBOOL(NSWindow.hasDynamicDepthLimit)
        self.assertArgIsBOOL(NSWindow.setHasShadow_, 0)
        self.assertResultIsBOOL(NSWindow.hasShadow)
        self.assertResultIsBOOL(NSWindow.canStoreColor)
        self.assertArgIsBOOL(NSWindow.setOpaque_, 0)
        self.assertResultIsBOOL(NSWindow.isOpaque)
        self.assertArgIsBOOL(NSWindow.setDisplaysWhenScreenProfileChanges_, 0)
        self.assertResultIsBOOL(NSWindow.displaysWhenScreenProfileChanges)
        self.assertResultIsBOOL(NSWindow.setFrameUsingName_force_)
        self.assertArgIsBOOL(NSWindow.setFrameUsingName_force_, 1)
        self.assertResultIsBOOL(NSWindow.setFrameUsingName_)
        self.assertResultIsBOOL(NSWindow.setFrameAutosaveName_)
        self.assertArgIsBOOL(NSWindow.postEvent_atStart_, 1)
        self.assertResultIsBOOL(NSWindow.acceptsMouseMovedEvents)
        self.assertArgIsBOOL(NSWindow.setIgnoresMouseEvents_, 0)
        self.assertResultIsBOOL(NSWindow.ignoresMouseEvents)
        self.assertResultIsBOOL(NSWindow.isSheet)
        self.assertArgIsBOOL(NSWindow.setAutorecalculatesKeyViewLoop_, 0)
        self.assertResultIsBOOL(NSWindow.autorecalculatesKeyViewLoop)
        self.assertArgIsBOOL(NSWindow.setShowsToolbarButton_, 0)
        self.assertResultIsBOOL(NSWindow.showsToolbarButton)
        self.assertArgIsBOOL(NSWindow.dragImage_at_offset_event_pasteboard_source_slideBack_, 6)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSWindow.autorecalculatesContentBorderThicknessForEdge_)
        self.assertArgIsBOOL(NSWindow.setAutorecalculatesContentBorderThickness_forEdge_, 0)
        self.assertArgIsBOOL(NSWindow.setCanBecomeVisibleWithoutLogin_, 0)
        self.assertResultIsBOOL(NSWindow.canBecomeVisibleWithoutLogin)
        self.assertResultIsBOOL(NSWindow.canBeVisibleOnAllSpaces)
        self.assertArgIsBOOL(NSWindow.setCanBeVisibleOnAllSpaces_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSWindow.inLiveResize)
        self.assertResultIsBOOL(NSWindow.isOnActiveSpace)
        self.assertResultIsBOOL(NSWindow.isMovable)
        self.assertArgIsBOOL(NSWindow.setMovable_, 0)
        self.assertResultIsBOOL(NSWindow.preventsApplicationTerminationWhenModal)
        self.assertArgIsBOOL(NSWindow.setPreventsApplicationTerminationWhenModal_, 0)
        self.assertResultIsBOOL(NSWindow.allowsConcurrentViewDrawing)
        self.assertArgIsBOOL(NSWindow.setAllowsConcurrentViewDrawing_, 0)

        self.assertArgHasType(NSWindow.windowNumberAtPoint_belowWindowWithWindowNumber_, 0, NSPoint.__typestr__)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSWindowHelper.windowShouldClose_)
        self.assertResultHasType(TestNSWindowHelper.windowWillResize_toSize_, NSSize.__typestr__)
        self.assertArgHasType(TestNSWindowHelper.windowWillResize_toSize_, 1, NSSize.__typestr__)
        self.assertResultHasType(TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_, NSRect.__typestr__)
        self.assertArgHasType(TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_, 1, NSRect.__typestr__)
        self.assertResultIsBOOL(TestNSWindowHelper.windowShouldZoom_toFrame_)
        self.assertArgHasType(TestNSWindowHelper.windowShouldZoom_toFrame_, 1, NSRect.__typestr__)
        self.assertResultHasType(TestNSWindowHelper.window_willPositionSheet_usingRect_, NSRect.__typestr__)
        self.assertArgHasType(TestNSWindowHelper.window_willPositionSheet_usingRect_, 2, NSRect.__typestr__)
        self.assertResultIsBOOL(TestNSWindowHelper.window_shouldPopUpDocumentPathMenu_)
        self.assertResultIsBOOL(TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_)
        self.assertArgHasType(TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_, 2, NSPoint.__typestr__)

if __name__ == "__main__":
    main()
