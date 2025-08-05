import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import objc


class TestNSTextContentManagerHelper(AppKit.NSObject):
    def enumerateTextElementsFromLocation_options_usingBlock_(self, a, b, c):
        return 1

    def synchronizeToBackingStore_(self, a):
        pass

    def locationFromLocation_withOffset_(self, a, b):
        pass

    def offsetFromLocation_toLocation_(self, a, b):
        return 1

    def adjustedRangeFromRange_forEditingTextSelection_(self, a, b):
        return 1

    def textContentManager_shouldEnumerateTextElement_options_(self, a, b, c):
        return 1

    def textContentStorage_textParagraphWithRange_(self, a, b):
        return 1


class TestNSTextContentManager(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSTextContentManagerEnumerationOptions)
        self.assertEqual(AppKit.NSTextContentManagerEnumerationOptionsNone, 0)
        self.assertEqual(AppKit.NSTextContentManagerEnumerationOptionsReverse, 1 << 0)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AppKit.NSTextContentStorageUnsupportedAttributeAddedNotification, str
        )

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextElementProvider")
        self.assertProtocolExists("NSTextContentManagerDelegate")
        self.assertProtocolExists("NSTextContentStorageDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNSTextContentManagerHelper.enumerateTextElementsFromLocation_options_usingBlock_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestNSTextContentManagerHelper.enumerateTextElementsFromLocation_options_usingBlock_,
            2,
            b"Z@",
        )

        self.assertArgIsBlock(
            TestNSTextContentManagerHelper.synchronizeToBackingStore_, 0, b"v@"
        )

        self.assertArgHasType(
            TestNSTextContentManagerHelper.locationFromLocation_withOffset_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSTextContentManagerHelper.offsetFromLocation_toLocation_,
            objc._C_NSInteger,
        )

        self.assertArgIsBOOL(
            TestNSTextContentManagerHelper.adjustedRangeFromRange_forEditingTextSelection_,
            1,
        )

        self.assertResultIsBOOL(
            TestNSTextContentManagerHelper.textContentManager_shouldEnumerateTextElement_options_
        )
        self.assertArgHasType(
            TestNSTextContentManagerHelper.textContentManager_shouldEnumerateTextElement_options_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestNSTextContentManagerHelper.textContentStorage_textParagraphWithRange_,
            1,
            AppKit.NSRange.__typestr__,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            AppKit.NSTextContentManager.synchronizeTextLayoutManagers_, 0, b"v@"
        )
        self.assertResultIsBOOL(AppKit.NSTextContentManager.hasEditingTransaction)
        self.assertArgIsBlock(
            AppKit.NSTextContentManager.performEditingTransactionUsingBlock_, 0, b"v"
        )

        self.assertResultIsBOOL(
            AppKit.NSTextContentManager.automaticallySynchronizesTextLayoutManagers
        )
        self.assertArgIsBOOL(
            AppKit.NSTextContentManager.setAutomaticallySynchronizesTextLayoutManagers_,
            0,
        )

        self.assertResultIsBOOL(
            AppKit.NSTextContentManager.automaticallySynchronizesToBackingStore
        )
        self.assertArgIsBOOL(
            AppKit.NSTextContentManager.setAutomaticallySynchronizesToBackingStore_, 0
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(AppKit.NSTextList.includesTextListMarkers)
