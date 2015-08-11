
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

if __name__ == "__main__":
    main()
