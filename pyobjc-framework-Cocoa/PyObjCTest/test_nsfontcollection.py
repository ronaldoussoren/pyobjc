from PyObjCTools.TestSupport import *

import AppKit

try:
    unicode
except NameError:
    unicode = str

class TestNSFontCollection (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSFontCollectionVisibilityProcess, 1)
        self.assertEqual(AppKit.NSFontCollectionVisibilityUser, 2)
        self.assertEqual(AppKit.NSFontCollectionVisibilityComputer, 4)

        self.assertIsInstance(AppKit.NSFontCollectionIncludeDisabledFontsOption, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionRemoveDuplicatesOption, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionDisallowAutoActivationOption, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionDidChangeNotification, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionActionKey, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionNameKey, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionOldNameKey, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionVisibilityKey, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionWasShown, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionWasHidden, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionWasRenamed, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionAllFonts, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionUser, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionFavorites, unicode)
        self.assertIsInstance(AppKit.NSFontCollectionRecentlyUsed, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSFontCollection.showFontCollection_withName_visibility_error_)
        self.assertArgIsOut(AppKit.NSFontCollection.showFontCollection_withName_visibility_error_, 3)
        self.assertResultIsBOOL(AppKit.NSFontCollection.hideFontCollectionWithName_visibility_error_)
        self.assertArgIsOut(AppKit.NSFontCollection.hideFontCollectionWithName_visibility_error_, 2)

        self.assertResultIsBOOL(AppKit.NSFontCollection.renameFontCollectionWithName_visibility_toName_error_)
        self.assertArgIsOut(AppKit.NSFontCollection.renameFontCollectionWithName_visibility_toName_error_, 3)

if __name__ == "__main__":
    main()
