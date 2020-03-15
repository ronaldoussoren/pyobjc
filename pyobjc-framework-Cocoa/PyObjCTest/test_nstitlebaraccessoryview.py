import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTitlebarAccessoryViewController(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSTitlebarAccessoryViewController.isHidden)
        self.assertArgIsBOOL(AppKit.NSTitlebarAccessoryViewController.setHidden_, 0)
