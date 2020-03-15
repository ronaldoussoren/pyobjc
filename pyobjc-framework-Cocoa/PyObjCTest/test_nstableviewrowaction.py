import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableViewRowAction(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTableViewRowActionStyleRegular, 0)
        self.assertEqual(AppKit.NSTableViewRowActionStyleDestructive, 1)
