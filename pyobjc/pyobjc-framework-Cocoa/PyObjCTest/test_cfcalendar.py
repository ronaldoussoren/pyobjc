import unittest
import CoreFoundation

class TestCFCalendarVariadic (unittest.TestCase):
    def testCFCalendarComposeAbsoluteTime(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
                None, CoreFoundation.kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, '')
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

    def testCFCalendarAddComponents(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
                None, CoreFoundation.kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, at2 = CoreFoundation.CFCalendarAddComponents(
                calendar, at, 0, "yH", 2, 3)
        self.assertEquals(success, True)
        self.assert_(isinstance(at2, float))

        success, y, H = CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at, at2, 0, "yH")
        self.assertEquals(success, True)
        self.assertEquals(y, 2)
        self.assertEquals(H, 3)


    def testCFCalendarDecomposeAbsoluteTime(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
                None, CoreFoundation.kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, y, M, d, H, m, s = CoreFoundation.CFCalendarDecomposeAbsoluteTime(
                calendar, at, "yMdHms")
        self.assertEquals(y, 1965)
        self.assertEquals(M, 1)
        self.assertEquals(d, 6)
        self.assertEquals(H, 14)
        self.assertEquals(m, 10)
        self.assertEquals(s, 0)

    def testCFCalendarGetComponentDifference(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
                None, CoreFoundation.kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at1 = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at1, float))

        success, at2 = CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1967, 2, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at2, float))

        success, y, M = CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, "yM")
        self.assertEquals(success, True)
        self.assertEquals(y, 2)
        self.assertEquals(M, 1)



if __name__ == "__main__":
    unittest.main()
