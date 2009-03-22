
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTokenFieldCellHelper (NSObject):
    def tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_(self, a, b, c, d): return 1
    def tokenFieldCell_shouldAddObjects_atIndex_(self, a, b, c): return 1
    def tokenFieldCell_writeRepresentedObjects_toPasteboard_(self, a, b, c): return 1
    def tokenFieldCell_hasMenuForRepresentedObject_(self, a, b): return 1
    def tokenFieldCell_styleForRepresentedObject_(self, a, b): return 1
        

class TestNSTokenFieldCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDefaultTokenStyle, 0)
        self.failUnlessEqual(NSPlainTextTokenStyle, 1)
        self.failUnlessEqual(NSRoundedTokenStyle, 2)

    def testProtocols(self):
        self.failUnlessArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 3, 'o^'+ objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_shouldAddObjects_atIndex_, 2, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSTokenFieldCellHelper.tokenFieldCell_writeRepresentedObjects_toPasteboard_)
        self.failUnlessResultIsBOOL(TestNSTokenFieldCellHelper.tokenFieldCell_hasMenuForRepresentedObject_)
        self.failUnlessResultHasType(TestNSTokenFieldCellHelper.tokenFieldCell_styleForRepresentedObject_, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
