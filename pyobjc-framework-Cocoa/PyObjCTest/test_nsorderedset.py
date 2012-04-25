from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSOrderedSet (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSOrderedSet.isEqualToOrderedSet_)
        self.assertResultIsBOOL(NSOrderedSet.containsObject_)
        self.assertResultIsBOOL(NSOrderedSet.intersectsOrderedSet_)
        self.assertResultIsBOOL(NSOrderedSet.intersectsSet_)
        self.assertResultIsBOOL(NSOrderedSet.isSubsetOfOrderedSet_)
        self.assertResultIsBOOL(NSOrderedSet.isSubsetOfSet_)

        self.assertArgIsBlock(NSOrderedSet.enumerateObjectsUsingBlock_, 0,
                b'v@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.enumerateObjectsWithOptions_usingBlock_, 1,
                b'v@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.enumerateObjectsAtIndexes_options_usingBlock_, 2,
                b'v@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSOrderedSet.indexOfObjectPassingTest_, 0,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.indexOfObjectWithOptions_passingTest_, 1,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.indexOfObjectAtIndexes_options_passingTest_, 2,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSOrderedSet.indexesOfObjectsPassingTest_, 0,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.indexesOfObjectsWithOptions_passingTest_, 1,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSOrderedSet.indexesOfObjectsAtIndexes_options_passingTest_, 2,
                objc._C_NSBOOL + b'@'+objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsBlock(NSOrderedSet.indexOfObject_inSortedRange_options_usingComparator_, 3,
                objc._C_NSInteger + b'@@')

        self.assertArgIsBOOL(NSOrderedSet.orderedSetWithOrderedSet_range_copyItems_, 2)
        self.assertArgIsBOOL(NSOrderedSet.orderedSetWithArray_range_copyItems_, 2)
        self.assertArgIsBOOL(NSOrderedSet.orderedSetWithArray_copyItems_, 1)
        self.assertArgIsBOOL(NSOrderedSet.orderedSetWithOrderedSet_range_copyItems_, 2)
        self.assertArgIsBOOL(NSOrderedSet.orderedSetWithOrderedSet_copyItems_, 1)
        self.assertArgIsBOOL(NSOrderedSet.initWithOrderedSet_range_copyItems_, 2)
        self.assertArgIsBOOL(NSOrderedSet.initWithOrderedSet_copyItems_, 1)
        self.assertArgIsBOOL(NSOrderedSet.initWithArray_range_copyItems_, 2)
        self.assertArgIsBOOL(NSOrderedSet.initWithArray_copyItems_, 1)
        self.assertArgIsBOOL(NSOrderedSet.initWithSet_copyItems_, 1)

        self.assertArgIsBlock(NSMutableOrderedSet.sortUsingComparator_, 0,
                objc._C_NSInteger + b'@@')
        self.assertArgIsBlock(NSMutableOrderedSet.sortWithOptions_usingComparator_, 1,
                objc._C_NSInteger + b'@@')
        self.assertArgIsBlock(NSMutableOrderedSet.sortRange_options_usingComparator_, 2,
                objc._C_NSInteger + b'@@')

    @min_os_level('10.7')
    def testCreation(self):
        obj = NSOrderedSet.orderedSet()
        self.assertIsInstance(obj, NSOrderedSet)

        obj = NSOrderedSet.orderedSetWithObjects_count_([1,2,3,4,5], 3)
        self.assertIsInstance(obj, NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))
        self.assertFalse(obj.containsObject_(5))

        obj = NSOrderedSet.orderedSetWithObjects_(1, 2, 3)
        self.assertIsInstance(obj, NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))

        obj = NSOrderedSet.alloc().initWithObjects_count_([1,2,3,4,5], 3)
        self.assertIsInstance(obj, NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))
        self.assertFalse(obj.containsObject_(5))

        obj = NSOrderedSet.alloc().initWithObjects_(1, 2, 3)
        self.assertIsInstance(obj, NSOrderedSet)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))


        obj = NSMutableOrderedSet.orderedSet()
        obj.addObjects_count_([1,2,3,4], 3)
        self.assertTrue(obj.containsObject_(1))
        self.assertTrue(obj.containsObject_(2))
        self.assertTrue(obj.containsObject_(3))
        self.assertFalse(obj.containsObject_(4))

        #obj = NSMutableOrderedSet.alloc().init()
        #obj.addObjects_(1,2,3)
        #self.assertTrue(obj.containsObject_(1))
        #self.assertTrue(obj.containsObject_(2))
        #self.assertTrue(obj.containsObject_(3))

        obj.replaceObjectsInRange_withObjects_count_(NSRange(0, 1), ['a', 'b', 'c', 'd'], 3)
        self.assertTrue(obj.containsObject_('a'))
        self.assertFalse(obj.containsObject_(1))


if __name__ == "__main__":
    main()
