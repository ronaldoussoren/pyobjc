from PyObjCTools.TestSupport import *
import time
from CoreFoundation import *
from Foundation import NSDictionary, NSString, NSMutableDictionary


class TestTimeZone (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFTimeZoneRef)

    def testTypeID(self):
        id = CFTimeZoneGetTypeID()
        self.failUnless(isinstance(id, (int, long)))

    def testSystemZone(self):
        zone = CFTimeZoneCopySystem()
        self.failUnless( isinstance(zone, CFTimeZoneRef) )

    def testResetSystem(self):
        v = CFTimeZoneResetSystem()
        self.failUnless( v is None )

    def testCopyDefault(self):
        zone = CFTimeZoneCopyDefault()
        self.failUnless( isinstance(zone, CFTimeZoneRef) )

    def testNames(self):
        self.failUnlessResultIsCFRetained(CFTimeZoneCopyKnownNames)
        array = CFTimeZoneCopyKnownNames()
        self.failUnless( isinstance(array, CFArrayRef) )

        self.failIf( len(array) == 0 )

        for nm in array:
            self.failUnless( isinstance(nm, unicode) )

    def testAbbreviationDict(self):
        map = CFTimeZoneCopyAbbreviationDictionary()
        self.failUnless( isinstance(map, CFDictionaryRef) )
        for key, value in map.items():
            self.failUnless( isinstance(key, unicode) )
            self.failUnless( isinstance(value, unicode) )


    @min_os_level('10.6')
    def testAbbrievationDictSetting(self):
        # Setting the dictionary is technically also possible
        # on 10.5, but the code below causes a crash, even when
        # rewritten als plan Objective-C.
        map = CFTimeZoneCopyAbbreviationDictionary()
        newmap = map.mutableCopy()
        newmap[u'AAA'] = u'Europe/Amsterdam'

        v = CFTimeZoneSetAbbreviationDictionary(newmap)
        self.failUnless(v is None)

        try:
            map2 = CFTimeZoneCopyAbbreviationDictionary()
            self.failUnless( isinstance(map2, CFDictionaryRef) )
            self.failUnless( map2[u'AAA'] == u'Europe/Amsterdam' )

        finally:
            CFTimeZoneSetAbbreviationDictionary(map)

    def testZoneObject(self):
        data = open('/usr/share/zoneinfo/posixrules', 'r').read()
        data = buffer(data)
        zone = CFTimeZoneCreate(None, u"Europe/Amsterdam", data)
        self.failUnless(isinstance(zone, CFTimeZoneRef))

        self.failUnlessResultIsCFRetained(CFTimeZoneCreateWithTimeIntervalFromGMT)
        zone = CFTimeZoneCreateWithTimeIntervalFromGMT(None, 3600)
        self.failUnless(isinstance(zone, CFTimeZoneRef))

        offset = CFTimeZoneGetSecondsFromGMT(zone, time.time())
        self.assertEquals(offset, 3600)

        zone = CFTimeZoneCreateWithName(None, "Europe/Amsterdam", True)
        self.failUnless(isinstance(zone, CFTimeZoneRef))

        name = CFTimeZoneGetName(zone)
        self.assertEquals(name, u"Europe/Amsterdam")

        data = CFTimeZoneGetData(zone)
        self.failUnless(isinstance(data, CFDataRef))

        abbrev = CFTimeZoneCopyAbbreviation(zone, time.time())
        self.failUnless(isinstance(abbrev, unicode))

        dt = CFGregorianDate(
                year = 2008,
                month = 7,
                day = 1,
                hour = 12,
                minute = 0,
                second = 0)

        r = CFTimeZoneIsDaylightSavingTime(zone, 
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.failUnless(r is True)

        dt = CFGregorianDate(
                year = 2008,
                month = 11,
                day = 1,
                hour = 12,
                minute = 0,
                second = 0)

        r = CFTimeZoneIsDaylightSavingTime(zone, 
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.failUnless(r in (False, True))

        offset = CFTimeZoneGetDaylightSavingTimeOffset(zone, 
                CFGregorianDateGetAbsoluteTime(dt, zone))
        self.failUnless(isinstance(offset, float))

        dt = CFTimeZoneGetNextDaylightSavingTimeTransition(
                zone, CFGregorianDateGetAbsoluteTime(dt, zone))
        self.failUnless(isinstance(dt, float))

        nm = CFTimeZoneCopyLocalizedName(zone, 
                kCFTimeZoneNameStyleShortStandard, CFLocaleCopyCurrent())
        self.failUnless(isinstance(nm, unicode))



    def testConstants(self):
        self.failUnless( kCFTimeZoneNameStyleStandard == 0 )
        self.failUnless( kCFTimeZoneNameStyleShortStandard == 1 )
        self.failUnless( kCFTimeZoneNameStyleDaylightSaving == 2 )
        self.failUnless( kCFTimeZoneNameStyleShortDaylightSaving == 3 )

        self.failUnless( isinstance(kCFTimeZoneSystemTimeZoneDidChangeNotification, unicode) )


if __name__ == "__main__":
    main()
