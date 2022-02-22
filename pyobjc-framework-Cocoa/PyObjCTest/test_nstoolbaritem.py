import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSToolbarItemHelper(AppKit.NSObject):
    def validateToolbarItem_(self, a):
        return


class TestNSToolbarItem(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSToolbarItemVisibilityPriority, int)

    def testConstants(self):
        self.assertEqual(AppKit.NSToolbarItemVisibilityPriorityStandard, 0)
        self.assertEqual(AppKit.NSToolbarItemVisibilityPriorityLow, -1000)
        self.assertEqual(AppKit.NSToolbarItemVisibilityPriorityHigh, 1000)
        self.assertEqual(AppKit.NSToolbarItemVisibilityPriorityUser, 2000)

        self.assertIsInstance(AppKit.NSToolbarSeparatorItemIdentifier, str)
        self.assertIsInstance(AppKit.NSToolbarSpaceItemIdentifier, str)
        self.assertIsInstance(AppKit.NSToolbarFlexibleSpaceItemIdentifier, str)

        self.assertIsInstance(AppKit.NSToolbarShowColorsItemIdentifier, str)
        self.assertIsInstance(AppKit.NSToolbarShowFontsItemIdentifier, str)
        self.assertIsInstance(AppKit.NSToolbarCustomizeToolbarItemIdentifier, str)
        self.assertIsInstance(AppKit.NSToolbarPrintItemIdentifier, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSToolbarToggleSidebarItemIdentifier, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSToolbarCloudSharingItemIdentifier, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSToolbarItem.autovalidates)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setAutovalidates_, 0)
        self.assertResultIsBOOL(AppKit.NSToolbarItem.allowsDuplicatesInToolbar)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isBordered)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setBordered_, 0)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isNavigational)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setNavigational_, 0)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSToolbarItemHelper.validateToolbarItem_)

    @min_sdk_level("10.12")
    def testProtocolObject(self):
        objc.protocolNamed("NSCloudSharingValidation")

    @min_sdk_level("10.14")
    def testProtocolObject10_14(self):
        objc.protocolNamed("NSToolbarItemValidation")
