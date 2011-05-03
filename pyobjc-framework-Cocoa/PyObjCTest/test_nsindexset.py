from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexSet (TestCase):
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


if __name__ == "__main__":
    main()
