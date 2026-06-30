import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSplitViewItem(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSSplitViewItemBehavior)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorDefault, 0)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorSidebar, 1)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorContentList, 2)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorInspector, 3)

        self.assertIsEnumType(AppKit.NSSplitViewItemCollapseBehavior)
        self.assertEqual(AppKit.NSSplitViewItemCollapseBehaviorDefault, 0)
        self.assertEqual(
            AppKit.NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings,
            1,
        )
        self.assertEqual(
            AppKit.NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView,
            2,
        )
        self.assertEqual(AppKit.NSSplitViewItemCollapseBehaviorUseConstraints, 3)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.isCollapsed)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setCollapsed_, 0)

        self.assertResultIsBOOL(AppKit.NSSplitViewItem.canCollapse)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setCanCollapse_, 0)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertIsInstance(AppKit.NSSplitViewItemUnspecifiedDimension, float)

        self.assertResultIsBOOL(AppKit.NSSplitViewItem.isSpringLoaded)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setSpringLoaded_, 0)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.canCollapseFromWindowResize)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setCanCollapseFromWindowResize_, 0)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.allowsFullHeightLayout)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setAllowsFullHeightLayout_, 0)
