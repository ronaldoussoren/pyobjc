import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSPageLayout(TestCase):
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
