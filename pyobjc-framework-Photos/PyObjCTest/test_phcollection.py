from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHCollection(TestCase):
        @min_os_level("10.15")
        def testMethods10_15(self):
            self.assertResultIsBOOL(Photos.PHCollection.canContainAssets)
            self.assertResultIsBOOL(Photos.PHCollection.canContainCollections)
            self.assertResultIsBOOL(Photos.PHCollection.canPerformEditOperation_)


if __name__ == "__main__":
    main()
