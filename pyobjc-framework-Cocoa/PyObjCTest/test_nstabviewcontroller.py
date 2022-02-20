import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTabViewController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTabViewControllerTabStyle)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(AppKit.NSTabViewControllerTabStyleSegmentedControlOnTop, 0)
        self.assertEqual(AppKit.NSTabViewControllerTabStyleSegmentedControlOnBottom, 1)
        self.assertEqual(AppKit.NSTabViewControllerTabStyleToolbar, 2)
        self.assertEqual(AppKit.NSTabViewControllerTabStyleUnspecified, -1)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(
            AppKit.NSTabViewController.canPropagateSelectedChildViewControllerTitle
        )
        self.assertArgIsBOOL(
            AppKit.NSTabViewController.setCanPropagateSelectedChildViewControllerTitle_,
            0,
        )

        self.assertResultIsBOOL(
            AppKit.NSTabViewController.tabView_shouldSelectTabViewItem_
        )

        self.assertArgIsBOOL(
            AppKit.NSTabViewController.toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_,
            2,
        )
