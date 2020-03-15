import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSStatusBarButton(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSStatusBarButton.appearsDisabled)
        self.assertArgIsBOOL(AppKit.NSStatusBarButton.setAppearsDisabled_, 0)
