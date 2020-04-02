import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPickerTouchBarItem(TestCase):
    def test_contants(self):
        self.assertEqual(AppKit.NSPickerTouchBarItemSelectionModeSelectOne, 0)
        self.assertEqual(AppKit.NSPickerTouchBarItemSelectionModeSelectAny, 1)
        self.assertEqual(AppKit.NSPickerTouchBarItemSelectionModeMomentary, 2)

        self.assertEqual(AppKit.NSPickerTouchBarItemControlRepresentationAutomatic, 0)
        self.assertEqual(AppKit.NSPickerTouchBarItemControlRepresentationExpanded, 1)
        self.assertEqual(AppKit.NSPickerTouchBarItemControlRepresentationCollapsed, 2)

    @min_os_level("10.15")
    def test_nethods10_15(self):
        self.assertArgIsSEL(
            AppKit.NSPickerTouchBarItem.pickerTouchBarItemWithIdentifier_labels_selectionMode_target_action_,  # noqa: B950
            4,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSPickerTouchBarItem.pickerTouchBarItemWithIdentifier_images_selectionMode_target_action_,  # noqa: B950
            4,
            b"v@:@",
        )

        self.assertArgIsSEL(AppKit.NSPickerTouchBarItem.setAction_, 0, b"v@:@")

        self.assertResultIsBOOL(AppKit.NSPickerTouchBarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSPickerTouchBarItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSPickerTouchBarItem.isEnabledAtIndex_)
        self.assertArgIsBOOL(AppKit.NSPickerTouchBarItem.setEnabled_atIndex_, 0)
