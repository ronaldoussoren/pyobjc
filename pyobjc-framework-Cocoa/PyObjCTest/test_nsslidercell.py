import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSliderCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTickMarkBelow, 0)
        self.assertEqual(AppKit.NSTickMarkAbove, 1)
        self.assertEqual(AppKit.NSTickMarkLeft, AppKit.NSTickMarkAbove)
        self.assertEqual(AppKit.NSTickMarkRight, AppKit.NSTickMarkBelow)

        self.assertEqual(AppKit.NSLinearSlider, 0)
        self.assertEqual(AppKit.NSCircularSlider, 1)

        self.assertEqual(AppKit.NSTickMarkPositionBelow, 0)
        self.assertEqual(AppKit.NSTickMarkPositionAbove, 1)
        self.assertEqual(
            AppKit.NSTickMarkPositionLeading, AppKit.NSTickMarkPositionAbove
        )
        self.assertEqual(
            AppKit.NSTickMarkPositionTrailing, AppKit.NSTickMarkPositionBelow
        )

        self.assertEqual(AppKit.NSSliderTypeLinear, 0)
        self.assertEqual(AppKit.NSSliderTypeCircular, 1)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSliderCell.prefersTrackingUntilMouseUp)
        self.assertArgIsBOOL(AppKit.NSSliderCell.knobRectFlipped_, 0)
        self.assertArgIsBOOL(AppKit.NSSliderCell.drawBarInside_flipped_, 1)
        self.assertResultIsBOOL(AppKit.NSSliderCell.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(AppKit.NSSliderCell.setAllowsTickMarkValuesOnly_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBOOL(AppKit.NSSliderCell.barRectFlipped_, 0)
