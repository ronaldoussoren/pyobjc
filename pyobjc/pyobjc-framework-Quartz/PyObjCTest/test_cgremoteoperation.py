
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGRemoteOperation (TestCase):
    def testConstants(self):
        self.failUnlessEqual(CGEventNoErr, kCGErrorSuccess)

        self.failUnlessEqual(kCGScreenUpdateOperationRefresh, 0)
        self.failUnlessEqual(kCGScreenUpdateOperationMove, cast_int(1 << 0))
        self.failUnlessEqual(kCGScreenUpdateOperationReducedDirtyRectangleCount, cast_int(1 << 31))

        self.failUnlessEqual(kCGEventFilterMaskPermitLocalMouseEvents, 1)
        self.failUnlessEqual(kCGEventFilterMaskPermitLocalKeyboardEvents, 2)
        self.failUnlessEqual(kCGEventFilterMaskPermitSystemDefinedEvents, 4)
        self.failUnlessEqual(kCGEventFilterMaskPermitAllEvents, 7)

        self.failUnlessEqual(kCGEventSuppressionStateSuppressionInterval, 0)
        self.failUnlessEqual(kCGEventSuppressionStateRemoteMouseDrag, 1)
        self.failUnlessEqual(kCGNumberOfEventSuppressionStates, 2)

        self.failUnlessEqual(kCGMouseDownEventMaskingDeadSwitchTimeout, 60.0)

        self.failUnlessEqual(kCGEventSupressionStateSupressionInterval, kCGEventSuppressionStateSuppressionInterval)
        self.failUnlessEqual(kCGEventSupressionStateRemoteMouseDrag, kCGEventSuppressionStateRemoteMouseDrag)
        self.failUnlessEqual(kCGNumberOfEventSupressionStates, kCGNumberOfEventSuppressionStates)

    def testStructs(self):
        v = CGScreenUpdateMoveDelta()
        self.failUnless(hasattr(v, 'dX'))
        self.failUnless(hasattr(v, 'dY'))




    def testFunctions(self):
        myInfo = object()
        callcount = [0]
        def callbackRefresh(count, rects, info):
            self.failUnless(info is myInfo)
            self.failUnlessIsInstance(rects, tuple)
            self.failUnlessIsInstance(count, (int, long))
            for i in rects:
                self.failUnlessIsInstance(i, CGRect)
            callcount[0] += 1

        err = CGRegisterScreenRefreshCallback(callbackRefresh, myInfo)
        self.failUnlessEqual(err, 0)

        # FIXME: should force a refresh here

        CGUnregisterScreenRefreshCallback(callbackRefresh, myInfo)

        # FIXME: This complete hangs the interpreter, don't have
        # time to investigate this.
        #
        #err, rects, count = CGWaitForScreenRefreshRects(None, None)
        #self.failUnlessEqual(err, 0)
        #self.failUnlessIsInstance(rects, tuple)
        #self.failUnlessIsInstance(count, (int, long))
        #for i in rects:
        #    self.failUnlessIsInstance(i, CGRect)

        v = CGCursorIsVisible()
        self.failUnlessIsInstance(v, (int, long))

        v = CGCursorIsDrawnInFramebuffer()
        self.failUnlessIsInstance(v, (int, long))

        v = CGPostMouseEvent((50, 50), True, 3, 0, 0, 0)
        self.failUnlessEqual(v, 0)

        v = CGPostScrollWheelEvent(3, 0, 0, 0)
        self.failUnlessEqual(v, 0)

        v = CGPostKeyboardEvent(0, 56, 1)
        self.failUnlessEqual(v, 0)

        v = CGWarpMouseCursorPosition((800, 800))
        self.failUnlessEqual(v, 0)

        v = CGInhibitLocalEvents(False)
        self.failUnlessEqual(v, 0)

        v = CGSetLocalEventsSuppressionInterval(0.1)
        self.failUnlessEqual(v, 0)

        v = CGEnableEventStateCombining(0)
        self.failUnlessEqual(v, 0)

        v  = CGSetLocalEventsFilterDuringSuppressionState(kCGEventFilterMaskPermitAllEvents, kCGEventSuppressionStateSuppressionInterval)
        self.failUnlessEqual(v, 0)

        v = CGAssociateMouseAndMouseCursorPosition(0)
        self.failUnlessEqual(v, 0)

        v = CGWindowServerCFMachPort()
        self.failUnlessIsInstance(v, CFMachPortRef)

        self.failUnless(CGSetLocalEventsFilterDuringSupressionState is CGSetLocalEventsFilterDuringSuppressionState)


    def testMissing(self):
        self.fail("CGWaitForScreenUpdateRects")
        self.fail("CGWaitForScreenRefreshRects")

if __name__ == "__main__":
    main()
