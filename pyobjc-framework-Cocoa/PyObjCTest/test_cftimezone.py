from PyObjCTools.TestSupport import *
import time
from CoreFoundation import *
from Foundation import NSDictionary, NSString, NSMutableDictionary
import sys

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int


class TestTimeZone (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFTimeZoneRef)

    def testTypeID(self):
        id = CFTimeZoneGetTypeID()
        self.assertIsInstance(id, (int, long))

    def testSystemZone(self):
        zone = CFTimeZoneCopySystem()
        self.assertIsInstance(zone, CFTimeZoneRef)

    def testResetSystem(self):
        v = CFTimeZoneResetSystem()
        self.assertIs(v, None )

    def testCopyDefault(self):
        zone = CFTimeZoneCopyDefault()
        self.assertIsInstance(zone, CFTimeZoneRef)

    def testNames(self):
        self.assertResultIsCFRetained(CFTimeZoneCopyKnownNames)
        array = CFTimeZoneCopyKnownNames()
        self.assertIsInstance(array, CFArrayRef)
        self.assertNotEqual(len(array) , 0 )
        for nm in array:
            self.assertIsInstance(nm, unicode)

    def testAbbreviationDict(self):
        map = CFTimeZoneCopyAbbreviationDictionary()
        self.assertIsInstance(map, CFDictionaryRef)
        for key, value in map.items():
            self.assertIsInstance(key, unicode)
            self.assertIsInstance(value, unicode)

    @min_os_level('10.6')
    def testAbbrievationDictSetting(self):
        # Setting the dictionary is technically also possible
        # on 10.5, but the code below causes a crash, even when
        # rewritten als plan Objective-C.
        map = CFTimeZoneCopyAbbreviationDictionary()
        newmap = map.mutableCopy()
        newmap[b'AAA'.decode('ascii')] = b'Europe/Amsterdam'.decode('ascii')

        v = CFTimeZoneSetAbbreviationDictionary(newmap)
        self.assertIs(v, None)
        try:
            map2 = CFTimeZoneCopyAbbreviationDictionary()
            self.assertIsInstance(map2, CFDictionaryRef)
            self.assertEqual(map2[b'AAA'.decode('ascii')] , b'Europe/Amsterdam'.decode('ascii') )
        finally:
            CFTimeZoneSetAbbreviationDictionary(map)

    def testZoneObject(self):
        with open('/usr/share/zoneinfo/posixrules', 'rb') as fp:
            data = fp.read()
        if sys.version_info[0] == 2:
            data = buffer(data)
        zone = CFTimeZoneCreate(None, b"Europe/Amsterdam".decode('ascii'), data)
        self.assertIsInstance(zone, CFTimeZoneRef)
        self.assertResultIsCFRetained(CFTimeZoneCreateWithTimeIntervalFromGMT)
        zone = CFTimeZoneCreateWithTimeIntervalFromGMT(None, 3600)
        self.assertIsInstance(zone, CFTimeZoneRef)
        offset = CFTimeZoneGetSecondsFromGMT(zone, time.time())
        self.assertEqual(offset, 3600)

        zone = CFTimeZoneCreateWithName(None, "Europe/Amsterdam", True)
        self.assertIsInstance(zone, CFTimeZoneRef)
        name = CFTimeZoneGetName(zone)
        self.assertEqual(name, b"Europe/Amsterdam".decode('ascii'))

        data = CFTimeZoneGetData(zone)
        self.assertIsInstance(data, CFDataRef)
        abbrev = CFTimeZoneCopyAbbreviation(zone, time.time())
        self.assertIsInstance(abbrev, unicode)
        dt = CFGregorianDate(
                year = 2008,
                month = 7,
                day = 1,
                hour = 12,
                minute = 0,
                second = 0)

        r = CFTimeZoneIsDaylightSavingTime(zone,
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.assertIs(r, True)
        dt = CFGregorianDate(
                year = 2008,
                month = 11,
                day = 1,
                hour = 12,
                minute = 0,
                second = 0)

        r = CFTimeZoneIsDaylightSavingTime(zone,
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.assertIn(r, (False, True))
        offset = CFTimeZoneGetDaylightSavingTimeOffset(zone,
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.assertIsInstance(offset, float)
        dt = CFTimeZoneGetNextDaylightSavingTimeTransition(
                zone, CFGregorianDateGetAbsoluteTime(dt, zone))
        self.assertIsInstance(dt, float)
        nm = CFTimeZoneCopyLocalizedName(zone,
                kCFTimeZoneNameStyleShortStandard, CFLocaleCopyCurrent())
        self.assertIsInstance(nm, unicode)

    def testConstants(self):
        self.assertEqual(kCFTimeZoneNameStyleStandard , 0 )
        self.assertEqual(kCFTimeZoneNameStyleShortStandard , 1 )
        self.assertEqual(kCFTimeZoneNameStyleDaylightSaving , 2 )
        self.assertEqual(kCFTimeZoneNameStyleShortDaylightSaving , 3 )
        self.assertIsInstance(kCFTimeZoneSystemTimeZoneDidChangeNotification, unicode)
        self.assertEqual(kCFTimeZoneNameStyleGeneric, 4)
        self.assertEqual(kCFTimeZoneNameStyleShortGeneric, 5)


if __name__ == "__main__":
    main()
