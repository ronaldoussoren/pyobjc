import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSPageLayout(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSPageLayoutResult)
        self.assertEqual(AppKit.NSPageLayoutResultCancelled, 0)
        self.assertEqual(AppKit.NSPageLayoutResultChanged, 1)

    def testMethods(self):
        self.assertArgIsSEL(
            AppKit.NSPageLayout.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSPageLayout.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            AppKit.NSPageLayout.beginSheetUsingPrintInfo_onWindow_completionHandler_,
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
