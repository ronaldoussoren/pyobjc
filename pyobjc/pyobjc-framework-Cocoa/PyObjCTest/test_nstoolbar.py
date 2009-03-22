
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSToolbarHelper (NSObject):
    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(self, a, b, c): return 1

class TestNSToolbar (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSToolbarDisplayModeDefault, 0)
        self.failUnlessEqual(NSToolbarDisplayModeIconAndLabel, 1)
        self.failUnlessEqual(NSToolbarDisplayModeIconOnly, 2)
        self.failUnlessEqual(NSToolbarDisplayModeLabelOnly, 3)

        self.failUnlessEqual(NSToolbarSizeModeDefault, 0)
        self.failUnlessEqual(NSToolbarSizeModeRegular, 1)
        self.failUnlessEqual(NSToolbarSizeModeSmall, 2)

        self.failUnlessIsInstance(NSToolbarWillAddItemNotification, unicode)
        self.failUnlessIsInstance(NSToolbarDidRemoveItemNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSToolbar.isVisible)
        self.failUnlessArgIsBOOL(NSToolbar.setVisible_, 0)
        self.failUnlessResultIsBOOL(NSToolbar.customizationPaletteIsRunning)
        self.failUnlessResultIsBOOL(NSToolbar.showsBaselineSeparator)
        self.failUnlessArgIsBOOL(NSToolbar.setShowsBaselineSeparator_, 0)
        self.failUnlessResultIsBOOL(NSToolbar.allowsUserCustomization)
        self.failUnlessArgIsBOOL(NSToolbar.setAllowsUserCustomization_, 0)
        self.failUnlessResultIsBOOL(NSToolbar.autosavesConfiguration)
        self.failUnlessArgIsBOOL(NSToolbar.setAutosavesConfiguration_, 0)

    def testProtocols(self):
        self.failUnlessArgIsBOOL(TestNSToolbarHelper.toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_, 2)

if __name__ == "__main__":
    main()
