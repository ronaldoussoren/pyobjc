
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

try:
    long
except NameError:
    long = int

class TestCGEventSource (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGEventSourceRef)

    def testFunctions(self):
        self.assertIsInstance(CGEventSourceGetTypeID(), (int, long))

        src = CGEventSourceCreate(0)
        self.assertIsInstance(src, CGEventSourceRef)

        v = CGEventSourceGetKeyboardType(src)
        self.assertIsInstance(v, (int, long))

        CGEventSourceSetKeyboardType(src, v)

        CGEventSourceSetPixelsPerLine(src, 23)
        v = CGEventSourceGetPixelsPerLine(src)
        self.assertIsInstance(v, float)
        self.assertEqual(v, 23)

        v = CGEventSourceGetSourceStateID(src)
        self.assertIsInstance(v, (int, long))

        self.assertResultHasType(CGEventSourceButtonState, objc._C_BOOL)
        v = CGEventSourceButtonState(0, 0)
        self.assertIsInstance(v, bool)

        self.assertResultHasType(CGEventSourceKeyState, objc._C_BOOL)
        v = CGEventSourceKeyState(0, 64)
        self.assertIsInstance(v, bool)

        v = CGEventSourceFlagsState(0)
        self.assertIsInstance(v, (int, long))

        v = CGEventSourceSecondsSinceLastEventType(0, kCGEventLeftMouseDown)
        self.assertIsInstance(v, float)

        v = CGEventSourceCounterForEventType(0, kCGEventLeftMouseDown)
        self.assertIsInstance(v, (int, long))

        CGEventSourceSetUserData(src, 0xabbccdd00112233)
        v = CGEventSourceGetUserData(src)
        self.assertIsInstance(v, (int, long))
        self.assertEqual(v, 0xabbccdd00112233)

        CGEventSourceSetLocalEventsFilterDuringSuppressionState(src,
                kCGEventFlagMaskControl|kCGEventFlagMaskCommand,
                 kCGEventSuppressionStateRemoteMouseDrag )

        m = CGEventSourceGetLocalEventsFilterDuringSuppressionState(src,
                 kCGEventSuppressionStateRemoteMouseDrag )
        self.assertIsInstance(m, (int, long))

        CGEventSourceSetLocalEventsSuppressionInterval(src, 1.5)
        v = CGEventSourceGetLocalEventsSuppressionInterval(src)
        self.assertEqual(v, 1.5)

if __name__ == "__main__":
    main()
