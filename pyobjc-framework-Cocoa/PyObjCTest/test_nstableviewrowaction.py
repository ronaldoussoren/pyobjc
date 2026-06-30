import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableViewRowAction(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTableViewRowActionStyle)
        self.assertEqual(AppKit.NSTableViewRowActionStyleRegular, 0)
        self.assertEqual(AppKit.NSTableViewRowActionStyleDestructive, 1)
