from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTokenFieldHelper (NSObject):
    def tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_(self, a, b, c, d): return 1
    def tokenField_shouldAddObjects_atIndex_(self, a, b, c): return 1
    def tokenField_writeRepresentedObjects_toPasteboard_(self, a, b, c): return 1
    def tokenField_hasMenuForRepresentedObject_(self, a, b): return 1
    def tokenField_styleForRepresentedObject_(self, a, b): return 1


class TestNSTokenField (TestCase):
    def testProtocols(self):
        self.failUnlessArgHasType(TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 3, 'o^' + objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTokenFieldHelper.tokenField_shouldAddObjects_atIndex_, 2, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSTokenFieldHelper.tokenField_writeRepresentedObjects_toPasteboard_)
        self.failUnlessResultIsBOOL(TestNSTokenFieldHelper.tokenField_hasMenuForRepresentedObject_)
        self.failUnlessResultHasType(TestNSTokenFieldHelper.tokenField_styleForRepresentedObject_, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
