import objc
import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSFontPanelHelper(AppKit.NSObject):
    def validModesForFontPanel_(self, p):
        return 1


class TestNSFontPanel(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSFPPreviewButton, 131)
        self.assertEqual(AppKit.NSFPRevertButton, 130)
        self.assertEqual(AppKit.NSFPSetButton, 132)
        self.assertEqual(AppKit.NSFPPreviewField, 128)
        self.assertEqual(AppKit.NSFPSizeField, 129)
        self.assertEqual(AppKit.NSFPSizeTitle, 133)
        self.assertEqual(AppKit.NSFPCurrentField, 134)
        self.assertEqual(AppKit.NSFontPanelFaceModeMask, 1 << 0)
        self.assertEqual(AppKit.NSFontPanelSizeModeMask, 1 << 1)
        self.assertEqual(AppKit.NSFontPanelCollectionModeMask, 1 << 2)
        self.assertEqual(AppKit.NSFontPanelUnderlineEffectModeMask, 1 << 8)
        self.assertEqual(AppKit.NSFontPanelStrikethroughEffectModeMask, 1 << 9)
        self.assertEqual(AppKit.NSFontPanelTextColorEffectModeMask, 1 << 10)
        self.assertEqual(AppKit.NSFontPanelDocumentColorEffectModeMask, 1 << 11)
        self.assertEqual(AppKit.NSFontPanelShadowEffectModeMask, 1 << 12)
        self.assertEqual(AppKit.NSFontPanelAllEffectsModeMask, (0xFFF00))
        self.assertEqual(AppKit.NSFontPanelStandardModesMask, (0xFFFF))
        self.assertEqual(AppKit.NSFontPanelAllModesMask, (0xFFFFFFFF))

        self.assertEqual(AppKit.NSFontPanelModeMaskFace, 1 << 0)
        self.assertEqual(AppKit.NSFontPanelModeMaskSize, 1 << 1)
        self.assertEqual(AppKit.NSFontPanelModeMaskCollection, 1 << 2)
        self.assertEqual(AppKit.NSFontPanelModeMaskUnderlineEffect, 1 << 8)
        self.assertEqual(AppKit.NSFontPanelModeMaskStrikethroughEffect, 1 << 9)
        self.assertEqual(AppKit.NSFontPanelModeMaskTextColorEffect, 1 << 10)
        self.assertEqual(AppKit.NSFontPanelModeMaskDocumentColorEffect, 1 << 11)
        self.assertEqual(AppKit.NSFontPanelModeMaskShadowEffect, 1 << 12)
        self.assertEqual(AppKit.NSFontPanelModeMaskAllEffects, 0xFFF00)
        self.assertEqual(AppKit.NSFontPanelModesMaskStandardModes, 0xFFFF)
        self.assertEqual(AppKit.NSFontPanelModesMaskAllModes, 0xFFFFFFFF)

    def testProtocols(self):
        self.assertResultHasType(
            TestNSFontPanelHelper.validModesForFontPanel_, objc._C_NSUInteger
        )

    @min_sdk_level("10.14")
    def testProtocols10_14(self):
        objc.protocolNamed("NSFontChanging")

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSFontPanel.sharedFontPanelExists)
        self.assertResultIsBOOL(AppKit.NSFontPanel.worksWhenModal)
        self.assertResultIsBOOL(AppKit.NSFontPanel.isEnabled)
        self.assertArgIsBOOL(AppKit.NSFontPanel.setEnabled_, 0)
        self.assertArgIsBOOL(AppKit.NSFontPanel.setPanelFont_isMultiple_, 1)
