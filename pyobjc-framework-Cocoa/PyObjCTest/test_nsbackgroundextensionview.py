import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)


class TestNSAccessibility(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            AppKit.NSBackgroundExtensionView.automaticallyPlacesContentView
        )
        self.assertArgIsBOOL(
            AppKit.NSBackgroundExtensionView.setAutomaticallyPlacesContentView_, 0
        )
