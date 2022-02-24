import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLayoutContraintManual(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSLayoutPriority, float)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSLayoutAttribute)
        self.assertIsEnumType(AppKit.NSLayoutConstraintOrientation)
        self.assertIsEnumType(AppKit.NSLayoutFormatOptions)
        self.assertIsEnumType(AppKit.NSLayoutRelation)

    def testNSDictionaryOfVariableBindings(self):
        var1 = "foo"  # noqa: F841
        var2 = "bar"  # noqa: F841

        self.assertEqual(
            AppKit.NSDictionaryOfVariableBindings("var1", "var2"),
            {"var1": "foo", "var2": "bar"},
        )

        self.assertRaises(
            KeyError, AppKit.NSDictionaryOfVariableBindings, "var1", "var3"
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSViewNoIntrinsicMetric, float)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSViewNoInstrinsicMetric, float)

        self.assertEqual(AppKit.NSLayoutRelationLessThanOrEqual, -1)
        self.assertEqual(AppKit.NSLayoutRelationEqual, 0)
        self.assertEqual(AppKit.NSLayoutRelationGreaterThanOrEqual, 1)

        self.assertEqual(AppKit.NSLayoutAttributeLeft, 1)
        self.assertEqual(AppKit.NSLayoutAttributeRight, 2)
        self.assertEqual(AppKit.NSLayoutAttributeTop, 3)
        self.assertEqual(AppKit.NSLayoutAttributeBottom, 4)
        self.assertEqual(AppKit.NSLayoutAttributeLeading, 5)
        self.assertEqual(AppKit.NSLayoutAttributeTrailing, 6)
        self.assertEqual(AppKit.NSLayoutAttributeWidth, 7)
        self.assertEqual(AppKit.NSLayoutAttributeHeight, 8)
        self.assertEqual(AppKit.NSLayoutAttributeCenterX, 9)
        self.assertEqual(AppKit.NSLayoutAttributeCenterY, 10)
        self.assertEqual(AppKit.NSLayoutAttributeBaseline, 11)
        self.assertEqual(
            AppKit.NSLayoutAttributeLastBaseline, AppKit.NSLayoutAttributeBaseline
        )
        self.assertEqual(AppKit.NSLayoutAttributeFirstBaseline, 12)
        self.assertEqual(AppKit.NSLayoutAttributeNotAnAttribute, 0)

        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllLeft, (1 << AppKit.NSLayoutAttributeLeft)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllRight, (1 << AppKit.NSLayoutAttributeRight)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllTop, (1 << AppKit.NSLayoutAttributeTop)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllBottom, (1 << AppKit.NSLayoutAttributeBottom)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllLeading, (1 << AppKit.NSLayoutAttributeLeading)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllTrailing,
            (1 << AppKit.NSLayoutAttributeTrailing),
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllCenterX, (1 << AppKit.NSLayoutAttributeCenterX)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllCenterY, (1 << AppKit.NSLayoutAttributeCenterY)
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllBaseline,
            (1 << AppKit.NSLayoutAttributeBaseline),
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllLastBaseline,
            (1 << AppKit.NSLayoutAttributeBaseline),
        )
        self.assertEqual(
            AppKit.NSLayoutFormatAlignAllFirstBaseline,
            (1 << AppKit.NSLayoutAttributeFirstBaseline),
        )

        self.assertEqual(AppKit.NSLayoutFormatAlignmentMask, 0xFFFF)

        self.assertEqual(AppKit.NSLayoutFormatDirectionLeadingToTrailing, 0 << 16)
        self.assertEqual(AppKit.NSLayoutFormatDirectionLeftToRight, 1 << 16)
        self.assertEqual(AppKit.NSLayoutFormatDirectionRightToLeft, 2 << 16)

        self.assertEqual(AppKit.NSLayoutFormatDirectionMask, 0x3 << 16)

        self.assertEqual(AppKit.NSLayoutConstraintOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSLayoutConstraintOrientationVertical, 1)

        self.assertEqual(AppKit.NSLayoutPriorityRequired, 1000)
        self.assertEqual(AppKit.NSLayoutPriorityDefaultHigh, 750)
        self.assertEqual(AppKit.NSLayoutPriorityDragThatCanResizeWindow, 510)
        self.assertEqual(AppKit.NSLayoutPriorityWindowSizeStayPut, 500)
        self.assertEqual(AppKit.NSLayoutPriorityDragThatCannotResizeWindow, 490)
        self.assertEqual(AppKit.NSLayoutPriorityDefaultLow, 250)
        self.assertEqual(AppKit.NSLayoutPriorityFittingSizeCompression, 50)

    @min_os_level("10.7")
    def testRecords10_7(self):
        v = AppKit.NSEdgeInsets()
        self.assertEqual(v.top, 0.0)
        self.assertEqual(v.left, 0.0)
        self.assertEqual(v.bottom, 0.0)
        self.assertEqual(v.right, 0.0)

        self.assertEqual(
            AppKit.NSEdgeInsets.__typestr__,
            b"{NSEdgeInsets="
            + objc._C_CGFloat
            + objc._C_CGFloat
            + objc._C_CGFloat
            + objc._C_CGFloat
            + b"}",
        )

    @min_os_level("10.7")
    def testFunctions10_7(self):
        v = AppKit.NSEdgeInsetsMake(1, 2, 3, 4)
        self.assertIsInstance(v, AppKit.NSEdgeInsets)
        self.assertEqual(v.top, 1.0)
        self.assertEqual(v.left, 2.0)
        self.assertEqual(v.bottom, 3.0)
        self.assertEqual(v.right, 4.0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSLayoutConstraint.shouldBeArchived)
        self.assertArgIsBOOL(AppKit.NSLayoutConstraint.setShouldBeArchived_, 0)

        self.assertResultIsBOOL(AppKit.NSView.needsUpdateConstraints)
        self.assertArgIsBOOL(AppKit.NSView.setNeedsUpdateConstraints_, 0)

        self.assertResultIsBOOL(AppKit.NSView.needsLayout)
        self.assertArgIsBOOL(AppKit.NSView.setNeedsLayout_, 0)

        self.assertResultIsBOOL(AppKit.NSView.translatesAutoresizingMaskIntoConstraints)
        self.assertArgIsBOOL(
            AppKit.NSView.setTranslatesAutoresizingMaskIntoConstraints_, 0
        )

        self.assertResultIsBOOL(AppKit.NSView.requiresConstraintBasedLayout)
        self.assertResultIsBOOL(AppKit.NSView.hasAmbiguousLayout)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSLayoutConstraint.isActive)
        self.assertArgIsBOOL(AppKit.NSLayoutConstraint.setActive_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AppKit.NSView.isHorizontalContentSizeConstraintActive)
        self.assertArgIsBOOL(AppKit.NSView.setHorizontalContentSizeConstraintActive_, 0)

        self.assertResultIsBOOL(AppKit.NSView.isVerticalContentSizeConstraintActive)
        self.assertArgIsBOOL(AppKit.NSView.setVerticalContentSizeConstraintActive_, 0)
