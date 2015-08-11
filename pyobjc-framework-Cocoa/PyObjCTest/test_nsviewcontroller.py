from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSViewController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsSEL(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 1, b'v@:@'+objc._C_NSBOOL + b'^v')
        self.assertArgHasType(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 2, b'^v')

        self.assertResultIsBOOL(NSViewController.commitEditing)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSViewController.isViewLoaded)

        self.assertArgIsBlock(NSViewController.transitionFromViewController_toViewController_options_completionHandler_, 3, b'v')

    @min_os_level('10.10')
    def testProtocols10_10(self):
        objc.protocolNamed('NSViewControllerPresentationAnimator')

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSViewControllerTransitionNone, 0x0)
        self.assertEqual(NSViewControllerTransitionCrossfade, 0x1)
        self.assertEqual(NSViewControllerTransitionSlideUp, 0x10)
        self.assertEqual(NSViewControllerTransitionSlideDown, 0x20)
        self.assertEqual(NSViewControllerTransitionSlideLeft, 0x40)
        self.assertEqual(NSViewControllerTransitionSlideRight, 0x80)
        self.assertEqual(NSViewControllerTransitionSlideForward, 0x140)
        self.assertEqual(NSViewControllerTransitionSlideBackward, 0x180)
        self.assertEqual(NSViewControllerTransitionAllowUserInteraction, 0x1000)


if __name__ == "__main__":
    main()
