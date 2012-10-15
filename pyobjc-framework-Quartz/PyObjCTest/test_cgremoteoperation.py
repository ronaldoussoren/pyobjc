
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

try:
    long
except NameError:
    long = int

class TestCGRemoteOperation (TestCase):
    def testConstants(self):
        self.assertEqual(CGEventNoErr, kCGErrorSuccess)

        self.assertEqual(kCGScreenUpdateOperationRefresh, 0)
        self.assertEqual(kCGScreenUpdateOperationMove, (1 << 0))
        self.assertEqual(kCGScreenUpdateOperationReducedDirtyRectangleCount, (1 << 31))

        self.assertEqual(kCGEventFilterMaskPermitLocalMouseEvents, 1)
        self.assertEqual(kCGEventFilterMaskPermitLocalKeyboardEvents, 2)
        self.assertEqual(kCGEventFilterMaskPermitSystemDefinedEvents, 4)
        self.assertEqual(kCGEventFilterMaskPermitAllEvents, 7)

        self.assertEqual(kCGEventSuppressionStateSuppressionInterval, 0)
        self.assertEqual(kCGEventSuppressionStateRemoteMouseDrag, 1)
        self.assertEqual(kCGNumberOfEventSuppressionStates, 2)

        self.assertEqual(kCGMouseDownEventMaskingDeadSwitchTimeout, 60.0)

        self.assertEqual(kCGEventSupressionStateSupressionInterval, kCGEventSuppressionStateSuppressionInterval)
        self.assertEqual(kCGEventSupressionStateRemoteMouseDrag, kCGEventSuppressionStateRemoteMouseDrag)
        self.assertEqual(kCGNumberOfEventSupressionStates, kCGNumberOfEventSuppressionStates)

    def testStructs(self):
        v = CGScreenUpdateMoveDelta()
        self.assertTrue(hasattr(v, 'dX'))
        self.assertTrue(hasattr(v, 'dY'))




    def testFunctions(self):
        myInfo = object()
        callcount = [0]
        def callbackRefresh(count, rects, info):
            self.assertTrue(info is myInfo)
            self.assertIsInstance(rects, tuple)
            self.assertIsInstance(count, (int, long))
            for i in rects:
                self.assertIsInstance(i, CGRect)
            callcount[0] += 1

        err = CGRegisterScreenRefreshCallback(callbackRefresh, myInfo)
        self.assertEqual(err, 0)

        # FIXME: should force a refresh here

        CGUnregisterScreenRefreshCallback(callbackRefresh, myInfo)

        # FIXME: This complete hangs the interpreter, don't have
        # time to investigate this.
        #
        #err, rects, count = CGWaitForScreenRefreshRects(None, None)
        #self.assertEqual(err, 0)
        #self.assertIsInstance(rects, tuple)
        #self.assertIsInstance(count, (int, long))
        #for i in rects:
        #    self.assertIsInstance(i, CGRect)

        v = CGCursorIsVisible()
        self.assertIsInstance(v, (int, long))

        v = CGCursorIsDrawnInFramebuffer()
        self.assertIsInstance(v, (int, long))

        v = CGPostMouseEvent((50, 50), True, 3, 0, 0, 0)
        self.assertEqual(v, 0)

        v = CGPostScrollWheelEvent(3, 0, 0, 0)
        self.assertEqual(v, 0)

        v = CGPostKeyboardEvent(0, 56, 1)
        self.assertEqual(v, 0)

        v = CGWarpMouseCursorPosition((800, 800))
        self.assertEqual(v, 0)

        v = CGInhibitLocalEvents(False)
        self.assertEqual(v, 0)

        v = CGSetLocalEventsSuppressionInterval(0.1)
        self.assertEqual(v, 0)

        v = CGEnableEventStateCombining(0)
        self.assertEqual(v, 0)

        v  = CGSetLocalEventsFilterDuringSuppressionState(kCGEventFilterMaskPermitAllEvents, kCGEventSuppressionStateSuppressionInterval)
        self.assertEqual(v, 0)

        v = CGAssociateMouseAndMouseCursorPosition(0)
        self.assertEqual(v, 0)

        # For some reason there are 2 NSMachPort classes on OSX 10.8
        classes = tuple([cls for cls in objc.getClassList() if cls.__name__ == 'NSMachPort'])

        v = CGWindowServerCFMachPort()
        self.assertIsInstance(v, classes)

        self.assertTrue(CGSetLocalEventsFilterDuringSupressionState is CGSetLocalEventsFilterDuringSuppressionState)

    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(CGWindowServerCreateServerPort)

    @expectedFailure
    def testMissing(self):

        self.fail("CGWaitForScreenUpdateRects")
        self.fail("CGWaitForScreenRefreshRects")

if __name__ == "__main__":
    main()
