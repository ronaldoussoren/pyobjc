
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontManagerHelper (NSObject):
    def fontManager_willIncludeFont_(self, m, f): return 1

class TestNSFontManager (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSItalicFontMask, 0x00000001)
        self.failUnlessEqual(NSBoldFontMask, 0x00000002)
        self.failUnlessEqual(NSUnboldFontMask, 0x00000004)
        self.failUnlessEqual(NSNonStandardCharacterSetFontMask, 0x00000008)
        self.failUnlessEqual(NSNarrowFontMask, 0x00000010)
        self.failUnlessEqual(NSExpandedFontMask, 0x00000020)
        self.failUnlessEqual(NSCondensedFontMask, 0x00000040)
        self.failUnlessEqual(NSSmallCapsFontMask, 0x00000080)
        self.failUnlessEqual(NSPosterFontMask, 0x00000100)
        self.failUnlessEqual(NSCompressedFontMask, 0x00000200)
        self.failUnlessEqual(NSFixedPitchFontMask, 0x00000400)
        self.failUnlessEqual(NSUnitalicFontMask, 0x01000000)
        self.failUnlessEqual(NSFontCollectionApplicationOnlyMask, 1 << 0)
        self.failUnlessEqual(NSNoFontChangeAction, 0)
        self.failUnlessEqual(NSViaPanelFontAction, 1)
        self.failUnlessEqual(NSAddTraitFontAction, 2)
        self.failUnlessEqual(NSSizeUpFontAction, 3)
        self.failUnlessEqual(NSSizeDownFontAction, 4)
        self.failUnlessEqual(NSHeavierFontAction, 5)
        self.failUnlessEqual(NSLighterFontAction, 6)
        self.failUnlessEqual(NSRemoveTraitFontAction, 7)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFontManager.isMultiple)
        self.failUnlessArgIsBOOL(NSFontManager.setSelectedFont_isMultiple_, 1)
        self.failUnlessArgIsBOOL(NSFontManager.fontMenu_, 0)
        self.failUnlessArgIsBOOL(NSFontManager.fontPanel_, 0)
        self.failUnlessResultIsBOOL(NSFontManager.isEnabled)
        self.failUnlessArgIsBOOL(NSFontManager.setEnabled_, 0)
        self.failUnlessResultIsBOOL(NSFontManager.sendAction)
        self.failUnlessArgIsBOOL(NSFontManager.setSelectedAttributes_isMultiple_, 1)
        self.failUnlessResultIsBOOL(NSFontManager.addCollection_options_)
        self.failUnlessResultIsBOOL(NSFontManager.removeCollection_)
        self.failUnlessResultIsBOOL(NSFontManager.fontNamed_hasTraits_)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSFontManagerHelper.fontManager_willIncludeFont_)

if __name__ == "__main__":
    main()
