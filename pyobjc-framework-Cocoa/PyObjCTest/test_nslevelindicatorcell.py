
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLevelIndicatorCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSRelevancyLevelIndicatorStyle, 0)
        self.assertEqual(NSContinuousCapacityLevelIndicatorStyle, 1)
        self.assertEqual(NSDiscreteCapacityLevelIndicatorStyle, 2)
        self.assertEqual(NSRatingLevelIndicatorStyle, 3)

if __name__ == "__main__":
    main()
