import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSGridView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSGridCellPlacement)
        self.assertIsEnumType(AppKit.NSGridRowAlignment)

    def testConstants(self):
        self.assertEqual(AppKit.NSGridCellPlacementInherited, 0)
        self.assertEqual(AppKit.NSGridCellPlacementNone, 1)
        self.assertEqual(AppKit.NSGridCellPlacementLeading, 2)
        self.assertEqual(AppKit.NSGridCellPlacementTop, 2)
        self.assertEqual(AppKit.NSGridCellPlacementTrailing, 3)
        self.assertEqual(AppKit.NSGridCellPlacementBottom, 3)
        self.assertEqual(AppKit.NSGridCellPlacementCenter, 4)
        self.assertEqual(AppKit.NSGridCellPlacementFill, 5)

        self.assertEqual(AppKit.NSGridRowAlignmentInherited, 0)
        self.assertEqual(AppKit.NSGridRowAlignmentNone, 1)
        self.assertEqual(AppKit.NSGridRowAlignmentFirstBaseline, 2)
        self.assertEqual(AppKit.NSGridRowAlignmentLastBaseline, 3)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSGridViewSizeForContent, float)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSGridRow.isHidden)
        self.assertArgIsBOOL(AppKit.NSGridRow.setHidden_, 0)

        self.assertResultIsBOOL(AppKit.NSGridColumn.isHidden)
        self.assertArgIsBOOL(AppKit.NSGridColumn.setHidden_, 0)
