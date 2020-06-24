from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHFetchOptions(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(Photos.PHFetchOptions.includeHiddenAssets)
        self.assertArgIsBOOL(Photos.PHFetchOptions.setIncludeHiddenAssets_, 0)
        self.assertResultIsBOOL(Photos.PHFetchOptions.wantsIncrementalChangeDetails)
        self.assertArgIsBOOL(Photos.PHFetchOptions.setWantsIncrementalChangeDetails_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(Photos.PHFetchOptions.includeAllBurstAssets)
        self.assertArgIsBOOL(Photos.PHFetchOptions.setIncludeAllBurstAssets_, 0)
