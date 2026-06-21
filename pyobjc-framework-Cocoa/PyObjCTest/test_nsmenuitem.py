import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMenuItem(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSMenuItemImageVisibility)
        self.assertEqual(AppKit.NSMenuItemImageVisibilityAutomatic, 0)
        self.assertEqual(AppKit.NSMenuItemImageVisibilityVisible, 1)
        self.assertEqual(AppKit.NSMenuItemImageVisibilityHidden, 2)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.usesUserKeyEquivalents)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setUsesUserKeyEquivalents_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.hasSubmenu)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isSeparatorItem)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isAlternate)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setAlternate_, 0)

    @min_os_level("10.5")
    def test_methods10_5(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHighlighted)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHidden)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHiddenOrHasHiddenAncestor)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.allowsKeyEquivalentWhenHidden)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setAllowsKeyEquivalentWhenHidden_, 0)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AppKit.NSMenuItem.allowsAutomaticKeyEquivalentLocalization
        )
        self.assertArgIsBOOL(
            AppKit.NSMenuItem.setAllowsAutomaticKeyEquivalentLocalization_, 0
        )

        self.assertResultIsBOOL(AppKit.NSMenuItem.allowsAutomaticKeyEquivalentMirroring)
        self.assertArgIsBOOL(
            AppKit.NSMenuItem.setAllowsAutomaticKeyEquivalentMirroring_, 0
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.isSectionHeader)
