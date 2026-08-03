from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import ApplicationServices
import objc
import os


class TestCGEvent(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CGEventRef)
        self.assertIsCFType(Quartz.CGEventSourceRef)

    def test_event_functions(self):
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
    def test_functions10_11(self):
        Quartz.CGEventPostToPid

    def test_manual_cgeventtapcreate(self):
        lst = []
        context = object()

        def callback(proxy, tp, event, userInfo):
            lst.append((proxy, tp, event, userInfo))  # noqa: F821

        with self.assertRaisesRegex(TypeError, "expected 6 arguments, got 0"):
            Quartz.CGEventTapCreate()

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreate(
                "Quartz.kCGSessionEventTap",
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,
                "Quartz.kCGHeadInsertEventTap",
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,
                Quartz.kCGHeadInsertEventTap,
                "Quartz.kCGEventTapOptionListenOnly",
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                "Quartz.kCGEventMaskForAllEvents",
                callback,
                context,
            )

        with self.assertRaisesRegex(ValueError, "callback should be a callable"):
            Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                42,
                context,
            )

        tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.kCGEventMaskForAllEvents,
            callback,
            context,
        )
        self.assertIsInstance(tap, Quartz.CFMachPortRef)
        self.assertTrue(Quartz.CGEventTapIsEnabled(tap))

        rls = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
        rl = Quartz.CFRunLoopGetCurrent()
        Quartz.CFRunLoopAddSource(rl, rls, Quartz.kCFRunLoopDefaultMode)
        print("\nmove mouse")
        Quartz.CFRunLoopRunInMode(Quartz.kCFRunLoopDefaultMode, 1.0, False)
        saved_lst = lst
        del lst

        with self.assertRaisesRegex(NameError, "cannot access free variable 'lst'"):
            Quartz.CFRunLoopRunInMode(Quartz.kCFRunLoopDefaultMode, 1.0, False)
        Quartz.CFRunLoopRemoveSource(rl, rls, Quartz.kCFRunLoopDefaultMode)

        for entry in saved_lst:
            self.assertIsInstance(entry[0], Quartz.CGEventTapProxy)
            self.assertIsInstance(entry[1], int)
            self.assertIsInstance(entry[2], Quartz.CGEventRef)
            self.assertIs(entry[3], context)

    def test_manual_cgeventtapcreateforpid(self):
        context = object()

        def callback(proxy, tp, event, userInfo):
            pass

        with self.assertRaisesRegex(TypeError, "expected 6 arguments, got 0"):
            Quartz.CGEventTapCreateForPid()

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            Quartz.CGEventTapCreateForPid(
                "os.getpid()",
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreateForPid(
                os.getpid(),
                "Quartz.kCGHeadInsertEventTap",
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreateForPid(
                os.getpid(),
                Quartz.kCGHeadInsertEventTap,
                "Quartz.kCGEventTapOptionListenOnly",
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGEventTapCreateForPid(
                os.getpid(),
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                "Quartz.kCGEventMaskForAllEvents",
                callback,
                context,
            )

        with self.assertRaisesRegex(ValueError, "callback should be a callable"):
            Quartz.CGEventTapCreateForPid(
                os.getpid(),
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                42,
                context,
            )

        tap = Quartz.CGEventTapCreateForPid(
            os.getpid(),
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.kCGEventMaskForAllEvents,
            callback,
            context,
        )
        self.assertIsInstance(tap, Quartz.CFMachPortRef)
        self.assertTrue(Quartz.CGEventTapIsEnabled(tap))

    def test_manual_cgeventtapcreateforpsn(self):
        context = object()

        _, psn = ApplicationServices.GetCurrentProcess(None)

        def callback(proxy, tp, event, userInfo):
            pass

        with self.assertRaisesRegex(TypeError, "expected 6 arguments, got 0"):
            Quartz.CGEventTapCreateForPSN()

        with self.assertRaisesRegex(
            TypeError, "depythonifying struct, got no sequence"
        ):
            Quartz.CGEventTapCreateForPSN(
                42,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreateForPSN(
                psn,
                "Quartz.kCGHeadInsertEventTap",
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGEventTapCreateForPSN(
                psn,
                Quartz.kCGHeadInsertEventTap,
                "Quartz.kCGEventTapOptionListenOnly",
                Quartz.kCGEventMaskForAllEvents,
                callback,
                context,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGEventTapCreateForPSN(
                psn,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                "Quartz.kCGEventMaskForAllEvents",
                callback,
                context,
            )

        with self.assertRaisesRegex(ValueError, "callback should be a callable"):
            Quartz.CGEventTapCreateForPSN(
                psn,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionListenOnly,
                Quartz.kCGEventMaskForAllEvents,
                42,
                context,
            )

        tap = Quartz.CGEventTapCreateForPSN(
            psn,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.kCGEventMaskForAllEvents,
            callback,
            context,
        )
        self.assertIsInstance(tap, Quartz.CFMachPortRef)
        self.assertTrue(Quartz.CGEventTapIsEnabled(tap))

    def test_functions(self):
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
    def test_functions10_13(self):
        Quartz.CGEventCreateScrollWheelEvent2

    @min_os_level("11.0")
    def test_functions10_15(self):
        Quartz.CGPreflightListenEventAccess
        Quartz.CGRequestListenEventAccess
        Quartz.CGPreflightPostEventAccess
        Quartz.CGRequestPostEventAccess
