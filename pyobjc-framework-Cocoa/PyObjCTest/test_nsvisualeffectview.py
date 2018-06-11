from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSVisualEffectView (TestCase):

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSVisualEffectMaterialAppearanceBased, 0)
        self.assertEqual(NSVisualEffectMaterialLight, 1)
        self.assertEqual(NSVisualEffectMaterialDark, 2)
        self.assertEqual(NSVisualEffectMaterialTitlebar, 3)
        self.assertEqual(NSVisualEffectMaterialSelection, 4)
        self.assertEqual(NSVisualEffectMaterialMenu, 5)
        self.assertEqual(NSVisualEffectMaterialPopover, 6)
        self.assertEqual(NSVisualEffectMaterialSidebar, 7)
        self.assertEqual(NSVisualEffectMaterialMediumLight, 8)
        self.assertEqual(NSVisualEffectMaterialUltraDark, 9)
        self.assertEqual(NSVisualEffectMaterialHeaderView, 10)
        self.assertEqual(NSVisualEffectMaterialSheet, 11)
        self.assertEqual(NSVisualEffectMaterialWindowBackground, 12)
        self.assertEqual(NSVisualEffectMaterialHUDWindow, 13)
        self.assertEqual(NSVisualEffectMaterialFullScreenUI, 15)
        self.assertEqual(NSVisualEffectMaterialToolTip, 17)
        self.assertEqual(NSVisualEffectMaterialContentBackground, 18)
        self.assertEqual(NSVisualEffectMaterialUnderWindowBackground, 21)
        self.assertEqual(NSVisualEffectMaterialUnderPageBackground, 22)

        self.assertEqual(NSVisualEffectBlendingModeBehindWindow, 0)
        self.assertEqual(NSVisualEffectBlendingModeWithinWindow, 1)

        self.assertEqual(NSVisualEffectStateFollowsWindowActiveState, 0)
        self.assertEqual(NSVisualEffectStateActive, 1)
        self.assertEqual(NSVisualEffectStateInactive, 2)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSVisualEffectView.isEmphasized)
        self.assertArgIsBOOL(NSVisualEffectView.setEmphasized_, 0)

if __name__ == "__main__":
    main()
