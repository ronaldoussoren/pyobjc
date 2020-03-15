import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSSearchFieldCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSSearchFieldRecentsTitleMenuItemTag, 1000)
        self.assertEqual(AppKit.NSSearchFieldRecentsMenuItemTag, 1001)
        self.assertEqual(AppKit.NSSearchFieldClearRecentsMenuItemTag, 1002)
        self.assertEqual(AppKit.NSSearchFieldNoRecentsMenuItemTag, 1003)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSearchFieldCell.sendsWholeSearchString)
        self.assertArgIsBOOL(AppKit.NSSearchFieldCell.setSendsWholeSearchString_, 0)
        self.assertResultIsBOOL(AppKit.NSSearchFieldCell.sendsSearchStringImmediately)
        self.assertArgIsBOOL(
            AppKit.NSSearchFieldCell.setSendsSearchStringImmediately_, 0
        )
