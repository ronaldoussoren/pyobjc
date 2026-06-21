import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSToolbarItemHelper(AppKit.NSObject):
    def validateToolbarItem_(self, a):
        return


class TestNSToolbarItem(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSToolbarItemVisibilityPriority, int)
        self.assertIsTypedEnum(AppKit.NSToolbarItemIdentifier, str)

    def test_constants(self):
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

        self.assertIsEnumType(AppKit.NSToolbarItemStyle)
        self.assertEqual(AppKit.NSToolbarItemStylePlain, 0)
        self.assertEqual(AppKit.NSToolbarItemStyleProminent, 1)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(AppKit.NSToolbarToggleSidebarItemIdentifier, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(AppKit.NSToolbarCloudSharingItemIdentifier, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(AppKit.NSToolbarToggleInspectorItemIdentifier, str)
        self.assertIsInstance(
            AppKit.NSToolbarInspectorTrackingSeparatorItemIdentifier, str
        )

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSToolbarItem.autovalidates)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setAutovalidates_, 0)
        self.assertResultIsBOOL(AppKit.NSToolbarItem.allowsDuplicatesInToolbar)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isBordered)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setBordered_, 0)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isNavigational)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setNavigational_, 0)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isVisible)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(AppKit.NSToolbarItem.isHidden)
        self.assertArgIsBOOL(AppKit.NSToolbarItem.setHidden_, 0)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSToolbarItemHelper.validateToolbarItem_)

    @min_sdk_level("10.12")
    def test_protocols10_12(self):
        self.assertProtocolExists("NSCloudSharingValidation", AppKit)

    @min_sdk_level("10.14")
    def test_protocols10_14(self):
        self.assertProtocolExists("NSToolbarItemValidation", AppKit)
