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

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsOut(NSIndexPath.getIndexes_range_, 0)
        self.assertArgSizeInArg(NSIndexPath.getIndexes_range_, 0, 1)

    def testConvenience(self):
        path = NSIndexPath.indexPathWithIndexes_length_([0, 1, 4], 3)

        self.assertEqual(path[0], 0)
        self.assertEqual(path[1], 1)
        self.assertEqual(path[2], 4)

        self.assertEqual(len(path), 3)

        p2 = path + 9
        self.assertEqual(len(p2), len(path) + 1)
        self.assertEqual(p2[3], 9)

        with self.assertRaises(ValueError):
            p2[1:3]


if __name__ == "__main__":
    main()
