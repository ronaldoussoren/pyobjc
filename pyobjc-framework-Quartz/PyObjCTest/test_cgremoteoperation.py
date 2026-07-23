from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz
import objc
import warnings


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

        err = Quartz.CGRegisterScreenRefreshCallback(callbackRefresh, myInfo)
        self.assertEqual(err, 0)

        # FIXME: should force a refresh here

        Quartz.CGUnregisterScreenRefreshCallback(callbackRefresh, myInfo)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 3"):
            Quartz.CGWaitForScreenRefreshRects(None, None, None)

        with self.assertRaisesRegex(ValueError, "'pRectArray' must be None"):
            Quartz.CGWaitForScreenRefreshRects(42, None)

        with self.assertRaisesRegex(ValueError, "'pCount' must be None"):
            Quartz.CGWaitForScreenRefreshRects(None, 42)

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning,
                "leaving out 'pRectArray' and 'pCount' is deprecated",
            ):
                Quartz.CGWaitForScreenRefreshRects()

        # FIXME: This complete hangs the interpreter, don't have
        # time to investigate this.
        #    Quartz.CGWaitForScreenRefreshRects(None, None)
        #

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            Quartz.CGWaitForScreenUpdateRects()

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGWaitForScreenUpdateRects("1", None, None, None, None)

        with self.assertRaisesRegex(ValueError, "currentOperation must be None"):
            Quartz.CGWaitForScreenUpdateRects(1, 42, None, None, None)

        with self.assertRaisesRegex(ValueError, "pRectArray must be None"):
            Quartz.CGWaitForScreenUpdateRects(1, None, 42, None, None)

        with self.assertRaisesRegex(ValueError, "pCount must be None"):
            Quartz.CGWaitForScreenUpdateRects(1, None, None, 42, None)

        with self.assertRaisesRegex(ValueError, "pDelta must be None"):
            Quartz.CGWaitForScreenUpdateRects(1, None, None, None, 42)

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning,
                "leaving out 'currentOperation', 'pRectArray', 'pCount' and 'pDelta' is deprecated",
            ):
                Quartz.CGWaitForScreenUpdateRects(1)

        # FIXME: This complete hangs the interpreter, don't have
        # time to investigate this.
        #    Quartz.CGWaitForScreenUpdateRect(1, None, None, None, None, None)

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
            "The rects returned by 'CGWaitForScreenRefreshRects' are released automaticly",
        ):
            Quartz.CGReleaseScreenRefreshRects()

        # The default metadata results in not actually calling the bindings therefore create
        # a copy of the function without this metadata.
        d = {}
        objc.loadBundleFunctions(
            None,
            d,
            [
                ("CGReleaseScreenRefreshRects", b"v^{CGRect={CGPoint=dd}{CGSize=dd}}"),
            ],
        )
        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            d["CGReleaseScreenRefreshRects"]()

        d["CGReleaseScreenRefreshRects"]([])

    @expectedFailure
    def test_blocks_forever(self):
        self.fail("Quartz.CGWaitForScreenRefreshRects")
        self.fail("Quartz.CGWaitForScreenUpdateRect")

    @expectedFailure
    def test_missing(self):
        self.fail("CGScreenRegisterMoveCallback")
        self.fail("CGScreenUnregisterMoveCallback")
