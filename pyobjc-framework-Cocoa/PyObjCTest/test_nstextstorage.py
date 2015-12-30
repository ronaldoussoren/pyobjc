
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextStorageHelper (NSObject):
    def textStorage_willProcessEditing_range_changeInLength_(self, s, e, r, l): pass
    def textStorage_didProcessEditing_range_changeInLength_(self, s, e, r, l): pass

class TestNSTextStorage (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextStorageEditedAttributes, 1)
        self.assertEqual(NSTextStorageEditedCharacters, 2)

        self.assertIsInstance(NSTextStorageWillProcessEditingNotification, unicode)
        self.assertIsInstance(NSTextStorageDidProcessEditingNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSTextStorage.fixesAttributesLazily)

    @min_sdk_level('10.10')
    def testProtocolObjects(self):
        objc.protocolNamed('NSTextStorageDelegate')

    def testProtocols(self):
        self.assertArgHasType(TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_, 2, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextStorageHelper.textStorage_willProcessEditing_range_changeInLength_, 3, objc._C_NSInteger)

        self.assertArgHasType(TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_, 2, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextStorageHelper.textStorage_didProcessEditing_range_changeInLength_, 3, objc._C_NSInteger)

if __name__ == "__main__":
    main()
