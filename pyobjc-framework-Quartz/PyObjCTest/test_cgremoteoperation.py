from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz
import objc


class TestCGRemoteOperation(TestCase):
    def testConstants(self):
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

    def testStructs(self):
        v = Quartz.CGScreenUpdateMoveDelta()
        self.assertTrue(hasattr(v, "dX"))
        self.assertTrue(hasattr(v, "dY"))
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
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

        # FIXME: This complete hangs the interpreter, don't have
        # time to investigate this.
        #
        Quartz.CGWaitForScreenRefreshRects
        # err, rects, count = Quartz.CGWaitForScreenRefreshRects(None, None)
        # self.assertEqual(err, 0)
        # self.assertIsInstance(rects, tuple)
        # self.assertIsInstance(count, int)
        # for i in rects:
        #    self.assertIsInstance(i, Quartz.CGRect)

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

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(Quartz.CGWindowServerCreateServerPort)

    @expectedFailure
    def testMissing(self):

        self.fail("CGScreenRegisterMoveCallback")
        self.fail("CGScreenUnregisterMoveCallback")
        self.fail("CGReleaseScreenRefreshRects")
        self.fail("CGWaitForScreenUpdateRects")
        self.fail("CGWaitForScreenRefreshRects")
