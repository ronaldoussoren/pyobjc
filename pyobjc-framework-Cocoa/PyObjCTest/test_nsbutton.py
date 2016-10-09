
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSButton (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSButton.isBordered)
        self.assertArgIsBOOL(NSButton.setBordered_, 0)
        self.assertResultIsBOOL(NSButton.isTransparent)
        self.assertArgIsBOOL(NSButton.setTransparent_, 0)
        self.assertArgIsOut(NSButton.getPeriodicDelay_interval_, 0)
        self.assertArgIsOut(NSButton.getPeriodicDelay_interval_, 1)
        self.assertResultIsBOOL(NSButton.performKeyEquivalent_)
        self.assertResultIsBOOL(NSButton.allowsMixedState)
        self.assertArgIsBOOL(NSButton.setAllowsMixedState_, 0)
        self.assertArgIsBOOL(NSButton.setShowsBorderOnlyWhileMouseInside_, 0)
        self.assertResultIsBOOL(NSButton.showsBorderOnlyWhileMouseInside)
        self.assertArgIsBOOL(NSButton.highlight_, 0)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSButton.isSpringLoaded)
        self.assertArgIsBOOL(NSButton.setSpringLoaded_, 0)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSButton.imageHugsTitle)
        self.assertArgIsBOOL(NSButton.setImageHugsTitle_, 0)

        self.assertArgIsSEL(NSButton.buttonWithTitle_image_target_action_, 3, b'v@:@')
        self.assertArgIsSEL(NSButton.buttonWithTitle_target_action_, 2, b'v@:@')
        self.assertArgIsSEL(NSButton.buttonWithImage_target_action_, 2, b'v@:@')
        self.assertArgIsSEL(NSButton.checkboxWithTitle_target_action_, 2, b'v@:@')
        self.assertArgIsSEL(NSButton.radioButtonWithTitle_target_action_, 2, b'v@:@')

if __name__ == "__main__":
    main()
