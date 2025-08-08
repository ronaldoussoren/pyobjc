import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSGlassEffectView(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSGlassEffectViewStyle)
        self.assertEqual(AppKit.NSGlassEffectViewStyleRegular, 0)
        self.assertEqual(AppKit.NSGlassEffectViewStyleClear, 1)
