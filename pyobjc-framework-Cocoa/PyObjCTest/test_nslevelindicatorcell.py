import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSLevelIndicatorCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSRelevancyLevelIndicatorStyle, 0)
        self.assertEqual(AppKit.NSContinuousCapacityLevelIndicatorStyle, 1)
        self.assertEqual(AppKit.NSDiscreteCapacityLevelIndicatorStyle, 2)
        self.assertEqual(AppKit.NSRatingLevelIndicatorStyle, 3)

        self.assertEqual(AppKit.NSLevelIndicatorStyleRelevancy, 0)
        self.assertEqual(AppKit.NSLevelIndicatorStyleContinuousCapacity, 1)
        self.assertEqual(AppKit.NSLevelIndicatorStyleDiscreteCapacity, 2)
        self.assertEqual(AppKit.NSLevelIndicatorStyleRating, 3)
