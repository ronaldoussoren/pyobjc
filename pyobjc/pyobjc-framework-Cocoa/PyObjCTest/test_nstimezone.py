from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSTimeZone (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTimeZone.isDaylightSavingTimeForDate_)
        self.failUnlessResultIsBOOL(NSTimeZone.isDaylightSavingTime)
        self.failUnlessResultIsBOOL(NSTimeZone.isEqualToTimeZone_)

    def testConstants(self):
        self.failUnlessEqual(NSTimeZoneNameStyleStandard, 0)
        self.failUnlessEqual(NSTimeZoneNameStyleShortStandard, 1)
        self.failUnlessEqual(NSTimeZoneNameStyleDaylightSaving, 2)
        self.failUnlessEqual(NSTimeZoneNameStyleShortDaylightSaving, 3)

        self.failUnlessIsInstance(NSSystemTimeZoneDidChangeNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSTimeZoneNameStyleGeneric, 4)
        self.failUnlessEqual(NSTimeZoneNameStyleShortGeneric, 5)

if __name__ == "__main__":
    main()
