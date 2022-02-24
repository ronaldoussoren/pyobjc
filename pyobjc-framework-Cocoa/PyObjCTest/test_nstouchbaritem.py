import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTouchBarItem(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTouchBarItemIdentifier, str)
        self.assertIsTypedEnum(AppKit.NSTouchBarItemPriority, float)

    @min_sdk_level("10.12")
    def testConstants(self):
        self.assertEqual(AppKit.NSTouchBarItemPriorityHigh, 1000.0)
        self.assertEqual(AppKit.NSTouchBarItemPriorityNormal, 0.0)
        self.assertEqual(AppKit.NSTouchBarItemPriorityLow, -1000.0)

        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierFixedSpaceSmall, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierFixedSpaceLarge, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierFlexibleSpace, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierOtherItemsProxy, str)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTouchBarItem.isVisible)
        # self.assertArgIsBOOL(AppKit.NSTouchBarItem.setVisible_, 0)
