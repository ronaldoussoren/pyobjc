import unittest
from CoreFoundation import *
from Foundation import NSDictionary, NSString


class TestTree (unittest.TestCase):
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

        newmap = NSDictionary.dictionaryWithDictionary_({
                NSString.stringWithString_('AAA'):
                    NSString.stringWithString_('Europe/Amsterdam')})
        v = CFTimeZoneSetAbbreviationDictionary(newmap)
        self.failUnless(v is None)

        try:
            map2 = CFTimeZoneCopyAbbreviationDictionary()
            self.failUnless( isinstance(map2, CFDictionaryRef) )
            self.failUnless( map2[u'AAA'] == u'Europe/Amsterdam' )

        finally:
            CFTimeZoneSetAbbreviationDictionary(map)

    def testDummy(self):
        self.fail("CFTimeZone tests are incomplete (start at CFTimeZoneCreate)")


    def testConstants(self):
        self.failUnless( kCFTimeZoneNameStyleStandard == 0 )
        self.failUnless( kCFTimeZoneNameStyleShortStandard == 1 )
        self.failUnless( kCFTimeZoneNameStyleDaylightSaving == 2 )
        self.failUnless( kCFTimeZoneNameStyleShortDaylightSaving == 3 )

        self.failUnless( isinstance(kCFTimeZoneSystemTimeZoneDidChangeNotification, unicode) )





if __name__ == "__main__":
    unittest.main()
