
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSToolbarItemHelper (NSObject):
    def validateToolbarItem_(self, a): return

class TestNSToolbarItem (TestCase):
    def testConstants(self):
        self.assertEqual(NSToolbarItemVisibilityPriorityStandard, 0)
        self.assertEqual(NSToolbarItemVisibilityPriorityLow, -1000)
        self.assertEqual(NSToolbarItemVisibilityPriorityHigh, 1000)
        self.assertEqual(NSToolbarItemVisibilityPriorityUser, 2000)

        self.assertIsInstance(NSToolbarSeparatorItemIdentifier, unicode)
        self.assertIsInstance(NSToolbarSpaceItemIdentifier, unicode)
        self.assertIsInstance(NSToolbarFlexibleSpaceItemIdentifier, unicode)

        self.assertIsInstance(NSToolbarShowColorsItemIdentifier, unicode)
        self.assertIsInstance(NSToolbarShowFontsItemIdentifier, unicode)
        self.assertIsInstance(NSToolbarCustomizeToolbarItemIdentifier, unicode)
        self.assertIsInstance(NSToolbarPrintItemIdentifier, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSToolbarToggleSidebarItemIdentifier, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSToolbarCloudSharingItemIdentifier, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSToolbarItem.isEnabled)
        self.assertArgIsBOOL(NSToolbarItem.setEnabled_, 0)
        self.assertResultIsBOOL(NSToolbarItem.autovalidates)
        self.assertArgIsBOOL(NSToolbarItem.setAutovalidates_, 0)
        self.assertResultIsBOOL(NSToolbarItem.allowsDuplicatesInToolbar)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSToolbarItemHelper.validateToolbarItem_)

    @min_sdk_level('10.12')
    def testProtocolObject(self):
        objc.protocolNamed('NSCloudSharingValidation')

    @min_sdk_level('10.14')
    def testProtocolObject10_14(self):
        objc.protocolNamed('NSToolbarItemValidation')

if __name__ == "__main__":
    main()
