
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenuItem (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMenuItem.usesUserKeyEquivalents)
        self.failUnlessArgIsBOOL(NSMenuItem.setUsesUserKeyEquivalents_, 0)
        self.failUnlessResultIsBOOL(NSMenuItem.hasSubmenu)
        self.failUnlessResultIsBOOL(NSMenuItem.isSeparatorItem)
        self.failUnlessResultIsBOOL(NSMenuItem.isEnabled)
        self.failUnlessArgIsBOOL(NSMenuItem.setEnabled_, 0)
        self.failUnlessResultIsBOOL(NSMenuItem.isAlternate)
        self.failUnlessArgIsBOOL(NSMenuItem.setAlternate_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSMenuItem.isHighlighted)
        self.failUnlessResultIsBOOL(NSMenuItem.isHidden)
        self.failUnlessArgIsBOOL(NSMenuItem.setHidden_, 0)
        self.failUnlessResultIsBOOL(NSMenuItem.isHiddenOrHasHiddenAncestor)

if __name__ == "__main__":
    main()
