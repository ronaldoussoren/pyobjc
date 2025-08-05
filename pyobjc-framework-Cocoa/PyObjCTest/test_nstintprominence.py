import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTintProminence(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSTintProminence)
        self.assertEqual(AppKit.NSTintProminenceAutomatic, 0)
        self.assertEqual(AppKit.NSTintProminenceNone, 1)
        self.assertEqual(AppKit.NSTintProminencePrimary, 2)
        self.assertEqual(AppKit.NSTintProminenceSecondary, 3)
