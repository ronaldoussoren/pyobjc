import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSParagraphStyle(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTextTabOptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSLineBreakMode)
        self.assertIsEnumType(AppKit.NSLineBreakStrategy)
        self.assertIsEnumType(AppKit.NSTextTabType)

    def testConstants(self):
        self.assertEqual(AppKit.NSLeftTabStopType, 0)
        self.assertEqual(AppKit.NSRightTabStopType, 1)
        self.assertEqual(AppKit.NSCenterTabStopType, 2)
        self.assertEqual(AppKit.NSDecimalTabStopType, 3)

        self.assertEqual(AppKit.NSLineBreakByWordWrapping, 0)
        self.assertEqual(AppKit.NSLineBreakByCharWrapping, 1)
        self.assertEqual(AppKit.NSLineBreakByClipping, 2)
        self.assertEqual(AppKit.NSLineBreakByTruncatingHead, 3)
        self.assertEqual(AppKit.NSLineBreakByTruncatingTail, 4)
        self.assertEqual(AppKit.NSLineBreakByTruncatingMiddle, 5)

        self.assertIsInstance(AppKit.NSTabColumnTerminatorsAttributeName, str)

        self.assertEqual(AppKit.NSLineBreakStrategyNone, 0)
        self.assertEqual(AppKit.NSLineBreakStrategyPushOut, 1 << 0)
        self.assertEqual(AppKit.NSLineBreakStrategyHangulWordPriority, 1 << 1)
        self.assertEqual(AppKit.NSLineBreakStrategyStandard, 0xFFFF)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AppKit.NSParagraphStyle.allowsDefaultTighteningForTruncation
        )
        self.assertArgIsBOOL(
            AppKit.NSMutableParagraphStyle.setAllowsDefaultTighteningForTruncation_, 0
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(AppKit.NSParagraphStyle.usesDefaultHyphenation)
        self.assertArgIsBOOL(
            AppKit.NSMutableParagraphStyle.setUsesDefaultHyphenation_, 0
        )
