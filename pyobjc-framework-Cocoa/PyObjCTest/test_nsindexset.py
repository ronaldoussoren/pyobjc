import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSIndexSet(TestCase):
    def testConvenience(self):
        v = Foundation.NSIndexSet.indexSetWithIndexesInRange_((5, 10))
        lst = list(v)
        self.assertEqual(lst, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

        lst = list(reversed(v))
        self.assertEqual(lst, [14, 13, 12, 11, 10, 9, 8, 7, 6, 5])

        v2 = Foundation.NSIndexSet.indexSetWithIndexesInRange_((5, 9))
        v3 = Foundation.NSIndexSet.indexSetWithIndexesInRange_((5, 10))

        self.assertFalse(v == v2)
        self.assertTrue(v == v3)
        self.assertFalse(v == 42)

        self.assertTrue(v != v2)
        self.assertTrue(v != 42)
        self.assertFalse(v != v3)

        self.assertTrue(8 in v)
        self.assertFalse(16 in v)
        self.assertFalse("a" in v)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSIndexSet.isEqualToIndexSet_)
        self.assertResultIsBOOL(Foundation.NSIndexSet.containsIndex_)
        self.assertResultIsBOOL(Foundation.NSIndexSet.containsIndexesInRange_)
        self.assertResultIsBOOL(Foundation.NSIndexSet.containsIndexes_)
        self.assertResultIsBOOL(Foundation.NSIndexSet.intersectsIndexesInRange_)

        self.assertArgIsOut(Foundation.NSIndexSet.getIndexes_maxCount_inIndexRange_, 0)
        self.assertArgSizeInArg(
            Foundation.NSIndexSet.getIndexes_maxCount_inIndexRange_, 0, 1
        )
        self.assertArgSizeInResult(
            Foundation.NSIndexSet.getIndexes_maxCount_inIndexRange_, 0
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateIndexesUsingBlock_,
            0,
            b"v" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateIndexesWithOptions_usingBlock_,
            1,
            b"v" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgHasType(
            Foundation.NSIndexSet.enumerateIndexesInRange_options_usingBlock_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateIndexesInRange_options_usingBlock_,
            2,
            b"v" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexPassingTest_,
            0,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgHasType(
            Foundation.NSIndexSet.indexInRange_options_passingTest_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexInRange_options_passingTest_,
            2,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexesPassingTest_,
            0,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexesWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgHasType(
            Foundation.NSIndexSet.indexesInRange_options_passingTest_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSIndexSet.indexesInRange_options_passingTest_,
            2,
            objc._C_NSBOOL + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

    @min_os_level("10.7")
    def testMethod10_7(self):
        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateRangesUsingBlock_,
            0,
            b"v" + Foundation.NSRange.__typestr__ + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateRangesWithOptions_usingBlock_,
            1,
            b"v" + Foundation.NSRange.__typestr__ + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSIndexSet.enumerateRangesInRange_options_usingBlock_,
            2,
            b"v" + Foundation.NSRange.__typestr__ + b"o^" + objc._C_NSBOOL,
        )
