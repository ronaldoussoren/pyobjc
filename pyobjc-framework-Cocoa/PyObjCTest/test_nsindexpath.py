from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexPath (TestCase):
    def testMethods(self):
        self.failUnlessArgIsIn(NSIndexPath.indexPathWithIndexes_length_, 0)
        self.failUnlessArgSizeInArg(NSIndexPath.indexPathWithIndexes_length_, 0, 1)

        self.failUnlessArgIsIn(NSIndexPath.initWithIndexes_length_, 0)
        self.failUnlessArgSizeInArg(NSIndexPath.initWithIndexes_length_, 0, 1)

        self.failUnlessArgIsOut(NSIndexPath.getIndexes_, 0)
        self.failUnlessArgIsVariableSize(NSIndexPath.getIndexes_, 0)

    def testConvenience(self):
        path = NSIndexPath.indexPathWithIndexes_length_([0, 1, 4], 3)

        self.failUnlessEqual(path[0], 0)
        self.failUnlessEqual(path[1], 1)
        self.failUnlessEqual(path[2], 4)

        self.failUnlessEqual(len(path), 3)

        p2 = path + 9
        self.failUnlessEqual(len(p2), len(path) + 1)
        self.failUnlessEqual(p2[3], 9)


if __name__ == "__main__":
    main()
