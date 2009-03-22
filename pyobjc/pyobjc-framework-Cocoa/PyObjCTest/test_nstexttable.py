
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextTable (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextBlockAbsoluteValueType, 0)
        self.failUnlessEqual(NSTextBlockPercentageValueType, 1)
        self.failUnlessEqual(NSTextBlockWidth, 0)
        self.failUnlessEqual(NSTextBlockMinimumWidth, 1)
        self.failUnlessEqual(NSTextBlockMaximumWidth, 2)
        self.failUnlessEqual(NSTextBlockHeight, 4)
        self.failUnlessEqual(NSTextBlockMinimumHeight, 5)
        self.failUnlessEqual(NSTextBlockMaximumHeight, 6)
        self.failUnlessEqual(NSTextBlockPadding, -1)
        self.failUnlessEqual(NSTextBlockBorder,  0)
        self.failUnlessEqual(NSTextBlockMargin,  1)
        self.failUnlessEqual(NSTextBlockTopAlignment, 0)
        self.failUnlessEqual(NSTextBlockMiddleAlignment, 1)
        self.failUnlessEqual(NSTextBlockBottomAlignment, 2)
        self.failUnlessEqual(NSTextBlockBaselineAlignment, 3)
        self.failUnlessEqual(NSTextTableAutomaticLayoutAlgorithm, 0)
        self.failUnlessEqual(NSTextTableFixedLayoutAlgorithm, 1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextTable.collapsesBorders)
        self.failUnlessArgIsBOOL(NSTextTable.setCollapsesBorders_, 0)
        self.failUnlessResultIsBOOL(NSTextTable.hidesEmptyCells)
        self.failUnlessArgIsBOOL(NSTextTable.setHidesEmptyCells_, 0)


if __name__ == "__main__":
    main()
