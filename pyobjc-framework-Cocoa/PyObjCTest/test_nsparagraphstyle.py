import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSParagraphStyle(TestCase):
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
