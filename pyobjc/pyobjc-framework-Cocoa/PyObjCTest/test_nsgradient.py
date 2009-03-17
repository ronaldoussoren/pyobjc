
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGradient (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSGradientDrawsBeforeStartingLocation, (1 << 0))
        self.failUnlessEqual(NSGradientDrawsAfterEndingLocation, (1 << 1))


    def testMethods(self):
        self.failUnlessArgSizeInArg(NSGradient.initWithColors_atLocations_colorSpace_, 1, 0)
        self.failUnlessArgIsIn(NSGradient.initWithColors_atLocations_colorSpace_, 1)
        
        self.failUnlessArgIsOut(NSGradient.getColor_location_atIndex_, 0)
        self.failUnlessArgIsOut(NSGradient.getColor_location_atIndex_, 1)


if __name__ == "__main__":
    main()
