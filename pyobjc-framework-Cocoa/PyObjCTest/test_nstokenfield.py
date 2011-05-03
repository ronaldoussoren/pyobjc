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
        self.assertArgHasType(TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTokenFieldHelper.tokenField_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 3, b'o^' + objc._C_NSInteger)
        self.assertArgHasType(TestNSTokenFieldHelper.tokenField_shouldAddObjects_atIndex_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTokenFieldHelper.tokenField_writeRepresentedObjects_toPasteboard_)
        self.assertResultIsBOOL(TestNSTokenFieldHelper.tokenField_hasMenuForRepresentedObject_)
        self.assertResultHasType(TestNSTokenFieldHelper.tokenField_styleForRepresentedObject_, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
