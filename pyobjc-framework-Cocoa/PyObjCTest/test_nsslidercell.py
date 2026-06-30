import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSSliderCell(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSSliderType)
        self.assertEqual(AppKit.NSSliderTypeLinear, 0)
        self.assertEqual(AppKit.NSSliderTypeCircular, 1)

        # Old aliases:
        self.assertEqual(AppKit.NSLinearSlider, 0)
        self.assertEqual(AppKit.NSCircularSlider, 1)

        self.assertIsEnumType(AppKit.NSTickMarkPosition)
        self.assertEqual(AppKit.NSTickMarkPositionBelow, 0)
        self.assertEqual(AppKit.NSTickMarkPositionAbove, 1)
        self.assertEqual(
            AppKit.NSTickMarkPositionLeading, AppKit.NSTickMarkPositionAbove
        )
        self.assertEqual(
            AppKit.NSTickMarkPositionTrailing, AppKit.NSTickMarkPositionBelow
        )

        # Old aliases:
        self.assertEqual(AppKit.NSTickMarkBelow, 0)
        self.assertEqual(AppKit.NSTickMarkAbove, 1)
        self.assertEqual(AppKit.NSTickMarkLeft, AppKit.NSTickMarkAbove)
        self.assertEqual(AppKit.NSTickMarkRight, AppKit.NSTickMarkBelow)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSSliderCell.prefersTrackingUntilMouseUp)
        self.assertArgIsBOOL(AppKit.NSSliderCell.knobRectFlipped_, 0)
        self.assertArgIsBOOL(AppKit.NSSliderCell.drawBarInside_flipped_, 1)
        self.assertResultIsBOOL(AppKit.NSSliderCell.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(AppKit.NSSliderCell.setAllowsTickMarkValuesOnly_, 0)

        self.assertArgIsBOOL(AppKit.NSSliderCell.barRectFlipped_, 0)
