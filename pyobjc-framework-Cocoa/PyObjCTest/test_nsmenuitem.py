
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

if __name__ == "__main__":
    main()
