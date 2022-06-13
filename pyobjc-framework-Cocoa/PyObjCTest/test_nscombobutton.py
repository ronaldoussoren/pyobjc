import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSComboButton(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSComboButtonStyle)
        self.assertEqual(AppKit.NSComboButtonStyleSplit, 0)
        self.assertEqual(AppKit.NSComboButtonStyleUnified, 1)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsSEL(
            AppKit.NSComboButton.comboButtonWithTitle_menu_target_action_, 3, b"v@:@"
        )
        self.assertArgIsSEL(
            AppKit.NSComboButton.comboButtonWithImage_menu_target_action_, 3, b"v@:@"
        )
        self.assertArgIsSEL(
            AppKit.NSComboButton.comboButtonWithTitle_image_menu_target_action_,
            4,
            b"v@:@",
        )
