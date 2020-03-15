import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSOrderedSet(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.differenceFromOrderedSet_withOptions_usingEquivalenceTest_,
            2,
            b"Z@@",
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(Foundation.NSOrderedSet.isEqualToOrderedSet_)
        self.assertResultIsBOOL(Foundation.NSOrderedSet.containsObject_)
        self.assertResultIsBOOL(Foundation.NSOrderedSet.intersectsOrderedSet_)
        self.assertResultIsBOOL(Foundation.NSOrderedSet.intersectsSet_)
        self.assertResultIsBOOL(Foundation.NSOrderedSet.isSubsetOfOrderedSet_)
        self.assertResultIsBOOL(Foundation.NSOrderedSet.isSubsetOfSet_)

        self.assertArgIsBlock(
            Foundation.NSOrderedSet.enumerateObjectsUsingBlock_,
            0,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.enumerateObjectsWithOptions_usingBlock_,
            1,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.enumerateObjectsAtIndexes_options_usingBlock_,
            2,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexOfObjectPassingTest_,
            0,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexOfObjectWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexOfObjectAtIndexes_options_passingTest_,
            2,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexesOfObjectsPassingTest_,
            0,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexesOfObjectsWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexesOfObjectsAtIndexes_options_passingTest_,
            2,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSOrderedSet.indexOfObject_inSortedRange_options_usingComparator_,
            3,
            objc._C_NSInteger + b"@@",
        )

        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithOrderedSet_range_copyItems_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithArray_range_copyItems_, 2
        )
        self.assertArgIsBOOL(Foundation.NSOrderedSet.orderedSetWithArray_copyItems_, 1)
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithOrderedSet_range_copyItems_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithOrderedSet_copyItems_, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.initWithOrderedSet_range_copyItems_, 2
        )
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithOrderedSet_copyItems_, 1)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithArray_range_copyItems_, 2)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithArray_copyItems_, 1)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithSet_copyItems_, 1)

        self.assertArgIsBlock(
            Foundation.NSMutableOrderedSet.sortUsingComparator_,
            0,
            objc._C_NSInteger + b"@@",
        )
        self.assertArgIsBlock(
            Foundation.NSMutableOrderedSet.sortWithOptions_usingComparator_,
            1,
            objc._C_NSInteger + b"@@",
        )
        self.assertArgIsBlock(
            Foundation.NSMutableOrderedSet.sortRange_options_usingComparator_,
            2,
            objc._C_NSInteger + b"@@",
        )

        self.assertArgIsBlock(
            Foundation.NSOrderedSet.sortedArrayUsingComparator_,
            0,
            objc._C_NSInteger + b"@@",
        )
        self.assertArgIsBlock(
            Foundation.NSOrderedSet.sortedArrayWithOptions_usingComparator_,
            1,
            objc._C_NSInteger + b"@@",
        )

    @min_os_level("10.7")
    def testCreation(self):
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithOrderedSet_range_copyItems_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.orderedSetWithArray_range_copyItems_, 2
        )
        self.assertArgIsBOOL(Foundation.NSOrderedSet.orderedSetWithSet_copyItems_, 1)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithOrderedSet_copyItems_, 1)
        self.assertArgIsBOOL(
            Foundation.NSOrderedSet.initWithOrderedSet_range_copyItems_, 2
        )
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithArray_copyItems_, 1)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithArray_range_copyItems_, 2)
        self.assertArgIsBOOL(Foundation.NSOrderedSet.initWithSet_copyItems_, 1)

        obj = Foundation.NSOrderedSet.orderedSet()
        self.assertIsInstance(obj, Foundation.NSOrderedSet)

        obj = Foundation.NSOrderedSet.orderedSetWithObjects_count_([1, 2, 3, 4, 5], 3)
        self.assertIsInstance(obj, Foundation.NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))
        self.assertFalse(obj.containsObject_(5))

        obj = Foundation.NSOrderedSet.orderedSetWithObjects_(1, 2, 3)
        self.assertIsInstance(obj, Foundation.NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))

        obj = Foundation.NSOrderedSet.alloc().initWithObjects_count_([1, 2, 3, 4, 5], 3)
        self.assertIsInstance(obj, Foundation.NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))
        self.assertFalse(obj.containsObject_(5))

        obj = Foundation.NSOrderedSet.alloc().initWithObjects_(1, 2, 3)
        self.assertIsInstance(obj, Foundation.NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))

        obj = Foundation.NSMutableOrderedSet.orderedSet()
        obj.addObjects_count_([1, 2, 3, 4], 3)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))

        # obj = Foundation.NSMutableOrderedSet.alloc().init()
        # obj.addObjects_(1,2,3)
        # self.assertTrue(obj.containsObject_(1))
        # self.assertTrue(obj.containsObject_(2))
        # self.assertTrue(obj.containsObject_(3))

        obj.replaceObjectsInRange_withObjects_count_(
            Foundation.NSRange(0, 1), ["a", "b", "c", "d"], 3
        )
        self.assertTrue(obj.containsObject_("a"))
        self.assertFalse(obj.containsObject_(1))
