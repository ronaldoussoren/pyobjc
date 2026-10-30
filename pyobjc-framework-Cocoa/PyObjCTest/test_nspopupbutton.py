import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPopUpButton(TestCase):
    def test_constants(self):
        self.assertIsInstance(AppKit.NSPopUpButtonWillPopUpNotification, str)

    def test_methods(self):
        self.assertArgIsBOOL(AppKit.NSPopUpButton.initWithFrame_pullsDown_, 1)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.pullsDown)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setPullsDown_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.autoenablesItems)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.selectItemWithTag_)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(AppKit.NSPopUpButton.usesItemFromMenu)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setUsesItemFromMenu_, 0)

        self.assertResultIsBOOL(AppKit.NSPopUpButton.altersStateOfSelectedItem)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setAltersStateOfSelectedItem_, 0)
