import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSTokenFieldHelper(AppKit.NSObject):
    def tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_(
        self, a, b, c, d
    ):
        return 1

    def tokenField_shouldAddObjects_atIndex_(self, a, b, c):
        return 1

    def tokenField_writeRepresentedObjects_toPasteboard_(self, a, b, c):
        return 1

    def tokenField_hasMenuForRepresentedObject_(self, a, b):
        return 1

    def tokenField_styleForRepresentedObject_(self, a, b):
        return 1


class TestNSTokenField(TestCase):
    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSTokenFieldDelegate")

    def testProtocols(self):
        self.assertArgHasType(
            TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_,  # noqa: B950
            3,
            b"o^" + objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTokenFieldHelper.tokenField_shouldAddObjects_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTokenFieldHelper.tokenField_writeRepresentedObjects_toPasteboard_
        )
        self.assertResultIsBOOL(
            TestNSTokenFieldHelper.tokenField_hasMenuForRepresentedObject_
        )
        self.assertResultHasType(
            TestNSTokenFieldHelper.tokenField_styleForRepresentedObject_,
            objc._C_NSUInteger,
        )
