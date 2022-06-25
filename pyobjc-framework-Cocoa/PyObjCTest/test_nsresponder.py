import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSResponder(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSResponder.tryToPerform_with_)
        self.assertResultIsBOOL(AppKit.NSResponder.performKeyEquivalent_)
        self.assertResultIsBOOL(AppKit.NSResponder.acceptsFirstResponder)
        self.assertResultIsBOOL(AppKit.NSResponder.becomeFirstResponder)
        self.assertResultIsBOOL(AppKit.NSResponder.resignFirstResponder)
        self.assertResultIsBOOL(AppKit.NSResponder.shouldBeTreatedAsInkEvent_)
        self.assertResultIsBOOL(AppKit.NSResponder.performMnemonic_)
        self.assertArgIsSEL(AppKit.NSResponder.doCommandBySelector_, 0, b"v@:@")

        self.assertArgIsSEL(
            AppKit.NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSResponder.presentError_)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            AppKit.NSResponder.wantsScrollEventsForSwipeTrackingOnAxis_
        )
        self.assertResultIsBOOL(AppKit.NSResponder.wantsForwardedScrollEventsForAxis_)
        self.assertArgIsSEL(
            AppKit.NSResponder.supplementalTargetForAction_sender_, 0, b"v@:@"
        )
        self.assertResultIsBOOL(
            AppKit.NSResponder.validateProposedFirstResponder_forEvent_
        )

    @min_sdk_level("10.14")
    def testProtocols(self):
        self.assertProtocolExists("NSStandardKeyBindingResponding")
