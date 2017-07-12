
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSplitViewController (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSSplitViewItem.isCollapsed)
        self.assertArgIsBOOL(NSSplitViewItem.setCollapsed_, 0)
        self.assertResultIsBOOL(NSSplitViewItem.canCollapse)
        self.assertArgIsBOOL(NSSplitViewItem.setCanCollapse_, 0)

        self.assertResultIsBOOL(NSSplitViewController.splitView_canCollapseSubview_)
        self.assertResultIsBOOL(NSSplitViewController.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_)
        self.assertResultIsBOOL(NSSplitViewController.splitView_shouldHideDividerAtIndex_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSSplitViewItem.isSpringLoaded)
        self.assertArgIsBOOL(NSSplitViewItem.setSpringLoaded_, 0)
        self.assertResultIsBOOL(NSSplitViewController.validateUserInterfaceItem_)

    def testConstants(self):
        self.assertEqual(NSSplitViewItemBehaviorDefault, 0)
        self.assertEqual(NSSplitViewItemBehaviorSidebar, 1)
        self.assertEqual(NSSplitViewItemBehaviorContentList, 2)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSSplitViewControllerAutomaticDimension, float)
        self.assertIsInstance(NSSplitViewItemUnspecifiedDimension, float)

        self.assertEqual(NSSplitViewItemCollapseBehaviorDefault, 0)
        self.assertEqual(NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings, 1)
        self.assertEqual(NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView, 2)
        self.assertEqual(NSSplitViewItemCollapseBehaviorUseConstraints, 3)


if __name__ == "__main__":
    main()
