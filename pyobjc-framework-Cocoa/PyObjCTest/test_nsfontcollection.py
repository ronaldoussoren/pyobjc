import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFontCollection(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSFontCollectionVisibilityProcess, 1)
        self.assertEqual(AppKit.NSFontCollectionVisibilityUser, 2)
        self.assertEqual(AppKit.NSFontCollectionVisibilityComputer, 4)

        self.assertIsInstance(AppKit.NSFontCollectionIncludeDisabledFontsOption, str)
        self.assertIsInstance(AppKit.NSFontCollectionRemoveDuplicatesOption, str)
        self.assertIsInstance(AppKit.NSFontCollectionDisallowAutoActivationOption, str)
        self.assertIsInstance(AppKit.NSFontCollectionDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSFontCollectionActionKey, str)
        self.assertIsInstance(AppKit.NSFontCollectionNameKey, str)
        self.assertIsInstance(AppKit.NSFontCollectionOldNameKey, str)
        self.assertIsInstance(AppKit.NSFontCollectionVisibilityKey, str)
        self.assertIsInstance(AppKit.NSFontCollectionWasShown, str)
        self.assertIsInstance(AppKit.NSFontCollectionWasHidden, str)
        self.assertIsInstance(AppKit.NSFontCollectionWasRenamed, str)
        self.assertIsInstance(AppKit.NSFontCollectionAllFonts, str)
        self.assertIsInstance(AppKit.NSFontCollectionUser, str)
        self.assertIsInstance(AppKit.NSFontCollectionFavorites, str)
        self.assertIsInstance(AppKit.NSFontCollectionRecentlyUsed, str)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            AppKit.NSFontCollection.showFontCollection_withName_visibility_error_
        )
        self.assertArgIsOut(
            AppKit.NSFontCollection.showFontCollection_withName_visibility_error_, 3
        )
        self.assertResultIsBOOL(
            AppKit.NSFontCollection.hideFontCollectionWithName_visibility_error_
        )
        self.assertArgIsOut(
            AppKit.NSFontCollection.hideFontCollectionWithName_visibility_error_, 2
        )

        self.assertResultIsBOOL(
            AppKit.NSFontCollection.renameFontCollectionWithName_visibility_toName_error_
        )
        self.assertArgIsOut(
            AppKit.NSFontCollection.renameFontCollectionWithName_visibility_toName_error_,
            3,
        )
