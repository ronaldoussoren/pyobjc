import AppKit
from PyObjCTools.TestSupport import TestCase


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
