
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSliderCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSTickMarkBelow, 0)
        self.assertEqual(NSTickMarkAbove, 1)
        self.assertEqual(NSTickMarkLeft, NSTickMarkAbove)
        self.assertEqual(NSTickMarkRight, NSTickMarkBelow)

        self.assertEqual(NSLinearSlider, 0)
        self.assertEqual(NSCircularSlider, 1)

        self.assertEqual(NSTickMarkPositionBelow, 0)
        self.assertEqual(NSTickMarkPositionAbove, 1)
        self.assertEqual(NSTickMarkPositionLeading, NSTickMarkPositionAbove)
        self.assertEqual(NSTickMarkPositionTrailing, NSTickMarkPositionBelow)

        self.assertEqual(NSSliderTypeLinear, 0)
        self.assertEqual(NSSliderTypeCircular, 1)



    def testMethods(self):
        self.assertResultIsBOOL(NSSliderCell.prefersTrackingUntilMouseUp)
        self.assertArgIsBOOL(NSSliderCell.knobRectFlipped_, 0)
        self.assertArgIsBOOL(NSSliderCell.drawBarInside_flipped_, 1)
        self.assertResultIsBOOL(NSSliderCell.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(NSSliderCell.setAllowsTickMarkValuesOnly_, 0)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBOOL(NSSliderCell.barRectFlipped_, 0)

if __name__ == "__main__":
    main()
