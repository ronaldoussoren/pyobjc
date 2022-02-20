import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextTable(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextBlockDimension)
        self.assertIsEnumType(AppKit.NSTextBlockLayer)
        self.assertIsEnumType(AppKit.NSTextBlockValueType)
        self.assertIsEnumType(AppKit.NSTextBlockVerticalAlignment)
        self.assertIsEnumType(AppKit.NSTextTableLayoutAlgorithm)

    def testConstants(self):
        self.assertEqual(AppKit.NSTextBlockAbsoluteValueType, 0)
        self.assertEqual(AppKit.NSTextBlockPercentageValueType, 1)

        self.assertEqual(AppKit.NSTextBlockWidth, 0)
        self.assertEqual(AppKit.NSTextBlockMinimumWidth, 1)
        self.assertEqual(AppKit.NSTextBlockMaximumWidth, 2)
        self.assertEqual(AppKit.NSTextBlockHeight, 4)
        self.assertEqual(AppKit.NSTextBlockMinimumHeight, 5)
        self.assertEqual(AppKit.NSTextBlockMaximumHeight, 6)

        self.assertEqual(AppKit.NSTextBlockPadding, -1)
        self.assertEqual(AppKit.NSTextBlockBorder, 0)
        self.assertEqual(AppKit.NSTextBlockMargin, 1)

        self.assertEqual(AppKit.NSTextBlockTopAlignment, 0)
        self.assertEqual(AppKit.NSTextBlockMiddleAlignment, 1)
        self.assertEqual(AppKit.NSTextBlockBottomAlignment, 2)
        self.assertEqual(AppKit.NSTextBlockBaselineAlignment, 3)

        self.assertEqual(AppKit.NSTextTableAutomaticLayoutAlgorithm, 0)
        self.assertEqual(AppKit.NSTextTableFixedLayoutAlgorithm, 1)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextTable.collapsesBorders)
        self.assertArgIsBOOL(AppKit.NSTextTable.setCollapsesBorders_, 0)
        self.assertResultIsBOOL(AppKit.NSTextTable.hidesEmptyCells)
        self.assertArgIsBOOL(AppKit.NSTextTable.setHidesEmptyCells_, 0)
