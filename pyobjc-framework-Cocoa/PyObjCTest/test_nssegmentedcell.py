import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSSegmentedCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSSegmentSwitchTrackingSelectOne, 0)
        self.assertEqual(AppKit.NSSegmentSwitchTrackingSelectAny, 1)
        self.assertEqual(AppKit.NSSegmentSwitchTrackingMomentary, 2)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSegmentedCell.selectSegmentWithTag_)
        self.assertResultIsBOOL(AppKit.NSSegmentedCell.isSelectedForSegment_)
        self.assertArgIsBOOL(AppKit.NSSegmentedCell.setSelected_forSegment_, 0)
        self.assertResultIsBOOL(AppKit.NSSegmentedCell.isEnabledForSegment_)
        self.assertArgIsBOOL(AppKit.NSSegmentedCell.setEnabled_forSegment_, 0)
