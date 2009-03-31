
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSToolbarItemHelper (NSObject):
    def validateToolbarItem_(self, a): return 

class TestNSToolbarItem (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityStandard, 0)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityLow, -1000)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityHigh, 1000)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityUser, 2000)

        self.failUnlessIsInstance(NSToolbarSeparatorItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarSpaceItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarFlexibleSpaceItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarShowColorsItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarShowFontsItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarCustomizeToolbarItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarPrintItemIdentifier, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSToolbarItem.isEnabled)
        self.failUnlessArgIsBOOL(NSToolbarItem.setEnabled_, 0)
        self.failUnlessResultIsBOOL(NSToolbarItem.autovalidates)
        self.failUnlessArgIsBOOL(NSToolbarItem.setAutovalidates_, 0)
        self.failUnlessResultIsBOOL(NSToolbarItem.allowsDuplicatesInToolbar)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSToolbarItemHelper.validateToolbarItem_)


if __name__ == "__main__":
    main()
