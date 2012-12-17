from PyObjCTools.TestSupport import *
from AppKit import *
import sys

class TestNSTouch (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertEqual(NSTouchPhaseBegan, 1 << 0)
        self.assertEqual(NSTouchPhaseMoved, 1 << 1)
        self.assertEqual(NSTouchPhaseStationary, 1 << 2)
        self.assertEqual(NSTouchPhaseEnded, 1 << 3)
        self.assertEqual(NSTouchPhaseCancelled, 1 << 4)
        self.assertEqual(NSTouchPhaseTouching, NSTouchPhaseBegan | NSTouchPhaseMoved | NSTouchPhaseStationary)
        if sys.maxsize >= 2**32:
            self.assertEqual(NSTouchPhaseAny, 0xffffffffffffffff)
        else:
            self.assertEqual(NSTouchPhaseAny, 0xffffffff)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSTouch.isResting)
        self.assertResultHasType(NSTouch.deviceSize, NSSize.__typestr__)

if __name__ == "__main__":
    main()
