import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSStackView(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSStackViewVisibilityPriority, float)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSStackViewDistribution)
        self.assertIsEnumType(AppKit.NSStackViewGravity)

    def testConstants(self):
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationVertical, 1)

        self.assertEqual(AppKit.NSStackViewGravityTop, 1)
        self.assertEqual(AppKit.NSStackViewGravityLeading, 1)
        self.assertEqual(AppKit.NSStackViewGravityCenter, 2)
        self.assertEqual(AppKit.NSStackViewGravityBottom, 3)
        self.assertEqual(AppKit.NSStackViewGravityTrailing, 3)

        self.assertEqual(AppKit.NSStackViewVisibilityPriorityMustHold, 1000.0)
        self.assertEqual(
            AppKit.NSStackViewVisibilityPriorityDetachOnlyIfNecessary, 900.0
        )
        self.assertEqual(AppKit.NSStackViewVisibilityPriorityNotVisible, 0.0)

        self.assertIsInstance(AppKit.NSStackViewSpacingUseDefault, float)
        self.assertEqual(AppKit.NSStackViewSpacingUseDefault, objc._FLT_MAX)

        self.assertEqual(AppKit.NSStackViewDistributionGravityAreas, -1)
        self.assertEqual(AppKit.NSStackViewDistributionFill, 0)
        self.assertEqual(AppKit.NSStackViewDistributionFillEqually, 1)
        self.assertEqual(AppKit.NSStackViewDistributionFillProportionally, 2)
        self.assertEqual(AppKit.NSStackViewDistributionEqualSpacing, 3)
        self.assertEqual(AppKit.NSStackViewDistributionEqualCentering, 4)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSStackView.hasEqualSpacing)
        self.assertArgIsBOOL(AppKit.NSStackView.setHasEqualSpacing_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSStackView.detachesHiddenViews)
        self.assertArgIsBOOL(AppKit.NSStackView.setDetachesHiddenViews_, 0)

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSStackViewDelegate")
