
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGEvent (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGEventRef)
        self.failUnlessIsCFType(CGEventSourceRef)

    def testMissing(self):
        evt = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (80, 90), kCGMouseButtonLeft)
        self.failUnlessIsInstance(evt, CGEventRef)

        self.failUnlessResultIsCFRetained(CGEventCreateSourceFromEvent)
        v = CGEventCreateSourceFromEvent(evt)
        self.failUnlessIsInstance(v, CGEventSourceRef)

        src = CGEventSourceCreate(kCGEventSourceStateCombinedSessionState)
        self.failUnlessIsInstance(src, CGEventSourceRef)

        CGEventSetSource(evt, src)

        t = CGEventGetType(evt)
        self.failUnlessIsInstance(t, (int, long))
        self.failUnlessEqual(t, kCGEventLeftMouseDown)

        CGEventSetType(evt, kCGEventOtherMouseUp)
        t = CGEventGetType(evt)
        self.failUnlessEqual(t, kCGEventOtherMouseUp)

        v = CGEventGetTimestamp(evt)
        self.failUnlessIsInstance(v, (int, long))

        CGEventSetTimestamp(evt, 99)
        v = CGEventGetTimestamp(evt)
        self.failUnlessEqual(v, 99)

        v = CGEventGetLocation(evt)
        self.failUnlessIsInstance(v, CGPoint)

        CGEventSetLocation(evt, (99, 99))
        v = CGEventGetLocation(evt)
        self.failUnlessEqual(v, (99, 99))

        v = CGEventGetFlags(evt)
        self.failUnlessIsInstance(v, (int, long))

        CGEventSetFlags(evt, 99)
        v = CGEventGetFlags(evt)
        self.failUnlessEqual(v, 99)

        v = CGEventGetIntegerValueField(evt, kCGMouseEventNumber)
        self.failUnlessIsInstance(v, (int, long))

        CGEventSetIntegerValueField(evt, kCGMouseEventNumber, 99)
        v = CGEventGetIntegerValueField(evt, kCGMouseEventNumber)
        self.failUnlessEqual(v, 99)

        v = CGEventGetDoubleValueField(evt, kCGMouseEventPressure)
        self.failUnlessIsInstance(v, float)

        CGEventSetDoubleValueField(evt, kCGMouseEventPressure, 42.5)

        self.fail("CGEventTapCreateForPSN")
        self.fail("CGEventTapEnable")
        self.fail("CGEventTapIsEnabled")
        self.fail("CGEventTapPostEvent")
        self.fail("CGGetEventTapList")
        self.fail("CGEventPost")
        self.fail("CGEventPostToPSN")


    def testFunctions(self):
        self.failUnlessIsInstance(CGEventGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CGEventCreate)
        evt = CGEventCreate(None)
        self.failUnlessIsInstance(evt, CGEventRef)

        self.failUnlessResultIsCFRetained(CGEventCreateData)
        dta = CGEventCreateData(None, evt)
        self.failUnlessIsInstance(dta, CFDataRef)

        self.failUnlessResultIsCFRetained(CGEventCreateFromData)
        v = CGEventCreateFromData(None, dta)
        self.failUnlessIsInstance(v, CGEventRef)

        self.failUnlessResultIsCFRetained(CGEventCreateMouseEvent)
        evt = CGEventCreateMouseEvent(None, kCGEventOtherMouseDown, (0, 0), 2)
        self.failUnlessIsInstance(evt, CGEventRef)

        self.failUnlessResultIsCFRetained(CGEventCreateKeyboardEvent)
        self.failUnlessArgHasType(CGEventCreateKeyboardEvent, 2, objc._C_BOOL)
        evt = CGEventCreateKeyboardEvent(None, 45, False)
        self.failUnlessIsInstance(evt, CGEventRef)


        v = CGEventCreateCopy(evt)
        self.failUnlessIsInstance(v, CGEventRef)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        self.failUnlessResultIsCFRetained(CGEventCreateScrollWheelEvent)
        evt = CGEventCreateScrollWheelEvent(None, kCGScrollEventUnitPixel, 2, 99, 44)
        self.failUnlessIsInstance(evt, CGEventRef)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99, 100, 101)
        
        v = CGEventGetUnflippedLocation(evt)
        self.failUnlessIsInstance(v, CGPoint)

if __name__ == "__main__":
    main()
