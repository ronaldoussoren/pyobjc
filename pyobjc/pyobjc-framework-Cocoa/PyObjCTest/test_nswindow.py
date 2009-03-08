
from PyObjCTools.TestSupport import *
from AppKit import *

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


        self.failUnlessEqual(NSDirectSelection = 0)
        self.failUnlessEqual(NSSelectingNext, 1)
        self.failUnlessEqual(NSSelectingPrevious, 2)

        self.failUnlessEqual(NSWindowCloseButton, 0)
        self.failUnlessEqual(NSWindowMiniaturizeButton, 1)
        self.failUnlessEqual(NSWindowZoomButton, 2)
        self.failUnlessEqual(NSWindowToolbarButton, 3)
        self.failUnlessEqual(NSWindowDocumentIconButton, 4)

        self.failUnlessIsEqual(NSWindowDidBecomeKeyNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidBecomeMainNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidChangeScreenNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidDeminiaturizeNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidExposeNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidMiniaturizeNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidMoveNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidResignKeyNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidResignMainNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidResizeNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidUpdateNotification, unicode)
        self.failUnlessIsEqual(NSWindowWillCloseNotification, unicode)
        self.failUnlessIsEqual(NSWindowWillMiniaturizeNotification, unicode)
        self.failUnlessIsEqual(NSWindowWillMoveNotification, unicode)
        self.failUnlessIsEqual(NSWindowWillBeginSheetNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidEndSheetNotification, unicode)
        self.failUnlessIsEqual(NSWindowDidChangeScreenProfileNotification, unicode)

    def testMagicConstants(self):
        # FIXME: The C code for kCGNormalWindowLevel and friends expands
        # into a function call.
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
        self.fail("- (NSWindow *)initWithWindowRef:(void * /* WindowRef */)windowRef;")
        self.fail("- (void * /* WindowRef */)windowRef;")


if __name__ == "__main__":
    main()
