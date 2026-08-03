from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCGRemoteOperation(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.CGEventNoErr, Quartz.kCGErrorSuccess)

        self.assertEqual(Quartz.kCGScreenUpdateOperationRefresh, 0)
        self.assertEqual(Quartz.kCGScreenUpdateOperationMove, (1 << 0))
        self.assertEqual(
            Quartz.kCGScreenUpdateOperationReducedDirtyRectangleCount, (1 << 31)
        )

        self.assertEqual(Quartz.kCGEventFilterMaskPermitLocalMouseEvents, 1)
        self.assertEqual(Quartz.kCGEventFilterMaskPermitLocalKeyboardEvents, 2)
        self.assertEqual(Quartz.kCGEventFilterMaskPermitSystemDefinedEvents, 4)
        self.assertEqual(Quartz.kCGEventFilterMaskPermitAllEvents, 7)

        self.assertEqual(Quartz.kCGEventSuppressionStateSuppressionInterval, 0)
        self.assertEqual(Quartz.kCGEventSuppressionStateRemoteMouseDrag, 1)
        self.assertEqual(Quartz.kCGNumberOfEventSuppressionStates, 2)

        self.assertEqual(Quartz.kCGMouseDownEventMaskingDeadSwitchTimeout, 60.0)

        self.assertEqual(
            Quartz.kCGEventSupressionStateSupressionInterval,
            Quartz.kCGEventSuppressionStateSuppressionInterval,
        )
        self.assertEqual(
            Quartz.kCGEventSupressionStateRemoteMouseDrag,
            Quartz.kCGEventSuppressionStateRemoteMouseDrag,
        )
        self.assertEqual(
            Quartz.kCGNumberOfEventSupressionStates,
            Quartz.kCGNumberOfEventSuppressionStates,
        )

    def test_structs(self):
        v = Quartz.CGScreenUpdateMoveDelta()
        self.assertTrue(hasattr(v, "dX"))
        self.assertTrue(hasattr(v, "dY"))
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        myInfo = object()
        callcount = [0]

        def callbackRefresh(count, rects, info):
            self.assertTrue(info is myInfo)
            self.assertIsInstance(rects, tuple)
            self.assertIsInstance(count, int)
            for i in rects:
                self.assertIsInstance(i, Quartz.CGRect)
            callcount[0] += 1

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            Quartz.CGRegisterScreenRefreshCallback()
        with self.assertRaisesRegex(TypeError, "callback not callable"):
            Quartz.CGRegisterScreenRefreshCallback(42, myInfo)

        err = Quartz.CGRegisterScreenRefreshCallback(callbackRefresh, myInfo)
        self.assertEqual(err, 0)

        # FIXME: should force a refresh here

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            Quartz.CGUnregisterScreenRefreshCallback()
        with self.assertRaisesRegex(ValueError, "Cannot find callback info"):
            Quartz.CGUnregisterScreenRefreshCallback(1, 2)
        Quartz.CGUnregisterScreenRefreshCallback(callbackRefresh, myInfo)

        v = Quartz.CGCursorIsVisible()
        self.assertIsInstance(v, int)

        v = Quartz.CGCursorIsDrawnInFramebuffer()
        self.assertIsInstance(v, int)

        v = Quartz.CGPostMouseEvent((50, 50), True, 3, 0, 0, 0)
        self.assertEqual(v, 0)

        v = Quartz.CGPostScrollWheelEvent(3, 0, 0, 0)
        self.assertEqual(v, 0)

        v = Quartz.CGPostKeyboardEvent(0, 56, 1)
        self.assertEqual(v, 0)

        v = Quartz.CGWarpMouseCursorPosition((800, 800))
        self.assertEqual(v, 0)

        v = Quartz.CGInhibitLocalEvents(False)
        self.assertEqual(v, 0)

        v = Quartz.CGSetLocalEventsSuppressionInterval(0.1)
        self.assertEqual(v, 0)

        v = Quartz.CGEnableEventStateCombining(0)
        self.assertEqual(v, 0)

        v = Quartz.CGSetLocalEventsFilterDuringSuppressionState(
            Quartz.kCGEventFilterMaskPermitAllEvents,
            Quartz.kCGEventSuppressionStateSuppressionInterval,
        )
        self.assertEqual(v, 0)

        v = Quartz.CGAssociateMouseAndMouseCursorPosition(0)
        self.assertEqual(v, 0)

        # For some reason there are 2 NSMachPort classes on OSX 10.8
        classes = tuple(
            cls for cls in objc.getClassList() if cls.__name__ == "NSMachPort"
        )

        v = Quartz.CGWindowServerCFMachPort()
        self.assertIsInstance(v, classes)

        self.assertTrue(
            Quartz.CGSetLocalEventsFilterDuringSupressionState
            is Quartz.CGSetLocalEventsFilterDuringSuppressionState
        )

        self.assertResultIsCFRetained(Quartz.CGWindowServerCreateServerPort)

        with self.assertRaisesRegex(
            TypeError,
            "function is not functional since macOS 10.8",
        ):
            Quartz.CGReleaseScreenRefreshRects()

        with self.assertRaisesRegex(
            TypeError,
            "function is not functional since macOS 10.8",
        ):
            Quartz.CGWaitForScreenRefreshRects(None, None)

        with self.assertRaisesRegex(
            TypeError,
            "function is not functional since macOS 10.8",
        ):
            Quartz.CGWaitForScreenUpdateRects(None, None)

        with self.assertRaisesRegex(
            TypeError,
            "function is not supported",
        ):
            Quartz.CGScreenRegisterMoveCallback()

        with self.assertRaisesRegex(
            TypeError,
            "function is not supported",
        ):
            Quartz.CGScreenUnregisterMoveCallback()
