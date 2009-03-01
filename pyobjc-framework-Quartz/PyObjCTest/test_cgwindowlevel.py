
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGWindowLevel (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGBaseWindowLevelKey, 0)
        self.failUnlessEqual(kCGMinimumWindowLevelKey, 1)
        self.failUnlessEqual(kCGDesktopWindowLevelKey, 2)
        self.failUnlessEqual(kCGBackstopMenuLevelKey, 3)
        self.failUnlessEqual(kCGNormalWindowLevelKey, 4)
        self.failUnlessEqual(kCGFloatingWindowLevelKey, 5)
        self.failUnlessEqual(kCGTornOffMenuWindowLevelKey, 6)
        self.failUnlessEqual(kCGDockWindowLevelKey, 7)
        self.failUnlessEqual(kCGMainMenuWindowLevelKey, 8)
        self.failUnlessEqual(kCGStatusWindowLevelKey, 9)
        self.failUnlessEqual(kCGModalPanelWindowLevelKey, 10)
        self.failUnlessEqual(kCGPopUpMenuWindowLevelKey, 11)
        self.failUnlessEqual(kCGDraggingWindowLevelKey, 12)
        self.failUnlessEqual(kCGScreenSaverWindowLevelKey, 13)
        self.failUnlessEqual(kCGMaximumWindowLevelKey, 14)
        self.failUnlessEqual(kCGOverlayWindowLevelKey, 15)
        self.failUnlessEqual(kCGHelpWindowLevelKey, 16)
        self.failUnlessEqual(kCGUtilityWindowLevelKey, 17)
        self.failUnlessEqual(kCGDesktopIconWindowLevelKey, 18)
        self.failUnlessEqual(kCGCursorWindowLevelKey, 19)
        self.failUnlessEqual(kCGAssistiveTechHighWindowLevelKey, 20)
        self.failUnlessEqual(kCGNumberOfWindowLevelKeys, 21)

        self.failUnlessEqual(kCGNumReservedWindowLevels, 16)

        lvl = CGWindowLevelForKey(kCGOverlayWindowLevelKey)
        self.failUnlessIsInstance(lvl, (int, long))

        self.failUnlessEqual(kCGBaseWindowLevel, CGWindowLevelForKey(kCGBaseWindowLevelKey))
        self.failUnlessEqual(kCGMinimumWindowLevel, CGWindowLevelForKey(kCGMinimumWindowLevelKey))
        self.failUnlessEqual(kCGDesktopWindowLevel, CGWindowLevelForKey(kCGDesktopWindowLevelKey))
        self.failUnlessEqual(kCGDesktopIconWindowLevel, CGWindowLevelForKey(kCGDesktopIconWindowLevelKey))
        self.failUnlessEqual(kCGBackstopMenuLevel, CGWindowLevelForKey(kCGBackstopMenuLevelKey))
        self.failUnlessEqual(kCGNormalWindowLevel, CGWindowLevelForKey(kCGNormalWindowLevelKey))
        self.failUnlessEqual(kCGFloatingWindowLevel, CGWindowLevelForKey(kCGFloatingWindowLevelKey))
        self.failUnlessEqual(kCGTornOffMenuWindowLevel, CGWindowLevelForKey(kCGTornOffMenuWindowLevelKey))
        self.failUnlessEqual(kCGDockWindowLevel, CGWindowLevelForKey(kCGDockWindowLevelKey))
        self.failUnlessEqual(kCGMainMenuWindowLevel, CGWindowLevelForKey(kCGMainMenuWindowLevelKey))
        self.failUnlessEqual(kCGStatusWindowLevel, CGWindowLevelForKey(kCGStatusWindowLevelKey))
        self.failUnlessEqual(kCGModalPanelWindowLevel, CGWindowLevelForKey(kCGModalPanelWindowLevelKey))
        self.failUnlessEqual(kCGPopUpMenuWindowLevel, CGWindowLevelForKey(kCGPopUpMenuWindowLevelKey))
        self.failUnlessEqual(kCGDraggingWindowLevel, CGWindowLevelForKey(kCGDraggingWindowLevelKey))
        self.failUnlessEqual(kCGScreenSaverWindowLevel, CGWindowLevelForKey(kCGScreenSaverWindowLevelKey))
        self.failUnlessEqual(kCGCursorWindowLevel, CGWindowLevelForKey(kCGCursorWindowLevelKey))
        self.failUnlessEqual(kCGOverlayWindowLevel, CGWindowLevelForKey(kCGOverlayWindowLevelKey))
        self.failUnlessEqual(kCGHelpWindowLevel, CGWindowLevelForKey(kCGHelpWindowLevelKey))
        self.failUnlessEqual(kCGUtilityWindowLevel, CGWindowLevelForKey(kCGUtilityWindowLevelKey))
        self.failUnlessEqual(kCGAssistiveTechHighWindowLevel, CGWindowLevelForKey(kCGAssistiveTechHighWindowLevelKey))
        self.failUnlessEqual(kCGMaximumWindowLevel, CGWindowLevelForKey(kCGMaximumWindowLevelKey))

if __name__ == "__main__":
    main()
