from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGWindowLevel(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGBaseWindowLevelKey, 0)
        self.assertEqual(Quartz.kCGMinimumWindowLevelKey, 1)
        self.assertEqual(Quartz.kCGDesktopWindowLevelKey, 2)
        self.assertEqual(Quartz.kCGBackstopMenuLevelKey, 3)
        self.assertEqual(Quartz.kCGNormalWindowLevelKey, 4)
        self.assertEqual(Quartz.kCGFloatingWindowLevelKey, 5)
        self.assertEqual(Quartz.kCGTornOffMenuWindowLevelKey, 6)
        self.assertEqual(Quartz.kCGDockWindowLevelKey, 7)
        self.assertEqual(Quartz.kCGMainMenuWindowLevelKey, 8)
        self.assertEqual(Quartz.kCGStatusWindowLevelKey, 9)
        self.assertEqual(Quartz.kCGModalPanelWindowLevelKey, 10)
        self.assertEqual(Quartz.kCGPopUpMenuWindowLevelKey, 11)
        self.assertEqual(Quartz.kCGDraggingWindowLevelKey, 12)
        self.assertEqual(Quartz.kCGScreenSaverWindowLevelKey, 13)
        self.assertEqual(Quartz.kCGMaximumWindowLevelKey, 14)
        self.assertEqual(Quartz.kCGOverlayWindowLevelKey, 15)
        self.assertEqual(Quartz.kCGHelpWindowLevelKey, 16)
        self.assertEqual(Quartz.kCGUtilityWindowLevelKey, 17)
        self.assertEqual(Quartz.kCGDesktopIconWindowLevelKey, 18)
        self.assertEqual(Quartz.kCGCursorWindowLevelKey, 19)
        self.assertEqual(Quartz.kCGAssistiveTechHighWindowLevelKey, 20)
        self.assertEqual(Quartz.kCGNumberOfWindowLevelKeys, 21)

        self.assertEqual(Quartz.kCGNumReservedWindowLevels, 16)

        lvl = Quartz.CGWindowLevelForKey(Quartz.kCGOverlayWindowLevelKey)
        self.assertIsInstance(lvl, int)

        self.assertEqual(
            Quartz.kCGBaseWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGBaseWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGMinimumWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGMinimumWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGDesktopWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGDesktopWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGDesktopIconWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGDesktopIconWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGBackstopMenuLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGBackstopMenuLevelKey),
        )
        self.assertEqual(
            Quartz.kCGNormalWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGNormalWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGFloatingWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGFloatingWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGTornOffMenuWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGTornOffMenuWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGDockWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGDockWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGMainMenuWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGMainMenuWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGStatusWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGStatusWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGModalPanelWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGModalPanelWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGPopUpMenuWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGPopUpMenuWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGDraggingWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGDraggingWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGScreenSaverWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGScreenSaverWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGCursorWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGCursorWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGOverlayWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGOverlayWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGHelpWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGHelpWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGUtilityWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGUtilityWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGAssistiveTechHighWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGAssistiveTechHighWindowLevelKey),
        )
        self.assertEqual(
            Quartz.kCGMaximumWindowLevel,
            Quartz.CGWindowLevelForKey(Quartz.kCGMaximumWindowLevelKey),
        )
