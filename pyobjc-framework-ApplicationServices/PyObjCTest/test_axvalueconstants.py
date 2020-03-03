import HIServices
from PyObjCTools.TestSupport import TestCase


class TestAXActionConstants(TestCase):
    def testConstants(self):
        self.assertEqual(
            HIServices.kAXHorizontalOrientationValue, "AXHorizontalOrientation"
        )
        self.assertEqual(
            HIServices.kAXVerticalOrientationValue, "AXVerticalOrientation"
        )
        self.assertEqual(HIServices.kAXUnknownOrientationValue, "AXUnknownOrientation")
        self.assertEqual(
            HIServices.kAXAscendingSortDirectionValue, "AXAscendingSortDirection"
        )
        self.assertEqual(
            HIServices.kAXDescendingSortDirectionValue, "AXDescendingSortDirection"
        )
        self.assertEqual(
            HIServices.kAXUnknownSortDirectionValue, "AXUnknownSortDirection"
        )
