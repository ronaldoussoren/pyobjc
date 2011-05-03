
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontManagerHelper (NSObject):
    def fontManager_willIncludeFont_(self, m, f): return 1

class TestNSFontManager (TestCase):
    def testConstants(self):
        self.assertEqual(NSItalicFontMask, 0x00000001)
        self.assertEqual(NSBoldFontMask, 0x00000002)
        self.assertEqual(NSUnboldFontMask, 0x00000004)
        self.assertEqual(NSNonStandardCharacterSetFontMask, 0x00000008)
        self.assertEqual(NSNarrowFontMask, 0x00000010)
        self.assertEqual(NSExpandedFontMask, 0x00000020)
        self.assertEqual(NSCondensedFontMask, 0x00000040)
        self.assertEqual(NSSmallCapsFontMask, 0x00000080)
        self.assertEqual(NSPosterFontMask, 0x00000100)
        self.assertEqual(NSCompressedFontMask, 0x00000200)
        self.assertEqual(NSFixedPitchFontMask, 0x00000400)
        self.assertEqual(NSUnitalicFontMask, 0x01000000)
        self.assertEqual(NSFontCollectionApplicationOnlyMask, 1 << 0)
        self.assertEqual(NSNoFontChangeAction, 0)
        self.assertEqual(NSViaPanelFontAction, 1)
        self.assertEqual(NSAddTraitFontAction, 2)
        self.assertEqual(NSSizeUpFontAction, 3)
        self.assertEqual(NSSizeDownFontAction, 4)
        self.assertEqual(NSHeavierFontAction, 5)
        self.assertEqual(NSLighterFontAction, 6)
        self.assertEqual(NSRemoveTraitFontAction, 7)

    def testMethods(self):
        self.assertResultIsBOOL(NSFontManager.isMultiple)
        self.assertArgIsBOOL(NSFontManager.setSelectedFont_isMultiple_, 1)
        self.assertArgIsBOOL(NSFontManager.fontMenu_, 0)
        self.assertArgIsBOOL(NSFontManager.fontPanel_, 0)
        self.assertResultIsBOOL(NSFontManager.isEnabled)
        self.assertArgIsBOOL(NSFontManager.setEnabled_, 0)
        self.assertResultIsBOOL(NSFontManager.sendAction)
        self.assertArgIsBOOL(NSFontManager.setSelectedAttributes_isMultiple_, 1)
        self.assertResultIsBOOL(NSFontManager.addCollection_options_)
        self.assertResultIsBOOL(NSFontManager.removeCollection_)
        self.assertResultIsBOOL(NSFontManager.fontNamed_hasTraits_)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSFontManagerHelper.fontManager_willIncludeFont_)

if __name__ == "__main__":
    main()
