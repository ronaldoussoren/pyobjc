from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation
from AppKit import *


class TestNSGridView (TestCase):
    def testConstants(self):
        self.assertEqual(NSGridCellPlacementInherited, 0)
        self.assertEqual(NSGridCellPlacementNone, 1)
        self.assertEqual(NSGridCellPlacementLeading, 2)
        self.assertEqual(NSGridCellPlacementTop, 2)
        self.assertEqual(NSGridCellPlacementTrailing, 3)
        self.assertEqual(NSGridCellPlacementBottom, 3)
        self.assertEqual(NSGridCellPlacementCenter, 4)
        self.assertEqual(NSGridCellPlacementFill, 5)

        self.assertEqual(NSGridRowAlignmentInherited, 0)
        self.assertEqual(NSGridRowAlignmentNone, 1)
        self.assertEqual(NSGridRowAlignmentFirstBaseline, 2)
        self.assertEqual(NSGridRowAlignmentLastBaseline, 3)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSGridViewSizeForContent, float)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSGridRow.isHidden)
        self.assertArgIsBOOL(NSGridRow.setHidden_, 0)

        self.assertResultIsBOOL(NSGridColumn.isHidden)
        self.assertArgIsBOOL(NSGridColumn.setHidden_, 0)


if __name__ == "__main__":
    main()
