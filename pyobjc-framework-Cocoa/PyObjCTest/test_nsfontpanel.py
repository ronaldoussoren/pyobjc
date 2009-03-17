
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontPanelHelper (NSObject):
    def validModesForFontPanel_(self, p): return 1

class TestNSFontPanel (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSFPPreviewButton, 131)
        self.failUnlessEqual(NSFPRevertButton, 130)
        self.failUnlessEqual(NSFPSetButton, 132)
        self.failUnlessEqual(NSFPPreviewField, 128)
        self.failUnlessEqual(NSFPSizeField, 129)
        self.failUnlessEqual(NSFPSizeTitle, 133)
        self.failUnlessEqual(NSFPCurrentField, 134)
        self.failUnlessEqual(NSFontPanelFaceModeMask, 1 << 0)
        self.failUnlessEqual(NSFontPanelSizeModeMask, 1 << 1)
        self.failUnlessEqual(NSFontPanelCollectionModeMask, 1 << 2)
        self.failUnlessEqual(NSFontPanelUnderlineEffectModeMask, 1<<8)
        self.failUnlessEqual(NSFontPanelStrikethroughEffectModeMask, 1<<9)
        self.failUnlessEqual(NSFontPanelTextColorEffectModeMask, 1<< 10)
        self.failUnlessEqual(NSFontPanelDocumentColorEffectModeMask, 1<<11)
        self.failUnlessEqual(NSFontPanelShadowEffectModeMask, 1<<12)
        self.failUnlessEqual(NSFontPanelAllEffectsModeMask, cast_int(0XFFF00))
        self.failUnlessEqual(NSFontPanelStandardModesMask, cast_int(0xFFFF))
        self.failUnlessEqual(NSFontPanelAllModesMask, cast_int(0xFFFFFFFF))

    def testProtocols(self):
        self.failUnlessResultHasType(TestNSFontPanelHelper.validModesForFontPanel_, objc._C_NSUInteger)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFontPanel.sharedFontPanelExists)
        self.failUnlessResultIsBOOL(NSFontPanel.worksWhenModal)
        self.failUnlessResultIsBOOL(NSFontPanel.isEnabled)
        self.failUnlessArgIsBOOL(NSFontPanel.setEnabled_, 0)
        self.failUnlessArgIsBOOL(NSFontPanel.setPanelFont_isMultiple_, 1)

if __name__ == "__main__":
    main()
