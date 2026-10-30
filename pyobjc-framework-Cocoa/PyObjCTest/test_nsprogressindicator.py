import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSProgressIndicator(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSProgressIndicatorStyle)
        self.assertEqual(AppKit.NSProgressIndicatorStyleBar, 0)
        self.assertEqual(AppKit.NSProgressIndicatorStyleSpinning, 1)

        # Old aliases:
        self.assertEqual(AppKit.NSProgressIndicatorBarStyle, 0)
        self.assertEqual(AppKit.NSProgressIndicatorSpinningStyle, 1)

        self.assertIsEnumType(AppKit.NSProgressIndicatorThickness)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredThickness, 14)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredSmallThickness, 10)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredLargeThickness, 18)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredAquaThickness, 12)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isIndeterminate)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setIndeterminate_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isBezeled)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setBezeled_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.usesThreadedAnimation)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setUsesThreadedAnimation_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isDisplayedWhenStopped)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setDisplayedWhenStopped_, 0)
