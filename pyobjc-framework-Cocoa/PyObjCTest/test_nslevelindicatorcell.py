
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLevelIndicatorCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSRelevancyLevelIndicatorStyle, 0)
        self.failUnlessEqual(NSContinuousCapacityLevelIndicatorStyle, 1)
        self.failUnlessEqual(NSDiscreteCapacityLevelIndicatorStyle, 2)
        self.failUnlessEqual(NSRatingLevelIndicatorStyle, 3)

if __name__ == "__main__":
    main()
