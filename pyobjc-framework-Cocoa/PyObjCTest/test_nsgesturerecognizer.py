from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGestureRecognizerHelper (NSObject):
    def gestureRecognizerShouldBegin_(self, g): return 1
    def gestureRecognizer_shouldRecognizeSimultaneouslyWithGestureRecognizer_(self, g, a): return 1
    def gestureRecognizer_shouldRequireFailureOfGestureRecognizer_(self, g, a): return 1
    def gestureRecognizer_shouldBeRequiredToFailByGestureRecognizer_(self, g, a): return 1
    def gestureRecognizer_shouldAttemptToRecognizeWithEvent_(self, g, e): return 1
    def gestureRecognizer_shouldReceiveTouch_(self, r, t): return 1

class TestNSGestureRecognizer (TestCase):
    def testConstants(self):
        self.assertEqual(NSGestureRecognizerStatePossible, 0)
        self.assertEqual(NSGestureRecognizerStateBegan, 1)
        self.assertEqual(NSGestureRecognizerStateChanged, 2)
        self.assertEqual(NSGestureRecognizerStateEnded, 3)
        self.assertEqual(NSGestureRecognizerStateCancelled, 4)
        self.assertEqual(NSGestureRecognizerStateFailed, 5)
        self.assertEqual(NSGestureRecognizerStateRecognized, NSGestureRecognizerStateEnded)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsSEL(NSGestureRecognizer.initWithTarget_action_, 1, b'v@:@')
        self.assertArgIsSEL(NSGestureRecognizer.setAction_, 0, b'v@:@')
        self.assertResultIsBOOL(NSGestureRecognizer.isEnabled)
        self.assertArgIsBOOL(NSGestureRecognizer.setEnabled_, 0)

        self.assertResultIsBOOL(NSGestureRecognizer.delaysPrimaryMouseButtonEvents)
        self.assertResultIsBOOL(NSGestureRecognizer.delaysSecondaryMouseButtonEvents)
        self.assertResultIsBOOL(NSGestureRecognizer.delaysOtherMouseButtonEvents)
        self.assertResultIsBOOL(NSGestureRecognizer.delaysKeyEvents)
        self.assertResultIsBOOL(NSGestureRecognizer.delaysMagnificationEvents)
        self.assertResultIsBOOL(NSGestureRecognizer.delaysRotationEvents)

        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysPrimaryMouseButtonEvents_, 0)
        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysSecondaryMouseButtonEvents_, 0)
        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysOtherMouseButtonEvents_, 0)
        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysKeyEvents_, 0)
        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysMagnificationEvents_, 0)
        self.assertArgIsBOOL(NSGestureRecognizer.setDelaysRotationEvents_, 0)

        self.assertResultIsBOOL(NSGestureRecognizer.canPreventGestureRecognizer_)
        self.assertResultIsBOOL(NSGestureRecognizer.canBePreventedByGestureRecognizer_)
        self.assertResultIsBOOL(NSGestureRecognizer.shouldRequireFailureOfGestureRecognizer_)
        self.assertResultIsBOOL(NSGestureRecognizer.shouldBeRequiredToFailByGestureRecognizer_)

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSGestureRecognizerDelegate')
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizerShouldBegin_)
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizer_shouldRecognizeSimultaneouslyWithGestureRecognizer_)
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizer_shouldRequireFailureOfGestureRecognizer_)
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizer_shouldBeRequiredToFailByGestureRecognizer_)

    @min_sdk_level('10.11')
    def testProtocols10_11(self):
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizer_shouldAttemptToRecognizeWithEvent_)

    @min_sdk_level('10.12')
    def testProtocols10_12(self):
        self.assertResultIsBOOL(TestNSGestureRecognizerHelper.gestureRecognizer_shouldReceiveTouch_)


if __name__ == "__main__":
    main()
