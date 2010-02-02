
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGradient (TestCase):
    def testConstants(self):
        self.assertEqual(NSGradientDrawsBeforeStartingLocation, (1 << 0))
        self.assertEqual(NSGradientDrawsAfterEndingLocation, (1 << 1))


    def testMethods(self):
        self.assertArgSizeInArg(NSGradient.initWithColors_atLocations_colorSpace_, 1, 0)
        self.assertArgIsIn(NSGradient.initWithColors_atLocations_colorSpace_, 1)
        
        self.assertArgIsOut(NSGradient.getColor_location_atIndex_, 0)
        self.assertArgIsOut(NSGradient.getColor_location_atIndex_, 1)


if __name__ == "__main__":
    main()
