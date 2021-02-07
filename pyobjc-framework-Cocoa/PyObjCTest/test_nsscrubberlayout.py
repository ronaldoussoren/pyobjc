import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSScrubberLayoutHelper(AppKit.NSObject):
    def scrubber_layout_sizeForItemAtIndex_(self, s, x, i):
        return 1


class TestNSScrubberLayout(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(
            AppKit.NSScrubberLayout.shouldInvalidateLayoutForSelectionChange
        )
        self.assertResultIsBOOL(
            AppKit.NSScrubberLayout.shouldInvalidateLayoutForHighlightChange
        )
        self.assertResultIsBOOL(
            AppKit.NSScrubberLayout.shouldInvalidateLayoutForChangeFromVisibleRect_toVisibleRect_  # noqa: B950
        )
        self.assertResultIsBOOL(
            AppKit.NSScrubberLayout.automaticallyMirrorsInRightToLeftLayout
        )

        self.assertResultHasType(
            TestNSScrubberLayoutHelper.scrubber_layout_sizeForItemAtIndex_,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSScrubberLayoutHelper.scrubber_layout_sizeForItemAtIndex_,
            2,
            objc._C_NSInteger,
        )

    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("NSScrubberFlowLayoutDelegate")
