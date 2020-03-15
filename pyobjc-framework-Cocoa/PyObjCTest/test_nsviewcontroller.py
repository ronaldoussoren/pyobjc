import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSViewController(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsSEL(
            AppKit.NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_,
            2,
            b"^v",
        )

        self.assertResultIsBOOL(AppKit.NSViewController.commitEditing)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSViewController.isViewLoaded)

        self.assertArgIsBlock(
            AppKit.NSViewController.transitionFromViewController_toViewController_options_completionHandler_,  # noqa: B950
            3,
            b"v",
        )

    @min_os_level("10.10")
    def testProtocols10_10(self):
        objc.protocolNamed("NSViewControllerPresentationAnimator")

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NSViewControllerTransitionNone, 0x0)
        self.assertEqual(AppKit.NSViewControllerTransitionCrossfade, 0x1)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideUp, 0x10)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideDown, 0x20)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideLeft, 0x40)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideRight, 0x80)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideForward, 0x140)
        self.assertEqual(AppKit.NSViewControllerTransitionSlideBackward, 0x180)
        self.assertEqual(AppKit.NSViewControllerTransitionAllowUserInteraction, 0x1000)
