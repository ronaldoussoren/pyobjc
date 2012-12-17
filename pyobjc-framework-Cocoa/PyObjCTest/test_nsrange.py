from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int


class TestNSRange (TestCase):
    def testStructs(self):
        v = NSRange()
        self.assertHasAttr(v, 'location')
        self.assertHasAttr(v, 'length')

    def testFunctions(self):
        v = NSMakeRange(1, 4)
        self.assertIsInstance(v, NSRange)
        self.assertIsInstance(v.location, (int, long))
        self.assertIsInstance(v.length, (int, long))
        self.assertEqual(v.location, 1)
        self.assertEqual(v.length, 4)

        self.assertEqual(NSMaxRange(v), 5)
        self.assertResultIsBOOL(NSLocationInRange)
        self.assertIs(NSLocationInRange(3, v), True)
        self.assertIs(NSLocationInRange(15, v), False)
        self.assertResultIsBOOL(NSEqualRanges)
        self.assertIs(NSEqualRanges(v, v), True)
        v = NSUnionRange((1, 3), (5, 10))
        self.assertIsInstance(v, NSRange)

        v = NSIntersectionRange((1, 4), (3, 5))
        self.assertIsInstance(v, NSRange)

        v = NSStringFromRange((9, 10))
        self.assertIsInstance(v, unicode)

        w = NSRangeFromString(v)
        self.assertIsInstance(w, NSRange)
        self.assertEqual(w, (9, 10))

        self.assertResultHasType(NSValue.rangeValue, NSRange.__typestr__)

if __name__ == "__main__":
    main()
