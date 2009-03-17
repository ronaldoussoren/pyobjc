
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSButton (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSButton.isBordered)
        self.failUnlessArgIsBOOL(NSButton.setBordered_, 0)
        self.failUnlessResultIsBOOL(NSButton.isTransparent)
        self.failUnlessArgIsBOOL(NSButton.setTransparent_, 0)
        self.failUnlessArgIsOut(NSButton.getPeriodicDelay_interval_, 0)
        self.failUnlessArgIsOut(NSButton.getPeriodicDelay_interval_, 1)
        self.failUnlessResultIsBOOL(NSButton.performKeyEquivalent_)
        self.failUnlessResultIsBOOL(NSButton.allowsMixedState)
        self.failUnlessArgIsBOOL(NSButton.setAllowsMixedState_, 0)

if __name__ == "__main__":
    main()
