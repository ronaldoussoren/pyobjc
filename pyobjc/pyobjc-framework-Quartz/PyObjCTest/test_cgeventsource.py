
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGEventSource (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGEventSourceRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CGEventSourceGetTypeID(), (int, long))

        src = CGEventSourceCreate(0)
        self.failUnlessIsInstance(src, CGEventSourceRef)

        v = CGEventSourceGetKeyboardType(src)
        self.failUnlessIsInstance(v, (int, long))

        CGEventSourceSetKeyboardType(src, v)

        CGEventSourceSetPixelsPerLine(src, 23)
        v = CGEventSourceGetPixelsPerLine(src)
        self.failUnlessIsInstance(v, float)
        self.failUnlessEqual(v, 23)

        v = CGEventSourceGetSourceStateID(src)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultHasType(CGEventSourceButtonState, objc._C_BOOL)
        v = CGEventSourceButtonState(0, 0)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultHasType(CGEventSourceKeyState, objc._C_BOOL)
        v = CGEventSourceKeyState(0, 64)
        self.failUnlessIsInstance(v, bool)

        v = CGEventSourceFlagsState(0)
        self.failUnlessIsInstance(v, (int, long))

        v = CGEventSourceSecondsSinceLastEventType(0, kCGEventLeftMouseDown)
        self.failUnlessIsInstance(v, float)

        v = CGEventSourceCounterForEventType(0, kCGEventLeftMouseDown)
        self.failUnlessIsInstance(v, (int, long))

        CGEventSourceSetUserData(src, 0xabbccdd00112233)
        v = CGEventSourceGetUserData(src)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessEqual(v, 0xabbccdd00112233)

        CGEventSourceSetLocalEventsFilterDuringSuppressionState(src, 
                kCGEventFlagMaskControl|kCGEventFlagMaskCommand,
                 kCGEventSuppressionStateRemoteMouseDrag )

        m = CGEventSourceGetLocalEventsFilterDuringSuppressionState(src, 
                 kCGEventSuppressionStateRemoteMouseDrag )
        self.failUnlessIsInstance(m, (int, long))
        
        CGEventSourceSetLocalEventsSuppressionInterval(src, 1.5)
        v = CGEventSourceGetLocalEventsSuppressionInterval(src)
        self.failUnlessEqual(v, 1.5)

if __name__ == "__main__":
    main()
