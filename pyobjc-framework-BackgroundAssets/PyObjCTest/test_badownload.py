from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBADownload(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BADownloadState)
        self.assertEqual(BackgroundAssets.BADownloadStateFailed, -1)
        self.assertEqual(BackgroundAssets.BADownloadStateCreated, 0)
        self.assertEqual(BackgroundAssets.BADownloadStateWaiting, 1)
        self.assertEqual(BackgroundAssets.BADownloadStateDownloading, 2)
        self.assertEqual(BackgroundAssets.BADownloadStateFinished, 3)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsEnumType(BackgroundAssets.BADownloaderPriority)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityMin, int)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityDefault, int)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityMax, int)

    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertResultIsBOOL(BackgroundAssets.BADownload.isEssential)
