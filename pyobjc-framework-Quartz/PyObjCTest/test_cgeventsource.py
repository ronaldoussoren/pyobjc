from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCGEventSource(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGEventSourceRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGEventSourceGetTypeID(), int)

        src = Quartz.CGEventSourceCreate(0)
        self.assertIsInstance(src, Quartz.CGEventSourceRef)

        v = Quartz.CGEventSourceGetKeyboardType(src)
        self.assertIsInstance(v, int)

        Quartz.CGEventSourceSetKeyboardType(src, v)

        Quartz.CGEventSourceSetPixelsPerLine(src, 23)
        v = Quartz.CGEventSourceGetPixelsPerLine(src)
        self.assertIsInstance(v, float)
        self.assertEqual(v, 23)

        v = Quartz.CGEventSourceGetSourceStateID(src)
        self.assertIsInstance(v, int)

        self.assertResultHasType(Quartz.CGEventSourceButtonState, objc._C_BOOL)
        v = Quartz.CGEventSourceButtonState(0, 0)
        self.assertIsInstance(v, bool)

        self.assertResultHasType(Quartz.CGEventSourceKeyState, objc._C_BOOL)
        v = Quartz.CGEventSourceKeyState(0, 64)
        self.assertIsInstance(v, bool)

        v = Quartz.CGEventSourceFlagsState(0)
        self.assertIsInstance(v, int)

        v = Quartz.CGEventSourceSecondsSinceLastEventType(
            0, Quartz.kCGEventLeftMouseDown
        )
        self.assertIsInstance(v, float)

        v = Quartz.CGEventSourceCounterForEventType(0, Quartz.kCGEventLeftMouseDown)
        self.assertIsInstance(v, int)

        Quartz.CGEventSourceSetUserData(src, 0xABBCCDD00112233)
        v = Quartz.CGEventSourceGetUserData(src)
        self.assertIsInstance(v, int)
        self.assertEqual(v, 0xABBCCDD00112233)

        Quartz.CGEventSourceSetLocalEventsFilterDuringSuppressionState(
            src,
            Quartz.kCGEventFlagMaskControl | Quartz.kCGEventFlagMaskCommand,
            Quartz.kCGEventSuppressionStateRemoteMouseDrag,
        )

        m = Quartz.CGEventSourceGetLocalEventsFilterDuringSuppressionState(
            src, Quartz.kCGEventSuppressionStateRemoteMouseDrag
        )
        self.assertIsInstance(m, int)

        Quartz.CGEventSourceSetLocalEventsSuppressionInterval(src, 1.5)
        v = Quartz.CGEventSourceGetLocalEventsSuppressionInterval(src)
        self.assertEqual(v, 1.5)
