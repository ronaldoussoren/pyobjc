import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSTimeZone(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSTimeZoneNameStyle)
        self.assertEqual(Foundation.NSTimeZoneNameStyleStandard, 0)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortStandard, 1)
        self.assertEqual(Foundation.NSTimeZoneNameStyleDaylightSaving, 2)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortDaylightSaving, 3)
        self.assertEqual(Foundation.NSTimeZoneNameStyleGeneric, 4)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortGeneric, 5)

    def test_constants(self):
        self.assertIsInstance(Foundation.NSSystemTimeZoneDidChangeNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSTimeZone.isDaylightSavingTimeForDate_)
        self.assertResultIsBOOL(Foundation.NSTimeZone.isDaylightSavingTime)
        self.assertResultIsBOOL(Foundation.NSTimeZone.isEqualToTimeZone_)
