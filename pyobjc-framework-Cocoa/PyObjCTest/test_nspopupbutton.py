import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPopUpButton(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSPopUpButtonWillPopUpNotification, str)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSPopUpButton.initWithFrame_pullsDown_, 1)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.pullsDown)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setPullsDown_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.autoenablesItems)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(AppKit.NSPopUpButton.selectItemWithTag_)

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(AppKit.NSPopUpButton.usesItemFromMenu)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setUsesItemFromMenu_, 0)

        self.assertResultIsBOOL(AppKit.NSPopUpButton.altersStateOfSelectedItem)
        self.assertArgIsBOOL(AppKit.NSPopUpButton.setAltersStateOfSelectedItem_, 0)
