import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextLayoutFragment(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextLayoutFragmentEnumerationOptions)
        self.assertIsEnumType(AppKit.NSTextLayoutFragmentState)

    def test_constants(self):
        self.assertEqual(AppKit.NSTextLayoutFragmentEnumerationOptionsNone, 0)
        self.assertEqual(AppKit.NSTextLayoutFragmentEnumerationOptionsReverse, 1 << 0)
        self.assertEqual(
            AppKit.NSTextLayoutFragmentEnumerationOptionsEstimatesSize, 1 << 1
        )
        self.assertEqual(
            AppKit.NSTextLayoutFragmentEnumerationOptionsEnsuresLayout, 1 << 2
        )
        self.assertEqual(
            AppKit.NSTextLayoutFragmentEnumerationOptionsEnsuresExtraLineFragment,
            1 << 3,
        )

        self.assertEqual(AppKit.NSTextLayoutFragmentStateNone, 0)
        self.assertEqual(AppKit.NSTextLayoutFragmentStateEstimatedUsageBounds, 1)
        self.assertEqual(AppKit.NSTextLayoutFragmentStateCalculatedUsageBounds, 2)
        self.assertEqual(AppKit.NSTextLayoutFragmentStateLayoutAvailable, 3)
