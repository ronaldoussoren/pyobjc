
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGEvent (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGEventRef)
        self.failUnlessIsCFType(CGEventSourceRef)

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

        self.failUnlessResultIsCFRetained(CGEventCreateScrollWheelEvent)
        evt = CGEventCreateScrollWheelEvent(None, kCGScrollEventUnitPixel, 2, 99, 44)
        self.failUnlessIsInstance(evt, CGEventRef)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99)
        self.assertRaises(ValueError, CGEventCreateScrollWheelEvent, kCGScrollEventUnitPixel, 40, 2, 99, 100, 101)

        v = CGEventCreateCopy(evt)
        self.failUnlessIsInstance(v, CGEventRef)
        

if __name__ == "__main__":
    main()
