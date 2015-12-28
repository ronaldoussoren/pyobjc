
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
        self.assertEqual(NSDefaultTokenStyle, 0)
        self.assertEqual(NSTokenStyleNone, 1)
        self.assertEqual(NSTokenStyleRounded, 2)

        self.assertEqual(NSPlainTextTokenStyle, 1) # Deprecated
        self.assertEqual(NSRoundedTokenStyle, 2) # Deprecated

        self.assertEqual(NSTokenStyleDefault, 0)
        self.assertEqual(NSTokenStyleNone, 1)
        self.assertEqual(NSTokenStyleRounded, 2)
        self.assertEqual(NSTokenStyleSquared, 3)
        self.assertEqual(NSTokenStylePlainSquared, 4)

    @min_os_level('10.10')
    def testContants10_10(self):
        self.assertEqual(NSTokenStyleSquared, 3)
        self.assertEqual(NSTokenStylePlainSquared, 4)

    @min_sdk_level('10.7')
    def testProtocolObjects(self):
        objc.protocolNamed('NSTokenFieldCellDelegate')

    def testProtocols(self):
        self.assertArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_completionsForSubstring_indexOfToken_indexOfSelectedItem_, 3, b'o^'+ objc._C_NSInteger)
        self.assertArgHasType(TestNSTokenFieldCellHelper.tokenFieldCell_shouldAddObjects_atIndex_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTokenFieldCellHelper.tokenFieldCell_writeRepresentedObjects_toPasteboard_)
        self.assertResultIsBOOL(TestNSTokenFieldCellHelper.tokenFieldCell_hasMenuForRepresentedObject_)
        self.assertResultHasType(TestNSTokenFieldCellHelper.tokenFieldCell_styleForRepresentedObject_, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
