import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLayoutAnchor(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(AppKit.NSLayoutAnchor.hasAmbiguousLayout)
