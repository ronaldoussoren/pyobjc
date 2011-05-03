
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGEvent (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGEventRef)
        self.assertIsCFType(CGEventSourceRef)

    def testEventFunctions(self):
        evt = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (80, 90), kCGMouseButtonLeft)
        self.assertIsInstance(evt, CGEventRef)

        self.assertResultIsCFRetained(CGEventCreateSourceFromEvent)
        v = CGEventCreateSourceFromEvent(evt)
        self.assertIsInstance(v, CGEventSourceRef)

        src = CGEventSourceCreate(kCGEventSourceStateCombinedSessionState)
        self.assertIsInstance(src, CGEventSourceRef)

        CGEventSetSource(evt, src)

        t = CGEventGetType(evt)
        self.assertIsInstance(t, (int, long))
        self.assertEqual(t, kCGEventLeftMouseDown)

        CGEventSetType(evt, kCGEventOtherMouseUp)
        t = CGEventGetType(evt)
        self.assertEqual(t, kCGEventOtherMouseUp)

        v = CGEventGetTimestamp(evt)
        self.assertIsInstance(v, (int, long))

        CGEventSetTimestamp(evt, 99)
        v = CGEventGetTimestamp(evt)
        self.assertEqual(v, 99)

        v = CGEventGetLocation(evt)
        self.assertIsInstance(v, CGPoint)

        CGEventSetLocation(evt, (99, 99))
        v = CGEventGetLocation(evt)
        self.assertEqual(v, (99, 99))

        v = CGEventGetFlags(evt)
        self.assertIsInstance(v, (int, long))

        CGEventSetFlags(evt, 99)
        v = CGEventGetFlags(evt)
        self.assertEqual(v, 99)

        v = CGEventGetIntegerValueField(evt, kCGMouseEventNumber)
        self.assertIsInstance(v, (int, long))

        CGEventSetIntegerValueField(evt, kCGMouseEventNumber, 99)
        v = CGEventGetIntegerValueField(evt, kCGMouseEventNumber)
        self.assertEqual(v, 99)

        v = CGEventGetDoubleValueField(evt, kCGMouseEventPressure)
        self.assertIsInstance(v, float)

        CGEventSetDoubleValueField(evt, kCGMouseEventPressure, 42.5)

        self.assertArgHasType(CGEventTapEnable, 0, '^{__CFMachPort=}')
        self.assertArgHasType(CGEventTapEnable, 1, objc._C_BOOL)

        self.assertResultHasType(CGEventTapIsEnabled, objc._C_BOOL)
        self.assertArgHasType(CGEventTapIsEnabled, 0, '^{__CFMachPort=}')

        self.assertArgHasType(CGEventTapPostEvent, 0, '^{__CGEventTapProxy=}')
        self.assertArgHasType(CGEventTapPostEvent, 1, '^{__CGEvent=}')

        self.assertResultHasType(CGGetEventTapList, objc._C_INT)
        self.assertArgHasType(CGGetEventTapList, 0, objc._C_UINT)
        self.assertArgHasType(CGGetEventTapList, 1, 'o^' + CGEventTapInformation.__typestr__)
        self.assertArgSizeInArg(CGGetEventTapList, 1, (0, 2))
        self.assertArgHasType(CGGetEventTapList, 2, 'o^' + objc._C_UINT)

        self.assertResultHasType(CGEventPost, objc._C_VOID)
        self.assertArgHasType(CGEventPost, 0, objc._C_UINT)
        self.assertArgHasType(CGEventPost, 1, '^{__CGEvent=}')

        self.assertResultHasType(CGEventPostToPSN, objc._C_VOID)
        self.assertArgHasType(CGEventPostToPSN, 0, 'n^{ProcessSerialNumber=II}')
        self.assertArgHasType(CGEventPostToPSN, 1, '^{__CGEvent=}')


    @expectedFailure
    def testMissing(self):
        self.fail("CGEventTapCreateForPSN")


    def testFunctions(self):
        self.assertIsInstance(CGEventGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CGEventCreate)
        evt = CGEventCreate(None)
        self.assertIsInstance(evt, CGEventRef)

        self.assertResultIsCFRetained(CGEventCreateData)
        dta = CGEventCreateData(None, evt)
        self.assertIsInstance(dta, CFDataRef)

        self.assertResultIsCFRetained(CGEventCreateFromData)
        v = CGEventCreateFromData(None, dta)
        self.assertIsInstance(v, CGEventRef)

        self.assertResultIsCFRetained(CGEventCreateMouseEvent)
        evt = CGEventCreateMouseEvent(None, kCGEventOtherMouseDown, (0, 0), 2)
        self.assertIsInstance(evt, CGEventRef)

        self.assertResultIsCFRetained(CGEventCreateKeyboardEvent)
        self.assertArgHasType(CGEventCreateKeyboardEvent, 2, objc._C_BOOL)
        evt = CGEventCreateKeyboardEvent(None, 45, False)
        self.assertIsInstance(evt, CGEventRef)


        v = CGEventCreateCopy(evt)
        self.assertIsInstance(v, CGEventRef)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        self.assertResultIsCFRetained(CGEventCreateScrollWheelEvent)
        evt = CGEventCreateScrollWheelEvent(None, kCGScrollEventUnitPixel, 2, 99, 44)
        self.assertIsInstance(evt, CGEventRef)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99, 100, 101)
        
        v = CGEventGetUnflippedLocation(evt)
        self.assertIsInstance(v, CGPoint)

if __name__ == "__main__":
    main()
