import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSColorPanel(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSColorPanelMode)
        self.assertIsEnumType(AppKit.NSColorPanelOptions)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSNoModeColorPanel, -1)

        self.assertEqual(AppKit.NSColorPanelModeNone, -1)

    def testConstants(self):
        self.assertEqual(AppKit.NSGrayModeColorPanel, 0)
        self.assertEqual(AppKit.NSRGBModeColorPanel, 1)
        self.assertEqual(AppKit.NSCMYKModeColorPanel, 2)
        self.assertEqual(AppKit.NSHSBModeColorPanel, 3)
        self.assertEqual(AppKit.NSCustomPaletteModeColorPanel, 4)
        self.assertEqual(AppKit.NSColorListModeColorPanel, 5)
        self.assertEqual(AppKit.NSWheelModeColorPanel, 6)
        self.assertEqual(AppKit.NSCrayonModeColorPanel, 7)

        self.assertEqual(AppKit.NSColorPanelModeGray, 0)
        self.assertEqual(AppKit.NSColorPanelModeRGB, 1)
        self.assertEqual(AppKit.NSColorPanelModeCMYK, 2)
        self.assertEqual(AppKit.NSColorPanelModeHSB, 3)
        self.assertEqual(AppKit.NSColorPanelModeCustomPalette, 4)
        self.assertEqual(AppKit.NSColorPanelModeColorList, 5)
        self.assertEqual(AppKit.NSColorPanelModeWheel, 6)
        self.assertEqual(AppKit.NSColorPanelModeCrayon, 7)

        self.assertEqual(AppKit.NSColorPanelGrayModeMask, 0x00000001)
        self.assertEqual(AppKit.NSColorPanelRGBModeMask, 0x00000002)
        self.assertEqual(AppKit.NSColorPanelCMYKModeMask, 0x00000004)
        self.assertEqual(AppKit.NSColorPanelHSBModeMask, 0x00000008)
        self.assertEqual(AppKit.NSColorPanelCustomPaletteModeMask, 0x00000010)
        self.assertEqual(AppKit.NSColorPanelColorListModeMask, 0x00000020)
        self.assertEqual(AppKit.NSColorPanelWheelModeMask, 0x00000040)
        self.assertEqual(AppKit.NSColorPanelCrayonModeMask, 0x00000080)
        self.assertEqual(AppKit.NSColorPanelAllModesMask, 0x0000FFFF)

        self.assertIsInstance(AppKit.NSColorPanelColorDidChangeNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSColorPanel.sharedColorPanelExists)
        self.assertResultIsBOOL(AppKit.NSColorPanel.dragColor_withEvent_fromView_)

        self.assertResultIsBOOL(AppKit.NSColorPanel.isContinuous)
        self.assertArgIsBOOL(AppKit.NSColorPanel.setContinuous_, 0)

        self.assertResultIsBOOL(AppKit.NSColorPanel.showsAlpha)
        self.assertArgIsBOOL(AppKit.NSColorPanel.setShowsAlpha_, 0)
