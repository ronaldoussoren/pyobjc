from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBAAssetPackStatus(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BAAssetPackStatus)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusDownloadAvailable, 1 << 0)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusUpdateAvailable, 1 << 1)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusUpToDate, 1 << 2)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusOutOfDate, 1 << 3)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusObsolete, 1 << 4)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusDownloading, 1 << 5)
        self.assertEqual(BackgroundAssets.BAAssetPackStatusDownloaded, 1 << 6)
