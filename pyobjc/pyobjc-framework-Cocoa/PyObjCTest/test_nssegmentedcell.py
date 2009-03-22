
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSegmentSwitchTrackingSelectOne, 0)
        self.failUnlessEqual(NSSegmentSwitchTrackingSelectAny, 1)
        self.failUnlessEqual(NSSegmentSwitchTrackingMomentary, 2)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSegmentedCell.selectSegmentWithTag_)
        self.failUnlessResultIsBOOL(NSSegmentedCell.isSelectedForSegment_)
        self.failUnlessArgIsBOOL(NSSegmentedCell.setSelected_forSegment_, 0)
        self.failUnlessResultIsBOOL(NSSegmentedCell.isEnabledForSegment_)
        self.failUnlessArgIsBOOL(NSSegmentedCell.setEnabled_forSegment_, 0)


if __name__ == "__main__":
    main()
