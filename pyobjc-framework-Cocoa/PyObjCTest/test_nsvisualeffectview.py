import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSVisualEffectView(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NSVisualEffectMaterialAppearanceBased, 0)
        self.assertEqual(AppKit.NSVisualEffectMaterialLight, 1)
        self.assertEqual(AppKit.NSVisualEffectMaterialDark, 2)
        self.assertEqual(AppKit.NSVisualEffectMaterialTitlebar, 3)
        self.assertEqual(AppKit.NSVisualEffectMaterialSelection, 4)
        self.assertEqual(AppKit.NSVisualEffectMaterialMenu, 5)
        self.assertEqual(AppKit.NSVisualEffectMaterialPopover, 6)
        self.assertEqual(AppKit.NSVisualEffectMaterialSidebar, 7)
        self.assertEqual(AppKit.NSVisualEffectMaterialMediumLight, 8)
        self.assertEqual(AppKit.NSVisualEffectMaterialUltraDark, 9)
        self.assertEqual(AppKit.NSVisualEffectMaterialHeaderView, 10)
        self.assertEqual(AppKit.NSVisualEffectMaterialSheet, 11)
        self.assertEqual(AppKit.NSVisualEffectMaterialWindowBackground, 12)
        self.assertEqual(AppKit.NSVisualEffectMaterialHUDWindow, 13)
        self.assertEqual(AppKit.NSVisualEffectMaterialFullScreenUI, 15)
        self.assertEqual(AppKit.NSVisualEffectMaterialToolTip, 17)
        self.assertEqual(AppKit.NSVisualEffectMaterialContentBackground, 18)
        self.assertEqual(AppKit.NSVisualEffectMaterialUnderWindowBackground, 21)
        self.assertEqual(AppKit.NSVisualEffectMaterialUnderPageBackground, 22)

        self.assertEqual(AppKit.NSVisualEffectBlendingModeBehindWindow, 0)
        self.assertEqual(AppKit.NSVisualEffectBlendingModeWithinWindow, 1)

        self.assertEqual(AppKit.NSVisualEffectStateFollowsWindowActiveState, 0)
        self.assertEqual(AppKit.NSVisualEffectStateActive, 1)
        self.assertEqual(AppKit.NSVisualEffectStateInactive, 2)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSVisualEffectView.isEmphasized)
        self.assertArgIsBOOL(AppKit.NSVisualEffectView.setEmphasized_, 0)
