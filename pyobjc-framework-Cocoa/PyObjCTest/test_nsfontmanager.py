import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSFontManagerHelper(AppKit.NSObject):
    def fontManager_willIncludeFont_(self, m, f):
        return 1


class TestNSFontManager(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSItalicFontMask, 0x00000001)
        self.assertEqual(AppKit.NSBoldFontMask, 0x00000002)
        self.assertEqual(AppKit.NSUnboldFontMask, 0x00000004)
        self.assertEqual(AppKit.NSNonStandardCharacterSetFontMask, 0x00000008)
        self.assertEqual(AppKit.NSNarrowFontMask, 0x00000010)
        self.assertEqual(AppKit.NSExpandedFontMask, 0x00000020)
        self.assertEqual(AppKit.NSCondensedFontMask, 0x00000040)
        self.assertEqual(AppKit.NSSmallCapsFontMask, 0x00000080)
        self.assertEqual(AppKit.NSPosterFontMask, 0x00000100)
        self.assertEqual(AppKit.NSCompressedFontMask, 0x00000200)
        self.assertEqual(AppKit.NSFixedPitchFontMask, 0x00000400)
        self.assertEqual(AppKit.NSUnitalicFontMask, 0x01000000)

        self.assertEqual(AppKit.NSFontCollectionApplicationOnlyMask, 1 << 0)

        self.assertEqual(AppKit.NSNoFontChangeAction, 0)
        self.assertEqual(AppKit.NSViaPanelFontAction, 1)
        self.assertEqual(AppKit.NSAddTraitFontAction, 2)
        self.assertEqual(AppKit.NSSizeUpFontAction, 3)
        self.assertEqual(AppKit.NSSizeDownFontAction, 4)
        self.assertEqual(AppKit.NSHeavierFontAction, 5)
        self.assertEqual(AppKit.NSLighterFontAction, 6)
        self.assertEqual(AppKit.NSRemoveTraitFontAction, 7)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSFontManager.isMultiple)
        self.assertArgIsBOOL(AppKit.NSFontManager.setSelectedFont_isMultiple_, 1)
        self.assertArgIsBOOL(AppKit.NSFontManager.fontMenu_, 0)
        self.assertArgIsBOOL(AppKit.NSFontManager.fontPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSFontManager.isEnabled)
        self.assertArgIsBOOL(AppKit.NSFontManager.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSFontManager.sendAction)
        self.assertArgIsBOOL(AppKit.NSFontManager.setSelectedAttributes_isMultiple_, 1)
        self.assertResultIsBOOL(AppKit.NSFontManager.addCollection_options_)
        self.assertResultIsBOOL(AppKit.NSFontManager.removeCollection_)
        self.assertResultIsBOOL(AppKit.NSFontManager.fontNamed_hasTraits_)

        self.assertArgIsBOOL(AppKit.NSFontManager.convertWeight_ofFont_, 0)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSFontManagerHelper.fontManager_willIncludeFont_)
