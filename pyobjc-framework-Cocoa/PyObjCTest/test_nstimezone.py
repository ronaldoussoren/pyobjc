import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTimeZone(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSTimeZone.isDaylightSavingTimeForDate_)
        self.assertResultIsBOOL(Foundation.NSTimeZone.isDaylightSavingTime)
        self.assertResultIsBOOL(Foundation.NSTimeZone.isEqualToTimeZone_)

    def testConstants(self):
        self.assertEqual(Foundation.NSTimeZoneNameStyleStandard, 0)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortStandard, 1)
        self.assertEqual(Foundation.NSTimeZoneNameStyleDaylightSaving, 2)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortDaylightSaving, 3)

        self.assertIsInstance(Foundation.NSSystemTimeZoneDidChangeNotification, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSTimeZoneNameStyleGeneric, 4)
        self.assertEqual(Foundation.NSTimeZoneNameStyleShortGeneric, 5)
