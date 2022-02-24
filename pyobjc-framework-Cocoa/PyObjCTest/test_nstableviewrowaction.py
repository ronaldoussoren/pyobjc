import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableViewRowAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTableViewRowActionStyle)

    def testConstants(self):
        self.assertEqual(AppKit.NSTableViewRowActionStyleRegular, 0)
        self.assertEqual(AppKit.NSTableViewRowActionStyleDestructive, 1)
