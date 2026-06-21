import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSStatusBar(TestCase):
    def test_constants(self):
        self.assertEqual(AppKit.NSVariableStatusItemLength, -1.0)
        self.assertEqual(AppKit.NSSquareStatusItemLength, -2.0)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSStatusBar.isVertical)
