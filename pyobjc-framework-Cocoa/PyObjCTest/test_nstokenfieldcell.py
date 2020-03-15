import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTokenFieldCellHelper(AppKit.NSObject):
    def tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_(
        self, a, b, c, d
    ):
        return 1

    def tokenFieldCell_shouldAddObjects_atIndex_(self, a, b, c):
        return 1

    def tokenFieldCell_writeRepresentedObjects_toPasteboard_(self, a, b, c):
        return 1

    def tokenFieldCell_hasMenuForRepresentedObject_(self, a, b):
        return 1

    def tokenFieldCell_styleForRepresentedObject_(self, a, b):
        return 1


class TestNSTokenFieldCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSDefaultTokenStyle, 0)
        self.assertEqual(AppKit.NSTokenStyleNone, 1)
        self.assertEqual(AppKit.NSTokenStyleRounded, 2)

        self.assertEqual(AppKit.NSPlainTextTokenStyle, 1)  # Deprecated
        self.assertEqual(AppKit.NSRoundedTokenStyle, 2)  # Deprecated

        self.assertEqual(AppKit.NSTokenStyleDefault, 0)
        self.assertEqual(AppKit.NSTokenStyleNone, 1)
        self.assertEqual(AppKit.NSTokenStyleRounded, 2)
        self.assertEqual(AppKit.NSTokenStyleSquared, 3)
        self.assertEqual(AppKit.NSTokenStylePlainSquared, 4)

    @min_os_level("10.10")
    def testContants10_10(self):
        self.assertEqual(AppKit.NSTokenStyleSquared, 3)
        self.assertEqual(AppKit.NSTokenStylePlainSquared, 4)

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTokenFieldCellDelegate")

    def testProtocols(self):
        self.assertArgHasType(
            TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_,  # noqa: B950
            3,
            b"o^" + objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTokenFieldCellHelper.tokenFieldCell_shouldAddObjects_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTokenFieldCellHelper.tokenFieldCell_writeRepresentedObjects_toPasteboard_
        )
        self.assertResultIsBOOL(
            TestNSTokenFieldCellHelper.tokenFieldCell_hasMenuForRepresentedObject_
        )
        self.assertResultHasType(
            TestNSTokenFieldCellHelper.tokenFieldCell_styleForRepresentedObject_,
            objc._C_NSUInteger,
        )
