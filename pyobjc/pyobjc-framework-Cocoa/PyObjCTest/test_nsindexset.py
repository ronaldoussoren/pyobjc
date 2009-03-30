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


if __name__ == "__main__":
    main()
