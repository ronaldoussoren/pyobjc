import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSTextStorageHelper(AppKit.NSObject):
    def textStorage_willProcessEditing_range_changeInLength_(self, s, e, r, l):
        pass

    def textStorage_didProcessEditing_range_changeInLength_(self, s, e, r, l):
        pass


class TestNSTextStorage(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTextStorageEditedAttributes, 1 << 0)
        self.assertEqual(AppKit.NSTextStorageEditedCharacters, 1 << 1)

        self.assertIsInstance(AppKit.NSTextStorageWillProcessEditingNotification, str)
        self.assertIsInstance(AppKit.NSTextStorageDidProcessEditingNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextStorage.fixesAttributesLazily)

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTextStorageDelegate")

    def testProtocols(self):
        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_,
            3,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_,
            3,
            objc._C_NSInteger,
        )
