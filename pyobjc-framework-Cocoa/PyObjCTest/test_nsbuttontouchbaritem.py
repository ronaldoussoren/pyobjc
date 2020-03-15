import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSButtonTouchBarItem(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_title_target_action_,
            3,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_image_target_action_,
            3,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_title_image_target_action_,  # noqa: B950
            4,
            b"v@:@",
        )
