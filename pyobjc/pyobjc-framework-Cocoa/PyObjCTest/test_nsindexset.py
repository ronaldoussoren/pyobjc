from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexSet (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSIndexSet.isEqualToIndexSet_)
        self.failUnlessResultIsBOOL(NSIndexSet.containsIndex_)
        self.failUnlessResultIsBOOL(NSIndexSet.containsIndexesInRange_)
        self.failUnlessResultIsBOOL(NSIndexSet.containsIndexes_)
        self.failUnlessResultIsBOOL(NSIndexSet.intersectsIndexesInRange_)

        self.failUnlessArgIsOut(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0)
        self.failUnlessArgSizeInArg(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0, 1)
        self.failUnlessArgSizeInResult(NSIndexSet.getIndexes_maxCount_inIndexRange_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBlock(NSIndexSet.enumerateIndexesUsingBlock_, 0,
                'v' + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsBlock(NSIndexSet.enumerateIndexesWithOptions_usingBlock_, 1,
                'v' + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSIndexSet.enumerateIndexesInRange_options_usingBlock_, 0, NSRange.__typestr__)
        self.failUnlessArgIsBlock(NSIndexSet.enumerateIndexesInRange_options_usingBlock_, 2,
                'v' + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)

        self.failUnlessArgIsBlock(NSIndexSet.indexPassingTest_, 0, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsBlock(NSIndexSet.indexWithOptions_passingTest_, 1, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSIndexSet.indexInRange_options_passingTest_, 0,  NSRange.__typestr__)
        self.failUnlessArgIsBlock(NSIndexSet.indexInRange_options_passingTest_, 2, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)

        self.failUnlessArgIsBlock(NSIndexSet.indexesPassingTest_, 0, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsBlock(NSIndexSet.indexesWithOptions_passingTest_, 1, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSIndexSet.indexesInRange_options_passingTest_, 0,  NSRange.__typestr__)
        self.failUnlessArgIsBlock(NSIndexSet.indexesInRange_options_passingTest_, 2, 
                objc._C_NSBOOL + objc._C_NSUInteger + 'o^' + objc._C_NSBOOL)


if __name__ == "__main__":
    main()
