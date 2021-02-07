import time

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestTimeZone(TestCase):
    def testTypes(self):
        try:
            if objc.lookUpClass("NSTimeZone") is CoreFoundation.CFTimeZoneRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFTimeZoneRef)

    def testTypeID(self):
        value = CoreFoundation.CFTimeZoneGetTypeID()
        self.assertIsInstance(value, int)

    def testSystemZone(self):
        zone = CoreFoundation.CFTimeZoneCopySystem()
        self.assertIsInstance(zone, CoreFoundation.CFTimeZoneRef)

        CoreFoundation.CFTimeZoneSetDefault

    def testResetSystem(self):
        v = CoreFoundation.CFTimeZoneResetSystem()
        self.assertIs(v, None)

    def testCopyDefault(self):
        zone = CoreFoundation.CFTimeZoneCopyDefault()
        self.assertIsInstance(zone, CoreFoundation.CFTimeZoneRef)

    def testNames(self):
        self.assertResultIsCFRetained(CoreFoundation.CFTimeZoneCopyKnownNames)
        array = CoreFoundation.CFTimeZoneCopyKnownNames()
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        self.assertNotEqual(len(array), 0)
        for nm in array:
            self.assertIsInstance(nm, str)

    def testAbbreviationDict(self):
        abbrevs = CoreFoundation.CFTimeZoneCopyAbbreviationDictionary()
        self.assertIsInstance(abbrevs, CoreFoundation.CFDictionaryRef)
        for key, value in abbrevs.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, str)

    @min_os_level("10.6")
    def testAbbrievationDictSetting(self):
        # Setting the dictionary is technically also possible
        # on 10.5, but the code below causes a crash, even when
        # rewritten als plan Objective-C.
        abbrevs = CoreFoundation.CFTimeZoneCopyAbbreviationDictionary()
        newmap = abbrevs.mutableCopy()
        newmap["AAA"] = "Europe/Amsterdam"

        v = CoreFoundation.CFTimeZoneSetAbbreviationDictionary(newmap)
        self.assertIs(v, None)
        try:
            map2 = CoreFoundation.CFTimeZoneCopyAbbreviationDictionary()
            self.assertIsInstance(map2, CoreFoundation.CFDictionaryRef)
            self.assertEqual(map2["AAA"], "Europe/Amsterdam")
        finally:
            CoreFoundation.CFTimeZoneSetAbbreviationDictionary(abbrevs)

    def testZoneObject(self):
        with open("/usr/share/zoneinfo/posixrules", "rb") as fp:
            data = fp.read()
        zone = CoreFoundation.CFTimeZoneCreate(None, "Europe/Amsterdam", data)
        self.assertIsInstance(zone, CoreFoundation.CFTimeZoneRef)
        self.assertResultIsCFRetained(
            CoreFoundation.CFTimeZoneCreateWithTimeIntervalFromGMT
        )
        zone = CoreFoundation.CFTimeZoneCreateWithTimeIntervalFromGMT(None, 3600)
        self.assertIsInstance(zone, CoreFoundation.CFTimeZoneRef)
        offset = CoreFoundation.CFTimeZoneGetSecondsFromGMT(zone, time.time())
        self.assertEqual(offset, 3600)

        zone = CoreFoundation.CFTimeZoneCreateWithName(None, "Europe/Amsterdam", True)
        self.assertIsInstance(zone, CoreFoundation.CFTimeZoneRef)
        name = CoreFoundation.CFTimeZoneGetName(zone)
        self.assertEqual(name, "Europe/Amsterdam")

        data = CoreFoundation.CFTimeZoneGetData(zone)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        abbrev = CoreFoundation.CFTimeZoneCopyAbbreviation(zone, time.time())
        self.assertIsInstance(abbrev, str)
        dt = CoreFoundation.CFGregorianDate(
            year=2008, month=7, day=1, hour=12, minute=0, second=0
        )

        r = CoreFoundation.CFTimeZoneIsDaylightSavingTime(
            zone, CoreFoundation.CFGregorianDateGetAbsoluteTime(dt, zone)
        )
        self.assertIs(r, True)
        dt = CoreFoundation.CFGregorianDate(
            year=2008, month=11, day=1, hour=12, minute=0, second=0
        )

        r = CoreFoundation.CFTimeZoneIsDaylightSavingTime(
            zone, CoreFoundation.CFGregorianDateGetAbsoluteTime(dt, zone)
        )
        self.assertIn(r, (False, True))
        offset = CoreFoundation.CFTimeZoneGetDaylightSavingTimeOffset(
            zone, CoreFoundation.CFGregorianDateGetAbsoluteTime(dt, zone)
        )
        self.assertIsInstance(offset, float)
        dt = CoreFoundation.CFTimeZoneGetNextDaylightSavingTimeTransition(
            zone, CoreFoundation.CFGregorianDateGetAbsoluteTime(dt, zone)
        )
        self.assertIsInstance(dt, float)
        nm = CoreFoundation.CFTimeZoneCopyLocalizedName(
            zone,
            CoreFoundation.kCFTimeZoneNameStyleShortStandard,
            CoreFoundation.CFLocaleCopyCurrent(),
        )
        self.assertIsInstance(nm, str)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleStandard, 0)
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleShortStandard, 1)
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleDaylightSaving, 2)
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleShortDaylightSaving, 3)
        self.assertIsInstance(
            CoreFoundation.kCFTimeZoneSystemTimeZoneDidChangeNotification, str
        )
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleGeneric, 4)
        self.assertEqual(CoreFoundation.kCFTimeZoneNameStyleShortGeneric, 5)
