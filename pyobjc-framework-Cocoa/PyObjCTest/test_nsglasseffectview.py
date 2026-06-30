import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSGlassEffectView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSGlassEffectViewStyle)
        self.assertEqual(AppKit.NSGlassEffectViewStyleRegular, 0)
        self.assertEqual(AppKit.NSGlassEffectViewStyleClear, 1)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSGlassEffectView.effectIsInteractive)
        self.assertArgIsBOOL(AppKit.NSGlassEffectView.setEffectIsInteractive_, 0)
