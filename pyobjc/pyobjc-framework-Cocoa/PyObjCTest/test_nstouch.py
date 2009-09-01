from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTouch (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessEqual(NSTouchPhaseBegan, 1 << 0)    
        self.failUnlessEqual(NSTouchPhaseMoved, 1 << 1)
        self.failUnlessEqual(NSTouchPhaseStationary, 1 << 2)
        self.failUnlessEqual(NSTouchPhaseEnded, 1 << 3)
        self.failUnlessEqual(NSTouchPhaseCancelled, 1 << 4)
        self.failUnlessEqual(NSTouchPhaseTouching, NSTouchPhaseBegan | NSTouchPhaseMoved | NSTouchPhaseStationary)
        self.failUnlessEqual(NSTouchPhaseAny, -1)

    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTouch.isResting)
        self.failUnlessResultHasType(NSTouch.deviceSize, NSSize.__typestr__)

if __name__ == "__main__":
    main()
