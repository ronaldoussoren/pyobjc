from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSRange (TestCase):
    def testStructs(self):
        v = NSRange()
        self.failUnless(hasattr(v, 'location'))
        self.failUnless(hasattr(v, 'length'))

    def testFunctions(self):
        v = NSMakeRange(1, 4)
        self.failUnlessIsInstance(v, NSRange)
        self.failUnlessIsInstance(v.location, (int, long))
        self.failUnlessIsInstance(v.length, (int, long))
        self.failUnlessEqual(v.location, 1)
        self.failUnlessEqual(v.length, 4)

        self.failUnlessEqual(NSMaxRange(v), 5)
        self.failUnlessResultIsBOOL(NSLocationInRange)
        self.failUnless(NSLocationInRange(3, v) is True)
        self.failUnless(NSLocationInRange(15, v) is False)

        self.failUnlessResultIsBOOL(NSEqualRanges)
        self.failUnless(NSEqualRanges(v, v) is True)

        v = NSUnionRange((1, 3), (5, 10))
        self.failUnlessIsInstance(v, NSRange)

        v = NSIntersectionRange((1, 4), (3, 5))
        self.failUnlessIsInstance(v, NSRange)

        v = NSStringFromRange((9, 10))
        self.failUnlessIsInstance(v, unicode)

        w = NSRangeFromString(v)
        self.failUnlessIsInstance(w, NSRange)
        self.failUnlessEqual(w, (9, 10))

if __name__ == "__main__":
    main()

