import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSMenuBadge(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSMenuItemBadgeType)
        self.assertEqual(AppKit.NSMenuItemBadgeTypeNone, 0)
        self.assertEqual(AppKit.NSMenuItemBadgeTypeUpdates, 1)
        self.assertEqual(AppKit.NSMenuItemBadgeTypeNewItems, 2)
        self.assertEqual(AppKit.NSMenuItemBadgeTypeAlerts, 3)
