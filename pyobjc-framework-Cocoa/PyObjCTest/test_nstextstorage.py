
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextStorage (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextStorageEditedAttributes, 1)
        self.failUnlessEqual(NSTextStorageEditedCharacters, 2)

        self.failUnlessIsInstance(NSTextStorageWillProcessEditingNotification, unicode)
        self.failUnlessIsInstance(NSTextStorageDidProcessEditingNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextStorage.fixesAttributesLazily)


if __name__ == "__main__":
    main()
