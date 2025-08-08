import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSViewLayoutRegion(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSViewLayoutRegionAdaptivityAxis)
        self.assertEqual(AppKit.NSViewLayoutRegionAdaptivityAxisNone, 0)
        self.assertEqual(AppKit.NSViewLayoutRegionAdaptivityAxisHorizontal, 1)
        self.assertEqual(AppKit.NSViewLayoutRegionAdaptivityAxisVertical, 2)
