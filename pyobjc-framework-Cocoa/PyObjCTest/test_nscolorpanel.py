
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSColorPanel (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(NSNoModeColorPanel, -1)

    def testConstants(self):
        self.assertEqual(NSGrayModeColorPanel, 0)
        self.assertEqual(NSRGBModeColorPanel, 1)
        self.assertEqual(NSCMYKModeColorPanel, 2)
        self.assertEqual(NSHSBModeColorPanel, 3)
        self.assertEqual(NSCustomPaletteModeColorPanel, 4)
        self.assertEqual(NSColorListModeColorPanel, 5)
        self.assertEqual(NSWheelModeColorPanel, 6)
        self.assertEqual(NSCrayonModeColorPanel, 7)
        self.assertEqual(NSColorPanelGrayModeMask, 0x00000001)
        self.assertEqual(NSColorPanelRGBModeMask, 0x00000002)
        self.assertEqual(NSColorPanelCMYKModeMask, 0x00000004)
        self.assertEqual(NSColorPanelHSBModeMask, 0x00000008)
        self.assertEqual(NSColorPanelCustomPaletteModeMask, 0x00000010)
        self.assertEqual(NSColorPanelColorListModeMask, 0x00000020)
        self.assertEqual(NSColorPanelWheelModeMask, 0x00000040)
        self.assertEqual(NSColorPanelCrayonModeMask, 0x00000080)
        self.assertEqual(NSColorPanelAllModesMask, 0x0000ffff)

        self.assertIsInstance(NSColorPanelColorDidChangeNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSColorPanel.sharedColorPanelExists)
        self.assertResultIsBOOL(NSColorPanel.dragColor_withEvent_fromView_)

        self.assertResultIsBOOL(NSColorPanel.isContinuous)
        self.assertArgIsBOOL(NSColorPanel.setContinuous_, 0)

        self.assertResultIsBOOL(NSColorPanel.showsAlpha)
        self.assertArgIsBOOL(NSColorPanel.setShowsAlpha_, 0)


if __name__ == "__main__":
    main()
