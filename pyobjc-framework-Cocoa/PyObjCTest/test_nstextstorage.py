
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSTextStorage (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextStorageEditedAttributes, 1)
        self.assertEqual(NSTextStorageEditedCharacters, 2)

        self.assertIsInstance(NSTextStorageWillProcessEditingNotification, unicode)
        self.assertIsInstance(NSTextStorageDidProcessEditingNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSTextStorage.fixesAttributesLazily)


if __name__ == "__main__":
    main()
