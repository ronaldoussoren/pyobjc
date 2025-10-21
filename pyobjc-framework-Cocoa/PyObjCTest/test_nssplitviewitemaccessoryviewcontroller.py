import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)


class TestNSSplitViewItemAccessoryViewController(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(AppKit.NSSplitViewItemAccessoryViewController.isHidden)
        self.assertArgIsBOOL(
            AppKit.NSSplitViewItemAccessoryViewController.setHidden_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSSplitViewItemAccessoryViewController.automaticallyAppliesContentInsets
        )
        self.assertArgIsBOOL(
            AppKit.NSSplitViewItemAccessoryViewController.setAutomaticallyAppliesContentInsets_,
            0,
        )
