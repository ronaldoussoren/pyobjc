from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHAsset (TestCase):
        @min_os_level('10.13')
        def testMethods(self):
            self.assertResultIsBOOL(Photos.PHAsset.isHidden)
            self.assertResultIsBOOL(Photos.PHAsset.isFavorite)
            self.assertResultIsBOOL(Photos.PHAsset.isSyncFailureHidden)

if __name__ == "__main__":
    main()
