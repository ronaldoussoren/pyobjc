
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGWindowLevel (TestCase):
    def testConstants(self):
        self.assertEqual(kCGBaseWindowLevelKey, 0)
        self.assertEqual(kCGMinimumWindowLevelKey, 1)
        self.assertEqual(kCGDesktopWindowLevelKey, 2)
        self.assertEqual(kCGBackstopMenuLevelKey, 3)
        self.assertEqual(kCGNormalWindowLevelKey, 4)
        self.assertEqual(kCGFloatingWindowLevelKey, 5)
        self.assertEqual(kCGTornOffMenuWindowLevelKey, 6)
        self.assertEqual(kCGDockWindowLevelKey, 7)
        self.assertEqual(kCGMainMenuWindowLevelKey, 8)
        self.assertEqual(kCGStatusWindowLevelKey, 9)
        self.assertEqual(kCGModalPanelWindowLevelKey, 10)
        self.assertEqual(kCGPopUpMenuWindowLevelKey, 11)
        self.assertEqual(kCGDraggingWindowLevelKey, 12)
        self.assertEqual(kCGScreenSaverWindowLevelKey, 13)
        self.assertEqual(kCGMaximumWindowLevelKey, 14)
        self.assertEqual(kCGOverlayWindowLevelKey, 15)
        self.assertEqual(kCGHelpWindowLevelKey, 16)
        self.assertEqual(kCGUtilityWindowLevelKey, 17)
        self.assertEqual(kCGDesktopIconWindowLevelKey, 18)
        self.assertEqual(kCGCursorWindowLevelKey, 19)
        self.assertEqual(kCGAssistiveTechHighWindowLevelKey, 20)
        self.assertEqual(kCGNumberOfWindowLevelKeys, 21)

        self.assertEqual(kCGNumReservedWindowLevels, 16)

        lvl = CGWindowLevelForKey(kCGOverlayWindowLevelKey)
        self.assertIsInstance(lvl, (int, long))

        self.assertEqual(kCGBaseWindowLevel, CGWindowLevelForKey(kCGBaseWindowLevelKey))
        self.assertEqual(kCGMinimumWindowLevel, CGWindowLevelForKey(kCGMinimumWindowLevelKey))
        self.assertEqual(kCGDesktopWindowLevel, CGWindowLevelForKey(kCGDesktopWindowLevelKey))
        self.assertEqual(kCGDesktopIconWindowLevel, CGWindowLevelForKey(kCGDesktopIconWindowLevelKey))
        self.assertEqual(kCGBackstopMenuLevel, CGWindowLevelForKey(kCGBackstopMenuLevelKey))
        self.assertEqual(kCGNormalWindowLevel, CGWindowLevelForKey(kCGNormalWindowLevelKey))
        self.assertEqual(kCGFloatingWindowLevel, CGWindowLevelForKey(kCGFloatingWindowLevelKey))
        self.assertEqual(kCGTornOffMenuWindowLevel, CGWindowLevelForKey(kCGTornOffMenuWindowLevelKey))
        self.assertEqual(kCGDockWindowLevel, CGWindowLevelForKey(kCGDockWindowLevelKey))
        self.assertEqual(kCGMainMenuWindowLevel, CGWindowLevelForKey(kCGMainMenuWindowLevelKey))
        self.assertEqual(kCGStatusWindowLevel, CGWindowLevelForKey(kCGStatusWindowLevelKey))
        self.assertEqual(kCGModalPanelWindowLevel, CGWindowLevelForKey(kCGModalPanelWindowLevelKey))
        self.assertEqual(kCGPopUpMenuWindowLevel, CGWindowLevelForKey(kCGPopUpMenuWindowLevelKey))
        self.assertEqual(kCGDraggingWindowLevel, CGWindowLevelForKey(kCGDraggingWindowLevelKey))
        self.assertEqual(kCGScreenSaverWindowLevel, CGWindowLevelForKey(kCGScreenSaverWindowLevelKey))
        self.assertEqual(kCGCursorWindowLevel, CGWindowLevelForKey(kCGCursorWindowLevelKey))
        self.assertEqual(kCGOverlayWindowLevel, CGWindowLevelForKey(kCGOverlayWindowLevelKey))
        self.assertEqual(kCGHelpWindowLevel, CGWindowLevelForKey(kCGHelpWindowLevelKey))
        self.assertEqual(kCGUtilityWindowLevel, CGWindowLevelForKey(kCGUtilityWindowLevelKey))
        self.assertEqual(kCGAssistiveTechHighWindowLevel, CGWindowLevelForKey(kCGAssistiveTechHighWindowLevelKey))
        self.assertEqual(kCGMaximumWindowLevel, CGWindowLevelForKey(kCGMaximumWindowLevelKey))

if __name__ == "__main__":
    main()
