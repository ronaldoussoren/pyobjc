import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableViewRowAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTableViewRowActionStyle)

    def test_constants(self):
        self.assertEqual(AppKit.NSTableViewRowActionStyleRegular, 0)
        self.assertEqual(AppKit.NSTableViewRowActionStyleDestructive, 1)
