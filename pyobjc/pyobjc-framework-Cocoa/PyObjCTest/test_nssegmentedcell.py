
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSegmentSwitchTrackingSelectOne, 0)
        self.failUnlessEqual(NSSegmentSwitchTrackingSelectAny, 1)
        self.failUnlessEqual(NSSegmentSwitchTrackingMomentary, 2)

if __name__ == "__main__":
    main()
