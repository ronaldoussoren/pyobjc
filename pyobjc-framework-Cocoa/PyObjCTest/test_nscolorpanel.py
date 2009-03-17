
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorPanel (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessEqual(NSNoModeColorPanel, -1)

    def testConstants(self):
        self.failUnlessEqual(NSGrayModeColorPanel, 0)
        self.failUnlessEqual(NSRGBModeColorPanel, 1)
        self.failUnlessEqual(NSCMYKModeColorPanel, 2)
        self.failUnlessEqual(NSHSBModeColorPanel, 3)
        self.failUnlessEqual(NSCustomPaletteModeColorPanel, 4)
        self.failUnlessEqual(NSColorListModeColorPanel, 5)
        self.failUnlessEqual(NSWheelModeColorPanel, 6)
        self.failUnlessEqual(NSCrayonModeColorPanel, 7)
        self.failUnlessEqual(NSColorPanelGrayModeMask, 0x00000001)
        self.failUnlessEqual(NSColorPanelRGBModeMask, 0x00000002)
        self.failUnlessEqual(NSColorPanelCMYKModeMask, 0x00000004)
        self.failUnlessEqual(NSColorPanelHSBModeMask, 0x00000008)
        self.failUnlessEqual(NSColorPanelCustomPaletteModeMask, 0x00000010)
        self.failUnlessEqual(NSColorPanelColorListModeMask, 0x00000020)
        self.failUnlessEqual(NSColorPanelWheelModeMask, 0x00000040)
        self.failUnlessEqual(NSColorPanelCrayonModeMask, 0x00000080)
        self.failUnlessEqual(NSColorPanelAllModesMask, 0x0000ffff)

        self.failUnlessIsInstance(NSColorPanelColorDidChangeNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSColorPanel.sharedColorPanelExists)
        self.failUnlessResultIsBOOL(NSColorPanel.dragColor_withEvent_fromView_)

        self.failUnlessResultIsBOOL(NSColorPanel.isContinuous)
        self.failUnlessArgIsBOOL(NSColorPanel.setContinuous_, 0)

        self.failUnlessResultIsBOOL(NSColorPanel.showsAlpha)
        self.failUnlessArgIsBOOL(NSColorPanel.setShowsAlpha_, 0)


if __name__ == "__main__":
    main()
