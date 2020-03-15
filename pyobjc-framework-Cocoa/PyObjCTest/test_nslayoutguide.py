import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLayoutGuide(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSLayoutGuide.hasAmbiguousLayout)
