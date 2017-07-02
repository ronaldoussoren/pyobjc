from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHFetchOptions (TestCase):
        @min_os_level('10.13')
        def testMethods(self):
            self.assertResultIsBOOL(Photos.PHFetchOptions.includeHiddenAssets)
            self.assertArgIsBOOL(Photos.PHFetchOptions.setIncludeHiddenAssets_, 0)
            self.assertResultIsBOOL(Photos.PHFetchOptions.wantsIncrementalChangeDetails)
            self.assertArgIsBOOL(Photos.PHFetchOptions.setWantsIncrementalChangeDetails_, 0)

if __name__ == "__main__":
    main()
