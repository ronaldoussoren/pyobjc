
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSButtonCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSMomentaryLightButton, 0)
        self.assertEqual(NSPushOnPushOffButton, 1)
        self.assertEqual(NSToggleButton, 2)
        self.assertEqual(NSSwitchButton, 3)
        self.assertEqual(NSRadioButton, 4)
        self.assertEqual(NSMomentaryChangeButton, 5)
        self.assertEqual(NSOnOffButton, 6)
        self.assertEqual(NSMomentaryPushInButton, 7)
        self.assertEqual(NSMomentaryPushButton, 0)
        self.assertEqual(NSMomentaryLight, 7)
        self.assertEqual(NSRoundedBezelStyle, 1)
        self.assertEqual(NSRegularSquareBezelStyle, 2)
        self.assertEqual(NSThickSquareBezelStyle, 3)
        self.assertEqual(NSThickerSquareBezelStyle, 4)
        self.assertEqual(NSDisclosureBezelStyle, 5)
        self.assertEqual(NSShadowlessSquareBezelStyle, 6)
        self.assertEqual(NSCircularBezelStyle, 7)
        self.assertEqual(NSTexturedSquareBezelStyle, 8)
        self.assertEqual(NSHelpButtonBezelStyle, 9)
        self.assertEqual(NSSmallSquareBezelStyle, 10)
        self.assertEqual(NSTexturedRoundedBezelStyle, 11)
        self.assertEqual(NSRoundRectBezelStyle, 12)
        self.assertEqual(NSRecessedBezelStyle, 13)
        self.assertEqual(NSRoundedDisclosureBezelStyle, 14)
        self.assertEqual(NSSmallIconButtonBezelStyle, 2)

        self.assertEqual(NSGradientNone, 0)
        self.assertEqual(NSGradientConcaveWeak, 1)
        self.assertEqual(NSGradientConcaveStrong, 2)
        self.assertEqual(NSGradientConvexWeak, 3)
        self.assertEqual(NSGradientConvexStrong, 4)


    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSInlineBezelStyle, 15)

    def testMethods(self):
        self.assertResultIsBOOL(NSButtonCell.isOpaque)
        self.assertResultIsBOOL(NSButtonCell.isTransparent)
        self.assertArgIsBOOL(NSButtonCell.setTransparent_, 0)

        self.assertArgIsOut(NSButtonCell.getPeriodicDelay_interval_, 0)
        self.assertArgIsOut(NSButtonCell.getPeriodicDelay_interval_, 1)

        self.assertResultIsBOOL(NSButtonCell.imageDimsWhenDisabled)
        self.assertArgIsBOOL(NSButtonCell.setImageDimsWhenDisabled_, 0)
        self.assertResultIsBOOL(NSButtonCell.showsBorderOnlyWhileMouseInside)
        self.assertArgIsBOOL(NSButtonCell.setShowsBorderOnlyWhileMouseInside_, 0)

if __name__ == "__main__":
    main()
