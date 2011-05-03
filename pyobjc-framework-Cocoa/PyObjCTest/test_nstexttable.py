
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextTable (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextBlockAbsoluteValueType, 0)
        self.assertEqual(NSTextBlockPercentageValueType, 1)
        self.assertEqual(NSTextBlockWidth, 0)
        self.assertEqual(NSTextBlockMinimumWidth, 1)
        self.assertEqual(NSTextBlockMaximumWidth, 2)
        self.assertEqual(NSTextBlockHeight, 4)
        self.assertEqual(NSTextBlockMinimumHeight, 5)
        self.assertEqual(NSTextBlockMaximumHeight, 6)
        self.assertEqual(NSTextBlockPadding, -1)
        self.assertEqual(NSTextBlockBorder,  0)
        self.assertEqual(NSTextBlockMargin,  1)
        self.assertEqual(NSTextBlockTopAlignment, 0)
        self.assertEqual(NSTextBlockMiddleAlignment, 1)
        self.assertEqual(NSTextBlockBottomAlignment, 2)
        self.assertEqual(NSTextBlockBaselineAlignment, 3)
        self.assertEqual(NSTextTableAutomaticLayoutAlgorithm, 0)
        self.assertEqual(NSTextTableFixedLayoutAlgorithm, 1)

    def testMethods(self):
        self.assertResultIsBOOL(NSTextTable.collapsesBorders)
        self.assertArgIsBOOL(NSTextTable.setCollapsesBorders_, 0)
        self.assertResultIsBOOL(NSTextTable.hidesEmptyCells)
        self.assertArgIsBOOL(NSTextTable.setHidesEmptyCells_, 0)


if __name__ == "__main__":
    main()
