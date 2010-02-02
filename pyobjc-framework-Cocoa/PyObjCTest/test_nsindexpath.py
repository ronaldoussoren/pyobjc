from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexPath (TestCase):
    def testMethods(self):
        self.assertArgIsIn(NSIndexPath.indexPathWithIndexes_length_, 0)
        self.assertArgSizeInArg(NSIndexPath.indexPathWithIndexes_length_, 0, 1)

        self.assertArgIsIn(NSIndexPath.initWithIndexes_length_, 0)
        self.assertArgSizeInArg(NSIndexPath.initWithIndexes_length_, 0, 1)

        self.assertArgIsOut(NSIndexPath.getIndexes_, 0)
        self.assertArgIsVariableSize(NSIndexPath.getIndexes_, 0)

    def testConvenience(self):
        path = NSIndexPath.indexPathWithIndexes_length_([0, 1, 4], 3)

        self.assertEqual(path[0], 0)
        self.assertEqual(path[1], 1)
        self.assertEqual(path[2], 4)

        self.assertEqual(len(path), 3)

        p2 = path + 9
        self.assertEqual(len(p2), len(path) + 1)
        self.assertEqual(p2[3], 9)


if __name__ == "__main__":
    main()
