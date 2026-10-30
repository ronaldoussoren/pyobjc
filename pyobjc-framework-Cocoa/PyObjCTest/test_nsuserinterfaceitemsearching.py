import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSUserInterfaceItemSearchingHelper(AppKit.NSObject):
    def searchForItemsWithSearchString_resultLimit_matchedItemHandler_(self, a, b, c):
        pass


class TestNSUserInterfaceItemSearching(TestCase):
    @min_sdk_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists("NSUserInterfaceItemSearching", AppKit)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNSUserInterfaceItemSearchingHelper.searchForItemsWithSearchString_resultLimit_matchedItemHandler_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestNSUserInterfaceItemSearchingHelper.searchForItemsWithSearchString_resultLimit_matchedItemHandler_,  # noqa: B950
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            AppKit.NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_
        )
        self.assertArgHasType(
            AppKit.NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_,
            3,
            b"o^" + AppKit.NSRange.__typestr__,
        )
