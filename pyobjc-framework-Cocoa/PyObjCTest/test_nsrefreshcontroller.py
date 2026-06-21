import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRefreshController(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSRefreshController.isRefreshing)

        self.assertResultIsSEL(AppKit.NSRefreshController.action_, b"v@:@")
        self.assertArgIsSEL(AppKit.NSRefreshController.setAction_, 0, b"v@:@")
