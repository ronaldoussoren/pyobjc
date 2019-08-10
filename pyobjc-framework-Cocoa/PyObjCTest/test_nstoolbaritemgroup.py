from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSToolbarItemGroup(TestCase):
    def test_constants(self):
        self.assertEqual(NSToolbarItemGroupSelectionModeSelectOne, 0)
        self.assertEqual(NSToolbarItemGroupSelectionModeSelectAny, 1)
        self.assertEqual(NSToolbarItemGroupSelectionModeMomentary, 2)

        self.assertEqual(NSToolbarItemGroupControlRepresentationAutomatic, 0)
        self.assertEqual(NSToolbarItemGroupControlRepresentationExpanded, 1)
        self.assertEqual(NSToolbarItemGroupControlRepresentationCollapsed, 2)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsSEL(
            NSToolbarItemGroup.groupWithItemIdentifier_titles_selectionMode_labels_target_action_,
            5,
            b"v@:@",
        )
        self.assertArgIsSEL(
            NSToolbarItemGroup.groupWithItemIdentifier_images_selectionMode_labels_target_action_,
            5,
            b"v@:@",
        )

        self.assertArgIsBOOL(NSToolbarItemGroup.setSelected_atIndex_, 0)
        self.assertResultIsBOOL(NSToolbarItemGroup.isSelectedAtIndex_)


if __name__ == "__main__":
    main()
