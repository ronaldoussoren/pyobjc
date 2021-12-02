import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSRange(TestCase):
    def testStructs(self):
        v = Foundation.NSRange()
        self.assertHasAttr(v, "location")
        self.assertHasAttr(v, "length")
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
        v = Foundation.NSMakeRange(1, 4)
        self.assertIsInstance(v, Foundation.NSRange)
        self.assertIsInstance(v.location, int)
        self.assertIsInstance(v.length, int)
        self.assertEqual(v.location, 1)
        self.assertEqual(v.length, 4)

        self.assertEqual(Foundation.NSMaxRange(v), 5)
        self.assertResultIsBOOL(Foundation.NSLocationInRange)
        self.assertIs(Foundation.NSLocationInRange(3, v), True)
        self.assertIs(Foundation.NSLocationInRange(15, v), False)
        self.assertResultIsBOOL(Foundation.NSEqualRanges)
        self.assertIs(Foundation.NSEqualRanges(v, v), True)
        v = Foundation.NSUnionRange((1, 3), (5, 10))
        self.assertIsInstance(v, Foundation.NSRange)

        v = Foundation.NSIntersectionRange((1, 4), (3, 5))
        self.assertIsInstance(v, Foundation.NSRange)

        v = Foundation.NSStringFromRange((9, 10))
        self.assertIsInstance(v, str)

        w = Foundation.NSRangeFromString(v)
        self.assertIsInstance(w, Foundation.NSRange)
        self.assertEqual(w, (9, 10))

        self.assertResultHasType(
            Foundation.NSValue.rangeValue, Foundation.NSRange.__typestr__
        )
