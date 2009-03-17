
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSButtonCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSMomentaryLightButton, 0)
        self.failUnlessEqual(NSPushOnPushOffButton, 1)
        self.failUnlessEqual(NSToggleButton, 2)
        self.failUnlessEqual(NSSwitchButton, 3)
        self.failUnlessEqual(NSRadioButton, 4)
        self.failUnlessEqual(NSMomentaryChangeButton, 5)
        self.failUnlessEqual(NSOnOffButton, 6)
        self.failUnlessEqual(NSMomentaryPushInButton, 7)
        self.failUnlessEqual(NSMomentaryPushButton, 0)
        self.failUnlessEqual(NSMomentaryLight, 7)
        self.failUnlessEqual(NSRoundedBezelStyle, 1)
        self.failUnlessEqual(NSRegularSquareBezelStyle, 2)
        self.failUnlessEqual(NSThickSquareBezelStyle, 3)
        self.failUnlessEqual(NSThickerSquareBezelStyle, 4)
        self.failUnlessEqual(NSDisclosureBezelStyle, 5)
        self.failUnlessEqual(NSShadowlessSquareBezelStyle, 6)
        self.failUnlessEqual(NSCircularBezelStyle, 7)
        self.failUnlessEqual(NSTexturedSquareBezelStyle, 8)
        self.failUnlessEqual(NSHelpButtonBezelStyle, 9)
        self.failUnlessEqual(NSSmallSquareBezelStyle, 10)
        self.failUnlessEqual(NSTexturedRoundedBezelStyle, 11)
        self.failUnlessEqual(NSRoundRectBezelStyle, 12)
        self.failUnlessEqual(NSRecessedBezelStyle, 13)
        self.failUnlessEqual(NSRoundedDisclosureBezelStyle, 14)
        self.failUnlessEqual(NSSmallIconButtonBezelStyle, 2)

        self.failUnlessEqual(NSGradientNone, 0)
        self.failUnlessEqual(NSGradientConcaveWeak, 1)
        self.failUnlessEqual(NSGradientConcaveStrong, 2)
        self.failUnlessEqual(NSGradientConvexWeak, 3)
        self.failUnlessEqual(NSGradientConvexStrong, 4)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSButtonCell.isOpaque)
        self.failUnlessResultIsBOOL(NSButtonCell.isTransparent)
        self.failUnlessArgIsBOOL(NSButtonCell.setTransparent_, 0)

        self.failUnlessArgIsOut(NSButtonCell.getPeriodicDelay_interval_, 0)
        self.failUnlessArgIsOut(NSButtonCell.getPeriodicDelay_interval_, 1)

        self.failUnlessResultIsBOOL(NSButtonCell.imageDimsWhenDisabled)
        self.failUnlessArgIsBOOL(NSButtonCell.setImageDimsWhenDisabled_, 0)
        self.failUnlessResultIsBOOL(NSButtonCell.showsBorderOnlyWhileMouseInside)
        self.failUnlessArgIsBOOL(NSButtonCell.setShowsBorderOnlyWhileMouseInside_, 0)
if __name__ == "__main__":
    main()
