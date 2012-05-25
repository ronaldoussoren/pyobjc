
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSToolbarHelper (NSObject):
    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(self, a, b, c): return 1

class TestNSToolbar (TestCase):
    def testConstants(self):
        self.assertEqual(NSToolbarDisplayModeDefault, 0)
        self.assertEqual(NSToolbarDisplayModeIconAndLabel, 1)
        self.assertEqual(NSToolbarDisplayModeIconOnly, 2)
        self.assertEqual(NSToolbarDisplayModeLabelOnly, 3)

        self.assertEqual(NSToolbarSizeModeDefault, 0)
        self.assertEqual(NSToolbarSizeModeRegular, 1)
        self.assertEqual(NSToolbarSizeModeSmall, 2)

        self.assertIsInstance(NSToolbarWillAddItemNotification, unicode)
        self.assertIsInstance(NSToolbarDidRemoveItemNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSToolbar.isVisible)
        self.assertArgIsBOOL(NSToolbar.setVisible_, 0)
        self.assertResultIsBOOL(NSToolbar.customizationPaletteIsRunning)
        self.assertResultIsBOOL(NSToolbar.showsBaselineSeparator)
        self.assertArgIsBOOL(NSToolbar.setShowsBaselineSeparator_, 0)
        self.assertResultIsBOOL(NSToolbar.allowsUserCustomization)
        self.assertArgIsBOOL(NSToolbar.setAllowsUserCustomization_, 0)
        self.assertResultIsBOOL(NSToolbar.autosavesConfiguration)
        self.assertArgIsBOOL(NSToolbar.setAutosavesConfiguration_, 0)

    def testProtocols(self):
        self.assertArgIsBOOL(TestNSToolbarHelper.toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_, 2)

if __name__ == "__main__":
    main()
