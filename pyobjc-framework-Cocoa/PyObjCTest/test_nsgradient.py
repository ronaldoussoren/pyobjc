import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSGradient(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSGradientDrawingOptions)

    def test_constants(self):
        self.assertEqual(AppKit.NSGradientDrawsBeforeStartingLocation, (1 << 0))
        self.assertEqual(AppKit.NSGradientDrawsAfterEndingLocation, (1 << 1))

    def test_methods(self):
        self.assertArgSizeInArg(
            AppKit.NSGradient.initWithColors_atLocations_colorSpace_, 1, 0
        )
        self.assertArgIsIn(AppKit.NSGradient.initWithColors_atLocations_colorSpace_, 1)

        self.assertArgIsOut(AppKit.NSGradient.getColor_location_atIndex_, 0)
        self.assertArgIsOut(AppKit.NSGradient.getColor_location_atIndex_, 1)
