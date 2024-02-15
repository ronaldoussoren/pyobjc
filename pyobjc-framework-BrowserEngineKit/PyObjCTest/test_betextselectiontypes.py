import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBETextSelectionTypes(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BrowserEngineKit.BEGestureType)
        self.assertEqual(BrowserEngineKit.BEGestureTypeLoupe, 0)
        self.assertEqual(BrowserEngineKit.BEGestureTypeOneFingerTap, 1)
        self.assertEqual(BrowserEngineKit.BEGestureTypeDoubleTapAndHold, 2)
        self.assertEqual(BrowserEngineKit.BEGestureTypeDoubleTap, 3)
        self.assertEqual(BrowserEngineKit.BEGestureTypeOneFingerDoubleTap, 8)
        self.assertEqual(BrowserEngineKit.BEGestureTypeOneFingerTripleTap, 9)
        self.assertEqual(BrowserEngineKit.BEGestureTypeTwoFingerSingleTap, 10)
        self.assertEqual(BrowserEngineKit.BEGestureTypeTwoFingerRangedSelectGesture, 11)
        self.assertEqual(BrowserEngineKit.BEGestureTypeIMPhraseBoundaryDrag, 14)
        self.assertEqual(BrowserEngineKit.BEGestureTypeForceTouch, 15)

        self.assertIsEnumType(BrowserEngineKit.BESelectionTouchPhase)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseStarted, 0)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseMoved, 1)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseEnded, 2)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseEndedMovingForward, 3)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseEndedMovingBackward, 4)
        self.assertEqual(BrowserEngineKit.BESelectionTouchPhaseEndedNotMoving, 5)

        self.assertIsEnumType(BrowserEngineKit.BESelectionFlags)
        self.assertEqual(BrowserEngineKit.BESelectionFlagsNone, 0)
        self.assertEqual(BrowserEngineKit.BEWordIsNearTap, 1 << 0)
        self.assertEqual(BrowserEngineKit.BESelectionFlipped, 1 << 1)
        self.assertEqual(BrowserEngineKit.BEPhraseBoundaryChanged, 1 << 2)
