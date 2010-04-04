from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSUserInterfaceItemSearchingHelper (NSObject):
    def searchForItemsWithSearchString_resultLimit_matchedItemHandler_(self, s, l, h): pass

class TestNSUserInterfaceItemSearching (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertArgHasType(TestNSUserInterfaceItemSearchingHelper.searchForItemsWithSearchString_resultLimit_matchedItemHandler_,
                1, objc._C_NSInteger)
        self.assertArgIsBlock(TestNSUserInterfaceItemSearchingHelper.searchForItemsWithSearchString_resultLimit_matchedItemHandler_,
                2, b'v@')

        self.assertResultIsBOOL(NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_)
        self.assertArgHasType(NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_, 2, NSRange.__typestr__)
        self.assertArgHasType(NSApplication.searchString_inUserInterfaceItemString_searchRange_foundRange_, 3, b'o^' + NSRange.__typestr__)

if __name__ == "__main__":
    main()
