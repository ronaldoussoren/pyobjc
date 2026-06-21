from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level
import Photos


class TestPHAsset(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(Photos.PHAsset.isHidden)
        self.assertResultIsBOOL(Photos.PHAsset.isFavorite)

    @min_os_level("10.13")
    @max_os_level("10.14")
    def test_methods10_13_removed_in_10_15(self):
        self.assertResultIsBOOL(Photos.PHAsset.isSyncFailureHidden)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(Photos.PHAsset.representsBurst)
        self.assertResultIsBOOL(Photos.PHAsset.canPerformEditOperation_)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(Photos.PHAsset.hasAdjustments)

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBOOL(Photos.PHAsset.setLivePhotoVideoPlaybackEnabled_, 0)

        self.assertResultIsBOOL(Photos.PHAsset.skipsDisplaySizeImage)
        self.assertArgIsBOOL(Photos.PHAsset.setSkipsDisplaySizeImage_, 0)
