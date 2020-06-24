from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level
import Photos


class TestPHAsset(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(Photos.PHAsset.isHidden)
        self.assertResultIsBOOL(Photos.PHAsset.isFavorite)

    @min_os_level("10.13")
    @max_os_level("10.14")
    def testMethods10_13_removed_in_10_15(self):
        self.assertResultIsBOOL(Photos.PHAsset.isSyncFailureHidden)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(Photos.PHAsset.representsBurst)
        self.assertResultIsBOOL(Photos.PHAsset.canPerformEditOperation_)
