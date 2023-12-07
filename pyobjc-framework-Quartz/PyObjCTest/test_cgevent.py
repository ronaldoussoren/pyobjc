from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz
import objc


class TestCGEvent(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGEventRef)
        self.assertIsCFType(Quartz.CGEventSourceRef)

    def testEventFunctions(self):
        evt = Quartz.CGEventCreateMouseEvent(
            None, Quartz.kCGEventLeftMouseDown, (80, 90), Quartz.kCGMouseButtonLeft
        )
        self.assertIsInstance(evt, Quartz.CGEventRef)

        self.assertResultIsCFRetained(Quartz.CGEventCreateSourceFromEvent)
        v = Quartz.CGEventCreateSourceFromEvent(evt)
        self.assertIsInstance(v, Quartz.CGEventSourceRef)

        src = Quartz.CGEventSourceCreate(Quartz.kCGEventSourceStateCombinedSessionState)
        self.assertIsInstance(src, Quartz.CGEventSourceRef)

        Quartz.CGEventSetSource(evt, src)

        t = Quartz.CGEventGetType(evt)
        self.assertIsInstance(t, int)
        self.assertEqual(t, Quartz.kCGEventLeftMouseDown)

        Quartz.CGEventSetType(evt, Quartz.kCGEventOtherMouseUp)
        t = Quartz.CGEventGetType(evt)
        self.assertEqual(t, Quartz.kCGEventOtherMouseUp)

        v = Quartz.CGEventGetTimestamp(evt)
        self.assertIsInstance(v, int)

        Quartz.CGEventSetTimestamp(evt, 99)
        v = Quartz.CGEventGetTimestamp(evt)
        self.assertEqual(v, 99)

        v = Quartz.CGEventGetLocation(evt)
        self.assertIsInstance(v, Quartz.CGPoint)

        Quartz.CGEventSetLocation(evt, (99, 99))
        v = Quartz.CGEventGetLocation(evt)
        self.assertEqual(v, (99, 99))

        v = Quartz.CGEventGetFlags(evt)
        self.assertIsInstance(v, int)

        Quartz.CGEventSetFlags(evt, 99)
        v = Quartz.CGEventGetFlags(evt)
        self.assertEqual(v, 99)

        v = Quartz.CGEventGetIntegerValueField(evt, Quartz.kCGMouseEventNumber)
        self.assertIsInstance(v, int)

        Quartz.CGEventSetIntegerValueField(evt, Quartz.kCGMouseEventNumber, 99)
        v = Quartz.CGEventGetIntegerValueField(evt, Quartz.kCGMouseEventNumber)
        self.assertEqual(v, 99)

        v = Quartz.CGEventGetDoubleValueField(evt, Quartz.kCGMouseEventPressure)
        self.assertIsInstance(v, float)

        Quartz.CGEventSetDoubleValueField(evt, Quartz.kCGMouseEventPressure, 42.5)

        self.assertArgHasType(Quartz.CGEventTapEnable, 0, b"^{__CFMachPort=}")
        self.assertArgHasType(Quartz.CGEventTapEnable, 1, objc._C_BOOL)

        self.assertResultHasType(Quartz.CGEventTapIsEnabled, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGEventTapIsEnabled, 0, b"^{__CFMachPort=}")

        self.assertArgHasType(Quartz.CGEventTapPostEvent, 0, b"^{__CGEventTapProxy=}")
        self.assertArgHasType(Quartz.CGEventTapPostEvent, 1, b"^{__CGEvent=}")

        self.assertResultHasType(Quartz.CGGetEventTapList, objc._C_INT)
        self.assertArgHasType(Quartz.CGGetEventTapList, 0, objc._C_UINT)
        self.assertArgHasType(
            Quartz.CGGetEventTapList,
            1,
            b"o^" + Quartz.CGEventTapInformation.__typestr__,
        )
        self.assertArgSizeInArg(Quartz.CGGetEventTapList, 1, (0, 2))
        self.assertArgHasType(Quartz.CGGetEventTapList, 2, b"o^" + objc._C_UINT)

        self.assertResultHasType(Quartz.CGEventPost, objc._C_VOID)
        self.assertArgHasType(Quartz.CGEventPost, 0, objc._C_UINT)
        self.assertArgHasType(Quartz.CGEventPost, 1, b"^{__CGEvent=}")

        self.assertResultHasType(Quartz.CGEventPostToPSN, objc._C_VOID)
        self.assertArgHasType(Quartz.CGEventPostToPSN, 0, b"n^{ProcessSerialNumber=II}")
        self.assertArgHasType(Quartz.CGEventPostToPSN, 1, b"^{__CGEvent=}")

    @min_os_level("10.11")
    def testFunctions10_11(self):
        Quartz.CGEventPostToPid

    @expectedFailure
    def testMissing(self):
        self.fail("CGEventTapCreateForPSN")
        self.fail("CGEventTapCreate")
        self.fail("CGEventTapCreateForPid")

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGEventGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGEventCreate)
        evt = Quartz.CGEventCreate(None)
        self.assertIsInstance(evt, Quartz.CGEventRef)

        self.assertResultIsCFRetained(Quartz.CGEventCreateData)
        dta = Quartz.CGEventCreateData(None, evt)
        self.assertIsInstance(dta, Quartz.CFDataRef)

        self.assertResultIsCFRetained(Quartz.CGEventCreateFromData)
        v = Quartz.CGEventCreateFromData(None, dta)
        self.assertIsInstance(v, Quartz.CGEventRef)

        self.assertResultIsCFRetained(Quartz.CGEventCreateMouseEvent)
        evt = Quartz.CGEventCreateMouseEvent(
            None, Quartz.kCGEventOtherMouseDown, (0, 0), 2
        )
        self.assertIsInstance(evt, Quartz.CGEventRef)

        self.assertResultIsCFRetained(Quartz.CGEventCreateKeyboardEvent)
        self.assertArgHasType(Quartz.CGEventCreateKeyboardEvent, 2, objc._C_BOOL)
        evt = Quartz.CGEventCreateKeyboardEvent(None, 45, False)
        self.assertIsInstance(evt, Quartz.CGEventRef)

        v = Quartz.CGEventCreateCopy(evt)
        self.assertIsInstance(v, Quartz.CGEventRef)

        s = "hello world"
        Quartz.CGEventKeyboardSetUnicodeString(evt, len(s), s)

        a, t = Quartz.CGEventKeyboardGetUnicodeString(evt, 50, None, None)
        self.assertEqual(a, len(s))
        self.assertEqual(s, t)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        self.assertResultIsCFRetained(Quartz.CGEventCreateScrollWheelEvent)
        evt = Quartz.CGEventCreateScrollWheelEvent(
            None, Quartz.kCGScrollEventUnitPixel, 2, 99, 44
        )
        self.assertIsInstance(evt, Quartz.CGEventRef)
        self.assertRaises(
            ValueError,
            Quartz.CGEventCreateScrollWheelEvent,
            Quartz.kCGScrollEventUnitPixel,
            40,
            2,
            99,
        )
        self.assertRaises(
            ValueError,
            Quartz.CGEventCreateScrollWheelEvent,
            Quartz.kCGScrollEventUnitPixel,
            40,
            2,
            99,
            100,
            101,
        )

        v = Quartz.CGEventGetUnflippedLocation(evt)
        self.assertIsInstance(v, Quartz.CGPoint)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGEventCreateScrollWheelEvent2

    @min_os_level("11.0")
    def testFunctions10_15(self):
        Quartz.CGPreflightListenEventAccess
        Quartz.CGRequestListenEventAccess
        Quartz.CGPreflightPostEventAccess
        Quartz.CGRequestPostEventAccess
