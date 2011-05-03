
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSSegmentSwitchTrackingSelectOne, 0)
        self.assertEqual(NSSegmentSwitchTrackingSelectAny, 1)
        self.assertEqual(NSSegmentSwitchTrackingMomentary, 2)

    def testMethods(self):
        self.assertResultIsBOOL(NSSegmentedCell.selectSegmentWithTag_)
        self.assertResultIsBOOL(NSSegmentedCell.isSelectedForSegment_)
        self.assertArgIsBOOL(NSSegmentedCell.setSelected_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedCell.isEnabledForSegment_)
        self.assertArgIsBOOL(NSSegmentedCell.setEnabled_forSegment_, 0)


if __name__ == "__main__":
    main()
