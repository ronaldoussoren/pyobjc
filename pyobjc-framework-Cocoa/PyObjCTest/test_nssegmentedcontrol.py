import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSegmentedControl(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSSegmentStyleAutomatic, 0)
        self.assertEqual(AppKit.NSSegmentStyleRounded, 1)
        self.assertEqual(AppKit.NSSegmentStyleTexturedRounded, 2)
        self.assertEqual(AppKit.NSSegmentStyleRoundRect, 3)
        self.assertEqual(AppKit.NSSegmentStyleTexturedSquare, 4)
        self.assertEqual(AppKit.NSSegmentStyleCapsule, 5)
        self.assertEqual(AppKit.NSSegmentStyleSmallSquare, 6)
        self.assertEqual(AppKit.NSSegmentStyleSeparated, 8)

        self.assertEqual(AppKit.NSSegmentSwitchTrackingSelectOne, 0)
        self.assertEqual(AppKit.NSSegmentSwitchTrackingSelectAny, 1)
        self.assertEqual(AppKit.NSSegmentSwitchTrackingMomentary, 2)
        self.assertEqual(AppKit.NSSegmentSwitchTrackingMomentaryAccelerator, 3)

        self.assertEqual(AppKit.NSSegmentDistributionFit, 0)
        self.assertEqual(AppKit.NSSegmentDistributionFill, 1)
        self.assertEqual(AppKit.NSSegmentDistributionFillEqually, 2)
        self.assertEqual(AppKit.NSSegmentDistributionFillProportionally, 3)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSegmentedControl.selectSegmentWithTag_)
        self.assertArgIsBOOL(AppKit.NSSegmentedControl.setSelected_forSegment_, 0)
        self.assertResultIsBOOL(AppKit.NSSegmentedControl.isSelectedForSegment_)
        self.assertArgIsBOOL(AppKit.NSSegmentedControl.setEnabled_forSegment_, 0)
        self.assertResultIsBOOL(AppKit.NSSegmentedControl.isEnabledForSegment_)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSSegmentedControl.isSpringLoaded)
        self.assertArgIsBOOL(AppKit.NSSegmentedControl.setSpringLoaded_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsSEL(
            AppKit.NSSegmentedControl.segmentedControlWithLabels_trackingMode_target_action_,
            3,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSSegmentedControl.segmentedControlWithImages_trackingMode_target_action_,
            3,
            b"v@:@",
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBOOL(
            AppKit.NSSegmentedControl.setShowsMenuIndicator_forSegment_, 0
        )
        self.assertResultIsBOOL(AppKit.NSSegmentedControl.showsMenuIndicatorForSegment_)
