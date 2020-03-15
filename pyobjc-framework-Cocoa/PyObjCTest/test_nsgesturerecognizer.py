import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSGestureRecognizerHelper(AppKit.NSObject):
    def gestureRecognizerShouldBegin_(self, g):
        return 1

    def gestureRecognizer_shouldRecognizeSimultaneouslyWithGestureRecognizer_(
        self, g, a
    ):
        return 1

    def gestureRecognizer_shouldRequireFailureOfGestureRecognizer_(self, g, a):
        return 1

    def gestureRecognizer_shouldBeRequiredToFailByGestureRecognizer_(self, g, a):
        return 1

    def gestureRecognizer_shouldAttemptToRecognizeWithEvent_(self, g, e):
        return 1

    def gestureRecognizer_shouldReceiveTouch_(self, r, t):
        return 1


class TestNSGestureRecognizer(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSGestureRecognizerStatePossible, 0)
        self.assertEqual(AppKit.NSGestureRecognizerStateBegan, 1)
        self.assertEqual(AppKit.NSGestureRecognizerStateChanged, 2)
        self.assertEqual(AppKit.NSGestureRecognizerStateEnded, 3)
        self.assertEqual(AppKit.NSGestureRecognizerStateCancelled, 4)
        self.assertEqual(AppKit.NSGestureRecognizerStateFailed, 5)
        self.assertEqual(
            AppKit.NSGestureRecognizerStateRecognized,
            AppKit.NSGestureRecognizerStateEnded,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsSEL(
            AppKit.NSGestureRecognizer.initWithTarget_action_, 1, b"v@:@"
        )
        self.assertArgIsSEL(AppKit.NSGestureRecognizer.setAction_, 0, b"v@:@")
        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.isEnabled)
        self.assertArgIsBOOL(AppKit.NSGestureRecognizer.setEnabled_, 0)

        self.assertResultIsBOOL(
            AppKit.NSGestureRecognizer.delaysPrimaryMouseButtonEvents
        )
        self.assertResultIsBOOL(
            AppKit.NSGestureRecognizer.delaysSecondaryMouseButtonEvents
        )
        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.delaysOtherMouseButtonEvents)
        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.delaysKeyEvents)
        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.delaysMagnificationEvents)
        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.delaysRotationEvents)

        self.assertArgIsBOOL(
            AppKit.NSGestureRecognizer.setDelaysPrimaryMouseButtonEvents_, 0
        )
        self.assertArgIsBOOL(
            AppKit.NSGestureRecognizer.setDelaysSecondaryMouseButtonEvents_, 0
        )
        self.assertArgIsBOOL(
            AppKit.NSGestureRecognizer.setDelaysOtherMouseButtonEvents_, 0
        )
        self.assertArgIsBOOL(AppKit.NSGestureRecognizer.setDelaysKeyEvents_, 0)
        self.assertArgIsBOOL(
            AppKit.NSGestureRecognizer.setDelaysMagnificationEvents_, 0
        )
        self.assertArgIsBOOL(AppKit.NSGestureRecognizer.setDelaysRotationEvents_, 0)

        self.assertResultIsBOOL(AppKit.NSGestureRecognizer.canPreventGestureRecognizer_)
        self.assertResultIsBOOL(
            AppKit.NSGestureRecognizer.canBePreventedByGestureRecognizer_
        )
        self.assertResultIsBOOL(
            AppKit.NSGestureRecognizer.shouldRequireFailureOfGestureRecognizer_
        )
        self.assertResultIsBOOL(
            AppKit.NSGestureRecognizer.shouldBeRequiredToFailByGestureRecognizer_
        )

    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("NSGestureRecognizerDelegate")
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizerShouldBegin_
        )
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizer_shouldRecognizeSimultaneouslyWithGestureRecognizer_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizer_shouldRequireFailureOfGestureRecognizer_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizer_shouldBeRequiredToFailByGestureRecognizer_  # noqa: B950
        )

    @min_sdk_level("10.11")
    def testProtocols10_11(self):
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizer_shouldAttemptToRecognizeWithEvent_
        )

    @min_sdk_level("10.12")
    def testProtocols10_12(self):
        self.assertResultIsBOOL(
            TestNSGestureRecognizerHelper.gestureRecognizer_shouldReceiveTouch_
        )
