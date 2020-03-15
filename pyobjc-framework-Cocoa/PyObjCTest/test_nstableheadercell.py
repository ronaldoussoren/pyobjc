import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableHeaderCell(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            AppKit.NSTableHeaderCell.drawSortIndicatorWithFrame_inView_ascending_priority_,
            2,
        )

        self.assertResultHasType(
            AppKit.NSTableHeaderCell.sortIndicatorRectForBounds_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTableHeaderCell.sortIndicatorRectForBounds_,
            0,
            AppKit.NSRect.__typestr__,
        )
