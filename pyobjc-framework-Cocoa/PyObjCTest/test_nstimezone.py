from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


class TestNSTimeZone (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSTimeZone.isDaylightSavingTimeForDate_)
        self.assertResultIsBOOL(NSTimeZone.isDaylightSavingTime)
        self.assertResultIsBOOL(NSTimeZone.isEqualToTimeZone_)

    def testConstants(self):
        self.assertEqual(NSTimeZoneNameStyleStandard, 0)
        self.assertEqual(NSTimeZoneNameStyleShortStandard, 1)
        self.assertEqual(NSTimeZoneNameStyleDaylightSaving, 2)
        self.assertEqual(NSTimeZoneNameStyleShortDaylightSaving, 3)

        self.assertIsInstance(NSSystemTimeZoneDidChangeNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSTimeZoneNameStyleGeneric, 4)
        self.assertEqual(NSTimeZoneNameStyleShortGeneric, 5)

if __name__ == "__main__":
    main()
