from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexSet (TestCase):
    def testConvenience(self):
        v = NSIndexSet.indexSetWithIndexesInRange_((5, 10))
        l = list(v)
        self.assertEqual(l, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

        l = list(reversed(v))
        self.assertEqual(l, [14, 13, 12, 11, 10, 9, 8, 7, 6, 5])


        v2 = NSIndexSet.indexSetWithIndexesInRange_((5, 9))
        v3 = NSIndexSet.indexSetWithIndexesInRange_((5, 10))

        self.assertFalse(v == v2)
        self.assertTrue(v == v3)
        self.assertFalse(v == 42)

        self.assertTrue(v != v2)
        self.assertTrue(v != 42)
        self.assertFalse(v != v3)

        self.assertTrue(8 in v)
        self.assertFalse(16 in v)
        self.assertFalse('a'in v)


    def testMethods(self):
        self.assertResultIsBOOL(NSIndexSet.isEqualToIndexSet_)
        self.assertResultIsBOOL(NSIndexSet.containsIndex_)
        self.assertResultIsBOOL(NSIndexSet.containsIndexesInRange_)
        self.assertResultIsBOOL(NSIndexSet.containsIndexes_)
        self.assertResultIsBOOL(NSIndexSet.intersectsIndexesInRange_)

        self.assertArgIsOut(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0)
        self.assertArgSizeInArg(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0, 1)
        self.assertArgSizeInResult(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSIndexSet.enumerateIndexesUsingBlock_, 0,
                b'v' + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSIndexSet.enumerateIndexesWithOptions_usingBlock_, 1,
                b'v' + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSIndexSet.enumerateIndexesInRange_options_usingBlock_, 0, NSRange.__typestr__)
        self.assertArgIsBlock(NSIndexSet.enumerateIndexesInRange_options_usingBlock_, 2,
                b'v' + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSIndexSet.indexPassingTest_, 0,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSIndexSet.indexWithOptions_passingTest_, 1,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSIndexSet.indexInRange_options_passingTest_, 0,  NSRange.__typestr__)
        self.assertArgIsBlock(NSIndexSet.indexInRange_options_passingTest_, 2,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSIndexSet.indexesPassingTest_, 0,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSIndexSet.indexesWithOptions_passingTest_, 1,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSIndexSet.indexesInRange_options_passingTest_, 0,  NSRange.__typestr__)
        self.assertArgIsBlock(NSIndexSet.indexesInRange_options_passingTest_, 2,
                objc._C_NSBOOL + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

    @min_os_level('10.7')
    def testMethod10_7(self):
        self.assertArgIsBlock(NSIndexSet.enumerateRangesUsingBlock_, 0,
                b'v' + NSRange.__typestr__ + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSIndexSet.enumerateRangesWithOptions_usingBlock_, 1,
                b'v' + NSRange.__typestr__ + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSIndexSet.enumerateRangesInRange_options_usingBlock_, 2,
                b'v' + NSRange.__typestr__ + b'o^' + objc._C_NSBOOL)


if __name__ == "__main__":
    main()
