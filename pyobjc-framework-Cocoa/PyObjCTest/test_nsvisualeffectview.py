from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSVisualEffectView (TestCase):

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSVisualEffectMaterialAppearanceBased, 0)
        self.assertEqual(NSVisualEffectMaterialLight, 1)
        self.assertEqual(NSVisualEffectMaterialDark, 2)
        self.assertEqual(NSVisualEffectMaterialTitlebar, 3)

        self.assertEqual(NSVisualEffectBlendingModeBehindWindow, 0)
        self.assertEqual(NSVisualEffectBlendingModeWithinWindow, 1)

        self.assertEqual(NSVisualEffectStateFollowsWindowActiveState, 0)
        self.assertEqual(NSVisualEffectStateActive, 1)
        self.assertEqual(NSVisualEffectStateInactive, 2)



if __name__ == "__main__":
    main()
