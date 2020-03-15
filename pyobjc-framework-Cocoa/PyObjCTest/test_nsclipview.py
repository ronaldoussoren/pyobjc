import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSClipView(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSClipView.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSClipView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSClipView.copiesOnScroll)
        self.assertArgIsBOOL(AppKit.NSClipView.setCopiesOnScroll_, 0)
        self.assertResultIsBOOL(AppKit.NSClipView.autoscroll_)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSClipView.automaticallyAdjustsContentInsets)
        self.assertArgIsBOOL(AppKit.NSClipView.setAutomaticallyAdjustsContentInsets_, 0)
