
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedControl (TestCase):
    def testConstants(self):
        self.assertEqual(NSSegmentStyleAutomatic, 0)
        self.assertEqual(NSSegmentStyleRounded, 1)
        self.assertEqual(NSSegmentStyleTexturedRounded, 2)
        self.assertEqual(NSSegmentStyleRoundRect, 3)
        self.assertEqual(NSSegmentStyleTexturedSquare, 4)
        self.assertEqual(NSSegmentStyleCapsule, 5)
        self.assertEqual(NSSegmentStyleSmallSquare, 6)
        self.assertEqual(NSSegmentStyleSeparated, 8)

        self.assertEqual(NSSegmentSwitchTrackingSelectOne, 0)
        self.assertEqual(NSSegmentSwitchTrackingSelectAny, 1)
        self.assertEqual(NSSegmentSwitchTrackingMomentary, 2)
        self.assertEqual(NSSegmentSwitchTrackingMomentaryAccelerator, 3)

        self.assertEqual(NSSegmentDistributionFit, 0)
        self.assertEqual(NSSegmentDistributionFill, 1)
        self.assertEqual(NSSegmentDistributionFillEqually, 2)
        self.assertEqual(NSSegmentDistributionFillProportionally, 3)

    def testMethods(self):
        self.assertResultIsBOOL(NSSegmentedControl.selectSegmentWithTag_)
        self.assertArgIsBOOL(NSSegmentedControl.setSelected_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedControl.isSelectedForSegment_)
        self.assertArgIsBOOL(NSSegmentedControl.setEnabled_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedControl.isEnabledForSegment_)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSSegmentedControl.isSpringLoaded)
        self.assertArgIsBOOL(NSSegmentedControl.setSpringLoaded_, 0)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertArgIsSEL(NSSegmentedControl.segmentedControlWithLabels_trackingMode_target_action_, 3, b'v@:@')
        self.assertArgIsSEL(NSSegmentedControl.segmentedControlWithImages_trackingMode_target_action_, 3, b'v@:@')

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBOOL(NSSegmentedControl.setShowsMenuIndicator_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedControl.showsMenuIndicatorForSegment_)

if __name__ == "__main__":
    main()
