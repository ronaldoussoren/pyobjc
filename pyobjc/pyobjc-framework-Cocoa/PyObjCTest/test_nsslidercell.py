
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSliderCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTickMarkBelow, 0)
        self.failUnlessEqual(NSTickMarkAbove, 1)
        self.failUnlessEqual(NSTickMarkLeft, NSTickMarkAbove)
        self.failUnlessEqual(NSTickMarkRight, NSTickMarkBelow)
        self.failUnlessEqual(NSLinearSlider, 0)
        self.failUnlessEqual(NSCircularSlider, 1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSliderCell.prefersTrackingUntilMouseUp)
        self.failUnlessArgIsBOOL(NSSliderCell.knobRectFlipped_, 0)
        self.failUnlessArgIsBOOL(NSSliderCell.drawBarInside_flipped_, 1)
        self.failUnlessResultIsBOOL(NSSliderCell.allowsTickMarkValuesOnly)
        self.failUnlessArgIsBOOL(NSSliderCell.setAllowsTickMarkValuesOnly_, 0)

if __name__ == "__main__":
    main()
