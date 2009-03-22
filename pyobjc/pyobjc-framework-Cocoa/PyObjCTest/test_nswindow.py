from PyObjCTools.TestSupport import *
from AppKit import *
from Quartz.CoreGraphics import *

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
        self.failUnlessEqual(NSBorderlessWindowMask, 0)
        self.failUnlessEqual(NSTitledWindowMask, 1 << 0)
        self.failUnlessEqual(NSClosableWindowMask, 1 << 1)
        self.failUnlessEqual(NSMiniaturizableWindowMask, 1 << 2)
        self.failUnlessEqual(NSResizableWindowMask, 1 << 3)

        self.failUnlessEqual(NSTexturedBackgroundWindowMask, 1 << 8)

        self.failUnlessEqual(NSUnscaledWindowMask, 1 << 11)

        self.failUnlessEqual(NSUnifiedTitleAndToolbarWindowMask, 1 << 12)

        self.failUnlessEqual(NSDisplayWindowRunLoopOrdering, 600000)
        self.failUnlessEqual(NSResetCursorRectsRunLoopOrdering, 700000)

        self.failUnlessEqual(NSWindowSharingNone, 0)
        self.failUnlessEqual(NSWindowSharingReadOnly, 1)
        self.failUnlessEqual(NSWindowSharingReadWrite, 2)

        self.failUnlessEqual(NSWindowBackingLocationDefault, 0)
        self.failUnlessEqual(NSWindowBackingLocationVideoMemory, 1)
        self.failUnlessEqual(NSWindowBackingLocationMainMemory, 2)

        self.failUnlessEqual(NSWindowCollectionBehaviorDefault, 0)
        self.failUnlessEqual(NSWindowCollectionBehaviorCanJoinAllSpaces, 1 << 0)
        self.failUnlessEqual(NSWindowCollectionBehaviorMoveToActiveSpace, 1 << 1)


        self.failUnlessEqual(NSDirectSelection, 0)
        self.failUnlessEqual(NSSelectingNext, 1)
        self.failUnlessEqual(NSSelectingPrevious, 2)

        self.failUnlessEqual(NSWindowCloseButton, 0)
        self.failUnlessEqual(NSWindowMiniaturizeButton, 1)
        self.failUnlessEqual(NSWindowZoomButton, 2)
        self.failUnlessEqual(NSWindowToolbarButton, 3)
        self.failUnlessEqual(NSWindowDocumentIconButton, 4)

        self.failUnlessIsInstance(NSWindowDidBecomeKeyNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidBecomeMainNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidChangeScreenNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidDeminiaturizeNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidExposeNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidMiniaturizeNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidMoveNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidResignKeyNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidResignMainNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidResizeNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidUpdateNotification, unicode)
        self.failUnlessIsInstance(NSWindowWillCloseNotification, unicode)
        self.failUnlessIsInstance(NSWindowWillMiniaturizeNotification, unicode)
        self.failUnlessIsInstance(NSWindowWillMoveNotification, unicode)
        self.failUnlessIsInstance(NSWindowWillBeginSheetNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidEndSheetNotification, unicode)
        self.failUnlessIsInstance(NSWindowDidChangeScreenProfileNotification, unicode)

    def testMagicConstants(self):
        self.failUnlessEqual(NSNormalWindowLevel, kCGNormalWindowLevel)
        self.failUnlessEqual(NSFloatingWindowLevel, kCGFloatingWindowLevel)
        self.failUnlessEqual(NSSubmenuWindowLevel, kCGTornOffMenuWindowLevel)
        self.failUnlessEqual(NSTornOffMenuWindowLevel, kCGTornOffMenuWindowLevel)
        self.failUnlessEqual(NSMainMenuWindowLevel, kCGMainMenuWindowLevel)
        self.failUnlessEqual(NSStatusWindowLevel, kCGStatusWindowLevel)
        self.failUnlessEqual(NSDockWindowLevel, kCGDockWindowLevel)
        self.failUnlessEqual(NSModalPanelWindowLevel, kCGModalPanelWindowLevel)
        self.failUnlessEqual(NSPopUpMenuWindowLevel, kCGPopUpMenuWindowLevel)
        self.failUnlessEqual(NSScreenSaverWindowLevel, kCGScreenSaverWindowLevel)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSWindow.initWithContentRect_styleMask_backing_defer_, 3)
        self.failUnlessArgIsBOOL(NSWindow.initWithContentRect_styleMask_backing_defer_screen_, 3)
        self.failUnlessArgIsBOOL(NSWindow.setExcludedFromWindowsMenu_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isExcludedFromWindowsMenu)
        self.failUnlessArgIsBOOL(NSWindow.fieldEditor_forObject_, 0)
        self.failUnlessArgIsBOOL(NSWindow.setFrame_display_, 1)
        self.failUnlessArgIsBOOL(NSWindow.setFrame_display_animate_, 1)
        self.failUnlessArgIsBOOL(NSWindow.setFrame_display_animate_, 2)
        self.failUnlessArgIsBOOL(NSWindow.setShowsResizeIndicator_, 0)
        self.failUnlessResultIsBOOL(NSWindow.showsResizeIndicator)
        self.failUnlessArgIsBOOL(NSWindow.useOptimizedDrawing_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isFlushWindowDisabled)
        self.failUnlessResultIsBOOL(NSWindow.viewsNeedDisplay)
        self.failUnlessArgIsBOOL(NSWindow.setViewsNeedDisplay_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isAutodisplay)
        self.failUnlessArgIsBOOL(NSWindow.setAutodisplay_, 0)
        self.failUnlessResultIsBOOL(NSWindow.preservesContentDuringLiveResize)
        self.failUnlessArgIsBOOL(NSWindow.setPreservesContentDuringLiveResize_, 0)
        self.failUnlessResultIsBOOL(NSWindow.makeFirstResponder_)
        self.failUnlessArgIsBOOL(NSWindow.setReleasedWhenClosed_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isReleasedWhenClosed)
        self.failUnlessResultIsBOOL(NSWindow.isZoomed)
        self.failUnlessResultIsBOOL(NSWindow.isMiniaturized)
        self.failUnlessResultIsBOOL(NSWindow.tryToPerform_with_)
        self.failUnlessResultIsBOOL(NSWindow.isMovableByWindowBackground)
        self.failUnlessArgIsBOOL(NSWindow.setMovableByWindowBackground_, 0)
        self.failUnlessResultIsBOOL(NSWindow.hidesOnDeactivate)
        self.failUnlessArgIsBOOL(NSWindow.setHidesOnDeactivate_, 0)
        self.failUnlessResultIsBOOL(NSWindow.canHide)
        self.failUnlessArgIsBOOL(NSWindow.setCanHide_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isDocumentEdited)
        self.failUnlessArgIsBOOL(NSWindow.setDocumentEdited_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isDocumentEdited)
        self.failUnlessResultIsBOOL(NSWindow.isVisible)
        self.failUnlessResultIsBOOL(NSWindow.isKeyWindow)
        self.failUnlessResultIsBOOL(NSWindow.isMainWindow)
        self.failUnlessResultIsBOOL(NSWindow.canBecomeKeyWindow)
        self.failUnlessResultIsBOOL(NSWindow.canBecomeMainWindow)
        self.failUnlessResultIsBOOL(NSWindow.worksWhenModal)
        self.failUnlessResultIsBOOL(NSWindow.isOneShot)
        self.failUnlessArgIsBOOL(NSWindow.setOneShot_, 0)
        self.failUnlessResultIsBOOL(NSWindow.areCursorRectsEnabled)
        self.failUnlessArgIsBOOL(NSWindow.setAllowsToolTipsWhenApplicationIsInactive_, 0)
        self.failUnlessResultIsBOOL(NSWindow.allowsToolTipsWhenApplicationIsInactive)
        self.failUnlessArgIsBOOL(NSWindow.setDynamicDepthLimit_, 0)
        self.failUnlessResultIsBOOL(NSWindow.hasDynamicDepthLimit)
        self.failUnlessArgIsBOOL(NSWindow.setHasShadow_, 0)
        self.failUnlessResultIsBOOL(NSWindow.hasShadow)
        self.failUnlessResultIsBOOL(NSWindow.canStoreColor)
        self.failUnlessArgIsBOOL(NSWindow.setOpaque_, 0)
        self.failUnlessResultIsBOOL(NSWindow.isOpaque)
        self.failUnlessArgIsBOOL(NSWindow.setDisplaysWhenScreenProfileChanges_, 0)
        self.failUnlessResultIsBOOL(NSWindow.displaysWhenScreenProfileChanges)
        self.failUnlessResultIsBOOL(NSWindow.setFrameUsingName_force_)
        self.failUnlessArgIsBOOL(NSWindow.setFrameUsingName_force_, 1)
        self.failUnlessResultIsBOOL(NSWindow.setFrameUsingName_)
        self.failUnlessResultIsBOOL(NSWindow.setFrameAutosaveName_)
        self.failUnlessArgIsBOOL(NSWindow.postEvent_atStart_, 1)
        self.failUnlessResultIsBOOL(NSWindow.acceptsMouseMovedEvents)
        self.failUnlessArgIsBOOL(NSWindow.setIgnoresMouseEvents_, 0)
        self.failUnlessResultIsBOOL(NSWindow.ignoresMouseEvents)
        self.failUnlessResultIsBOOL(NSWindow.isSheet)
        self.failUnlessArgIsBOOL(NSWindow.setAutorecalculatesKeyViewLoop_, 0)
        self.failUnlessResultIsBOOL(NSWindow.autorecalculatesKeyViewLoop)
        self.failUnlessArgIsBOOL(NSWindow.setShowsToolbarButton_, 0)
        self.failUnlessResultIsBOOL(NSWindow.showsToolbarButton)
        self.failUnlessArgIsBOOL(NSWindow.dragImage_at_offset_event_pasteboard_source_slideBack_, 6)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSWindow.autorecalculatesContentBorderThicknessForEdge_)
        self.failUnlessArgIsBOOL(NSWindow.setAutorecalculatesContentBorderThickness_forEdge_, 0)
        self.failUnlessArgIsBOOL(NSWindow.setCanBecomeVisibleWithoutLogin_, 0)
        self.failUnlessResultIsBOOL(NSWindow.canBecomeVisibleWithoutLogin)
        self.failUnlessResultIsBOOL(NSWindow.canBeVisibleOnAllSpaces)
        self.failUnlessArgIsBOOL(NSWindow.setCanBeVisibleOnAllSpaces_, 0)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSWindowHelper.windowShouldClose_)
        self.failUnlessResultHasType(TestNSWindowHelper.windowWillResize_toSize_, NSSize.__typestr__)
        self.failUnlessArgHasType(TestNSWindowHelper.windowWillResize_toSize_, 1, NSSize.__typestr__)
        self.failUnlessResultHasType(TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSWindowHelper.windowWillUseStandardFrame_defaultFrame_, 1, NSRect.__typestr__)
        self.failUnlessResultIsBOOL(TestNSWindowHelper.windowShouldZoom_toFrame_)
        self.failUnlessArgHasType(TestNSWindowHelper.windowShouldZoom_toFrame_, 1, NSRect.__typestr__)
        self.failUnlessResultHasType(TestNSWindowHelper.window_willPositionSheet_usingRect_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSWindowHelper.window_willPositionSheet_usingRect_, 2, NSRect.__typestr__)
        self.failUnlessResultIsBOOL(TestNSWindowHelper.window_shouldPopUpDocumentPathMenu_)
        self.failUnlessResultIsBOOL(TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_)
        self.failUnlessArgHasType(TestNSWindowHelper.window_shouldDragDocumentWithEvent_from_withPasteboard_, 2, NSPoint.__typestr__)

if __name__ == "__main__":
    main()
