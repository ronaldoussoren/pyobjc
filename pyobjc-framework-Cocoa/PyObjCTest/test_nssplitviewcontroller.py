import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSplitViewController(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.isCollapsed)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setCollapsed_, 0)
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.canCollapse)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setCanCollapse_, 0)

        self.assertResultIsBOOL(
            AppKit.NSSplitViewController.splitView_canCollapseSubview_
        )
        self.assertResultIsBOOL(
            AppKit.NSSplitViewController.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_  # noqa: B950
        )
        self.assertResultIsBOOL(
            AppKit.NSSplitViewController.splitView_shouldHideDividerAtIndex_
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItem.isSpringLoaded)
        self.assertArgIsBOOL(AppKit.NSSplitViewItem.setSpringLoaded_, 0)
        self.assertResultIsBOOL(AppKit.NSSplitViewController.validateUserInterfaceItem_)

    def testConstants(self):
        self.assertEqual(AppKit.NSSplitViewItemBehaviorDefault, 0)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorSidebar, 1)
        self.assertEqual(AppKit.NSSplitViewItemBehaviorContentList, 2)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSSplitViewControllerAutomaticDimension, float)
        self.assertIsInstance(AppKit.NSSplitViewItemUnspecifiedDimension, float)

        self.assertEqual(AppKit.NSSplitViewItemCollapseBehaviorDefault, 0)
        self.assertEqual(
            AppKit.NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings,
            1,
        )
        self.assertEqual(
            AppKit.NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView,
            2,
        )
        self.assertEqual(
            AppKit.NSSplitViewItemCollapseBehaviorUseConstraints, 3
        )  # noqa: B950
