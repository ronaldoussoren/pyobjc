
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSliderCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTickMarkBelow, 0)
        self.failUnlessEqual(NSTickMarkAbove, 1)
        self.failUnlessEqual(NSTickMarkLeft, NSTickMarkAbove)
        self.failUnlessEqual(NSTickMarkRight, NSTickMarkBelow)
        self.failUnlessEqual(NSLinearSlider, 0)
        self.failUnlessEqual(NSCircularSlider, 1)

if __name__ == "__main__":
    main()
