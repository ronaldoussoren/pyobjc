
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenuItem (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSMenuItem.usesUserKeyEquivalents)
        self.assertArgIsBOOL(NSMenuItem.setUsesUserKeyEquivalents_, 0)
        self.assertResultIsBOOL(NSMenuItem.hasSubmenu)
        self.assertResultIsBOOL(NSMenuItem.isSeparatorItem)
        self.assertResultIsBOOL(NSMenuItem.isEnabled)
        self.assertArgIsBOOL(NSMenuItem.setEnabled_, 0)
        self.assertResultIsBOOL(NSMenuItem.isAlternate)
        self.assertArgIsBOOL(NSMenuItem.setAlternate_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSMenuItem.isHighlighted)
        self.assertResultIsBOOL(NSMenuItem.isHidden)
        self.assertArgIsBOOL(NSMenuItem.setHidden_, 0)
        self.assertResultIsBOOL(NSMenuItem.isHiddenOrHasHiddenAncestor)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(NSMenuItem.allowsKeyEquivalentWhenHidden)
        self.assertArgIsBOOL(NSMenuItem.setAllowsKeyEquivalentWhenHidden_, 0)

if __name__ == "__main__":
    main()
