import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextTable(TestCase):

    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTextBlockValueType)
        self.assertEqual(AppKit.NSTextBlockValueTypeAbsolute, 0)
        self.assertEqual(AppKit.NSTextBlockValueTypePercentage, 1)
        self.assertEqual(
            AppKit.NSTextBlockAbsoluteValueType, AppKit.NSTextBlockValueTypeAbsolute
        )
        self.assertEqual(
            AppKit.NSTextBlockPercentageValueType, AppKit.NSTextBlockValueTypePercentage
        )

        self.assertIsEnumType(AppKit.NSTextBlockDimension)
        self.assertEqual(AppKit.NSTextBlockDimensionWidth, 0)
        self.assertEqual(AppKit.NSTextBlockDimensionMinimumWidth, 1)
        self.assertEqual(AppKit.NSTextBlockDimensionMaximumWidth, 2)
        self.assertEqual(AppKit.NSTextBlockDimensionHeight, 4)
        self.assertEqual(AppKit.NSTextBlockDimensionMinimumHeight, 5)
        self.assertEqual(AppKit.NSTextBlockDimensionMaximumHeight, 6)
        self.assertEqual(AppKit.NSTextBlockWidth, AppKit.NSTextBlockDimensionWidth)
        self.assertEqual(
            AppKit.NSTextBlockMinimumWidth, AppKit.NSTextBlockDimensionMinimumWidth
        )
        self.assertEqual(
            AppKit.NSTextBlockMaximumWidth, AppKit.NSTextBlockDimensionMaximumWidth
        )
        self.assertEqual(AppKit.NSTextBlockHeight, AppKit.NSTextBlockDimensionHeight)
        self.assertEqual(
            AppKit.NSTextBlockMinimumHeight, AppKit.NSTextBlockDimensionMinimumHeight
        )
        self.assertEqual(
            AppKit.NSTextBlockMaximumHeight, AppKit.NSTextBlockDimensionMaximumHeight
        )

        self.assertIsEnumType(AppKit.NSTextBlockLayer)
        self.assertEqual(AppKit.NSTextBlockLayerPadding, -1)
        self.assertEqual(AppKit.NSTextBlockLayerBorder, 0)
        self.assertEqual(AppKit.NSTextBlockLayerMargin, 1)
        self.assertEqual(AppKit.NSTextBlockPadding, AppKit.NSTextBlockLayerPadding)
        self.assertEqual(AppKit.NSTextBlockBorder, AppKit.NSTextBlockLayerBorder)
        self.assertEqual(AppKit.NSTextBlockMargin, AppKit.NSTextBlockLayerMargin)

        self.assertIsEnumType(AppKit.NSTextBlockVerticalAlignment)
        self.assertEqual(AppKit.NSTextBlockVerticalAlignmentTop, 0)
        self.assertEqual(AppKit.NSTextBlockVerticalAlignmentMiddle, 1)
        self.assertEqual(AppKit.NSTextBlockVerticalAlignmentBottom, 2)
        self.assertEqual(AppKit.NSTextBlockVerticalAlignmentBaseline, 3)
        self.assertEqual(
            AppKit.NSTextBlockTopAlignment, AppKit.NSTextBlockVerticalAlignmentTop
        )
        self.assertEqual(
            AppKit.NSTextBlockMiddleAlignment, AppKit.NSTextBlockVerticalAlignmentMiddle
        )
        self.assertEqual(
            AppKit.NSTextBlockBottomAlignment, AppKit.NSTextBlockVerticalAlignmentBottom
        )
        self.assertEqual(
            AppKit.NSTextBlockBaselineAlignment,
            AppKit.NSTextBlockVerticalAlignmentBaseline,
        )

        self.assertIsEnumType(AppKit.NSTextTableLayoutAlgorithm)
        self.assertEqual(AppKit.NSTextTableLayoutAlgorithmAutomatic, 0)
        self.assertEqual(AppKit.NSTextTableLayoutAlgorithmFixed, 1)
        self.assertEqual(
            AppKit.NSTextTableAutomaticLayoutAlgorithm,
            AppKit.NSTextTableLayoutAlgorithmAutomatic,
        )
        self.assertEqual(
            AppKit.NSTextTableFixedLayoutAlgorithm,
            AppKit.NSTextTableLayoutAlgorithmFixed,
        )

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTextTable.collapsesBorders)
        self.assertArgIsBOOL(AppKit.NSTextTable.setCollapsesBorders_, 0)
        self.assertResultIsBOOL(AppKit.NSTextTable.hidesEmptyCells)
        self.assertArgIsBOOL(AppKit.NSTextTable.setHidesEmptyCells_, 0)
