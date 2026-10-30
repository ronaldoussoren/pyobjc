import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSAnimationContext(TestCase):
    def test_methods(self):
        self.assertResultIsBlock(AppKit.NSAnimationContext.completionHandler, b"v")
        self.assertArgIsBlock(AppKit.NSAnimationContext.setCompletionHandler_, 0, b"v")

        self.assertArgIsBlock(
            AppKit.NSAnimationContext.runAnimationGroup_completionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            AppKit.NSAnimationContext.runAnimationGroup_completionHandler_, 1, b"v"
        )

        self.assertResultIsBOOL(AppKit.NSAnimationContext.allowsImplicitAnimation)
        self.assertArgIsBOOL(AppKit.NSAnimationContext.setAllowsImplicitAnimation_, 0)
