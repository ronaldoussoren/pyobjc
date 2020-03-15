import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSProgressIndicator(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSProgressIndicatorPreferredThickness, 14)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredSmallThickness, 10)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredLargeThickness, 18)
        self.assertEqual(AppKit.NSProgressIndicatorPreferredAquaThickness, 12)

        self.assertEqual(AppKit.NSProgressIndicatorBarStyle, 0)
        self.assertEqual(AppKit.NSProgressIndicatorSpinningStyle, 1)

        self.assertEqual(AppKit.NSProgressIndicatorStyleBar, 0)
        self.assertEqual(AppKit.NSProgressIndicatorStyleSpinning, 1)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isIndeterminate)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setIndeterminate_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isBezeled)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setBezeled_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.usesThreadedAnimation)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setUsesThreadedAnimation_, 0)
        self.assertResultIsBOOL(AppKit.NSProgressIndicator.isDisplayedWhenStopped)
        self.assertArgIsBOOL(AppKit.NSProgressIndicator.setDisplayedWhenStopped_, 0)
