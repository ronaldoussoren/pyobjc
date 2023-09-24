import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextInsertionIndicator(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSTextInsertionIndicatorDisplayMode)
        self.assertEqual(AppKit.NSTextInsertionIndicatorDisplayModeAutomatic, 0)
        self.assertEqual(AppKit.NSTextInsertionIndicatorDisplayModeHidden, 1)
        self.assertEqual(AppKit.NSTextInsertionIndicatorDisplayModeVisible, 2)

        self.assertIsEnumType(AppKit.NSTextInsertionIndicatorAutomaticModeOptions)
        self.assertEqual(
            AppKit.NSTextInsertionIndicatorAutomaticModeOptionsShowEffectsView, 1 << 0
        )
        self.assertEqual(
            AppKit.NSTextInsertionIndicatorAutomaticModeOptionsShowWhileTracking, 1 << 1
        )

    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBlock(
            AppKit.NSTextInsertionIndicator.effectsViewInserter, b"v@"
        )
        self.assertArgIsBlock(
            AppKit.NSTextInsertionIndicator.setEffectsViewInserter_, 0, b"v@"
        )
