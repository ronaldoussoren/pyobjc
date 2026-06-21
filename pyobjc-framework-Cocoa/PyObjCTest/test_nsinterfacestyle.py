import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSInterfaceStyle(TestCase):
    def test_constants(self):
        self.assertEqual(AppKit.NSNoInterfaceStyle, 0)
        self.assertEqual(AppKit.NSNextStepInterfaceStyle, 1)
        self.assertEqual(AppKit.NSWindows95InterfaceStyle, 2)
        self.assertEqual(AppKit.NSMacintoshInterfaceStyle, 3)

        self.assertIsInstance(AppKit.NSInterfaceStyleDefault, str)

    def test_functions(self):
        v = AppKit.NSInterfaceStyleForKey("button", None)
        self.assertIsInstance(v, int)
