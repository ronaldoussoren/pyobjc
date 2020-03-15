import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSToolbarItemGroup(TestCase):
    def test_constants(self):
        self.assertEqual(AppKit.NSToolbarItemGroupSelectionModeSelectOne, 0)
        self.assertEqual(AppKit.NSToolbarItemGroupSelectionModeSelectAny, 1)
        self.assertEqual(AppKit.NSToolbarItemGroupSelectionModeMomentary, 2)

        self.assertEqual(AppKit.NSToolbarItemGroupControlRepresentationAutomatic, 0)
        self.assertEqual(AppKit.NSToolbarItemGroupControlRepresentationExpanded, 1)
        self.assertEqual(AppKit.NSToolbarItemGroupControlRepresentationCollapsed, 2)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsSEL(
            AppKit.NSToolbarItemGroup.groupWithItemIdentifier_titles_selectionMode_labels_target_action_,  # noqa: B950
            5,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSToolbarItemGroup.groupWithItemIdentifier_images_selectionMode_labels_target_action_,  # noqa: B950
            5,
            b"v@:@",
        )

        self.assertArgIsBOOL(AppKit.NSToolbarItemGroup.setSelected_atIndex_, 0)
        self.assertResultIsBOOL(AppKit.NSToolbarItemGroup.isSelectedAtIndex_)
