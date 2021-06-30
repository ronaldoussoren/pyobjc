import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMenuItem(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.usesUserKeyEquivalents)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setUsesUserKeyEquivalents_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.hasSubmenu)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isSeparatorItem)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isAlternate)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setAlternate_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHighlighted)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHidden)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItem.isHiddenOrHasHiddenAncestor)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSMenuItem.allowsKeyEquivalentWhenHidden)
        self.assertArgIsBOOL(AppKit.NSMenuItem.setAllowsKeyEquivalentWhenHidden_, 0)

    @min_os_level("12.0")
    def testMethods12_0(self):
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
