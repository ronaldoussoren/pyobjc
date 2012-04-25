
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontPanelHelper (NSObject):
    def validModesForFontPanel_(self, p): return 1

class TestNSFontPanel (TestCase):
    def testConstants(self):
        self.assertEqual(NSFPPreviewButton, 131)
        self.assertEqual(NSFPRevertButton, 130)
        self.assertEqual(NSFPSetButton, 132)
        self.assertEqual(NSFPPreviewField, 128)
        self.assertEqual(NSFPSizeField, 129)
        self.assertEqual(NSFPSizeTitle, 133)
        self.assertEqual(NSFPCurrentField, 134)
        self.assertEqual(NSFontPanelFaceModeMask, 1 << 0)
        self.assertEqual(NSFontPanelSizeModeMask, 1 << 1)
        self.assertEqual(NSFontPanelCollectionModeMask, 1 << 2)
        self.assertEqual(NSFontPanelUnderlineEffectModeMask, 1<<8)
        self.assertEqual(NSFontPanelStrikethroughEffectModeMask, 1<<9)
        self.assertEqual(NSFontPanelTextColorEffectModeMask, 1<< 10)
        self.assertEqual(NSFontPanelDocumentColorEffectModeMask, 1<<11)
        self.assertEqual(NSFontPanelShadowEffectModeMask, 1<<12)
        self.assertEqual(NSFontPanelAllEffectsModeMask, (0XFFF00))
        self.assertEqual(NSFontPanelStandardModesMask, (0xFFFF))
        self.assertEqual(NSFontPanelAllModesMask, (0xFFFFFFFF))

    def testProtocols(self):
        self.assertResultHasType(TestNSFontPanelHelper.validModesForFontPanel_, objc._C_NSUInteger)

    def testMethods(self):
        self.assertResultIsBOOL(NSFontPanel.sharedFontPanelExists)
        self.assertResultIsBOOL(NSFontPanel.worksWhenModal)
        self.assertResultIsBOOL(NSFontPanel.isEnabled)
        self.assertArgIsBOOL(NSFontPanel.setEnabled_, 0)
        self.assertArgIsBOOL(NSFontPanel.setPanelFont_isMultiple_, 1)

if __name__ == "__main__":
    main()
