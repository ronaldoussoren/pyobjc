import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSButtonCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSMomentaryLightButton, 0)
        self.assertEqual(AppKit.NSPushOnPushOffButton, 1)
        self.assertEqual(AppKit.NSToggleButton, 2)
        self.assertEqual(AppKit.NSSwitchButton, 3)
        self.assertEqual(AppKit.NSRadioButton, 4)
        self.assertEqual(AppKit.NSMomentaryChangeButton, 5)
        self.assertEqual(AppKit.NSOnOffButton, 6)
        self.assertEqual(AppKit.NSMomentaryPushInButton, 7)
        self.assertEqual(AppKit.NSAcceleratorButton, 8)
        self.assertEqual(AppKit.NSMultiLevelAcceleratorButton, 9)

        self.assertEqual(AppKit.NSMomentaryPushButton, 0)
        self.assertEqual(AppKit.NSMomentaryLight, 7)

        self.assertEqual(AppKit.NSRoundedBezelStyle, 1)
        self.assertEqual(AppKit.NSRegularSquareBezelStyle, 2)
        self.assertEqual(AppKit.NSThickSquareBezelStyle, 3)
        self.assertEqual(AppKit.NSThickerSquareBezelStyle, 4)
        self.assertEqual(AppKit.NSDisclosureBezelStyle, 5)
        self.assertEqual(AppKit.NSShadowlessSquareBezelStyle, 6)
        self.assertEqual(AppKit.NSCircularBezelStyle, 7)
        self.assertEqual(AppKit.NSTexturedSquareBezelStyle, 8)
        self.assertEqual(AppKit.NSHelpButtonBezelStyle, 9)
        self.assertEqual(AppKit.NSSmallSquareBezelStyle, 10)
        self.assertEqual(AppKit.NSTexturedRoundedBezelStyle, 11)
        self.assertEqual(AppKit.NSRoundRectBezelStyle, 12)
        self.assertEqual(AppKit.NSRecessedBezelStyle, 13)
        self.assertEqual(AppKit.NSRoundedDisclosureBezelStyle, 14)
        self.assertEqual(AppKit.NSSmallIconButtonBezelStyle, 2)

        self.assertEqual(AppKit.NSGradientNone, 0)
        self.assertEqual(AppKit.NSGradientConcaveWeak, 1)
        self.assertEqual(AppKit.NSGradientConcaveStrong, 2)
        self.assertEqual(AppKit.NSGradientConvexWeak, 3)
        self.assertEqual(AppKit.NSGradientConvexStrong, 4)

        self.assertEqual(AppKit.NSButtonTypeMomentaryLight, 0)
        self.assertEqual(AppKit.NSButtonTypePushOnPushOff, 1)
        self.assertEqual(AppKit.NSButtonTypeToggle, 2)
        self.assertEqual(AppKit.NSButtonTypeSwitch, 3)
        self.assertEqual(AppKit.NSButtonTypeRadio, 4)
        self.assertEqual(AppKit.NSButtonTypeMomentaryChange, 5)
        self.assertEqual(AppKit.NSButtonTypeOnOff, 6)
        self.assertEqual(AppKit.NSButtonTypeMomentaryPushIn, 7)
        self.assertEqual(AppKit.NSButtonTypeAccelerator, 8)
        self.assertEqual(AppKit.NSButtonTypeMultiLevelAccelerator, 9)

        self.assertEqual(AppKit.NSBezelStyleRounded, 1)
        self.assertEqual(AppKit.NSBezelStyleRegularSquare, 2)
        self.assertEqual(AppKit.NSBezelStyleDisclosure, 5)
        self.assertEqual(AppKit.NSBezelStyleShadowlessSquare, 6)
        self.assertEqual(AppKit.NSBezelStyleCircular, 7)
        self.assertEqual(AppKit.NSBezelStyleTexturedSquare, 8)
        self.assertEqual(AppKit.NSBezelStyleHelpButton, 9)
        self.assertEqual(AppKit.NSBezelStyleSmallSquare, 10)
        self.assertEqual(AppKit.NSBezelStyleTexturedRounded, 11)
        self.assertEqual(AppKit.NSBezelStyleRoundRect, 12)
        self.assertEqual(AppKit.NSBezelStyleRecessed, 13)
        self.assertEqual(AppKit.NSBezelStyleRoundedDisclosure, 14)
        self.assertEqual(AppKit.NSBezelStyleInline, 15)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSInlineBezelStyle, 15)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSButtonCell.isOpaque)
        self.assertResultIsBOOL(AppKit.NSButtonCell.isTransparent)
        self.assertArgIsBOOL(AppKit.NSButtonCell.setTransparent_, 0)

        self.assertArgIsOut(AppKit.NSButtonCell.getPeriodicDelay_interval_, 0)
        self.assertArgIsOut(AppKit.NSButtonCell.getPeriodicDelay_interval_, 1)

        self.assertResultIsBOOL(AppKit.NSButtonCell.imageDimsWhenDisabled)
        self.assertArgIsBOOL(AppKit.NSButtonCell.setImageDimsWhenDisabled_, 0)
        self.assertResultIsBOOL(AppKit.NSButtonCell.showsBorderOnlyWhileMouseInside)
        self.assertArgIsBOOL(AppKit.NSButtonCell.setShowsBorderOnlyWhileMouseInside_, 0)
