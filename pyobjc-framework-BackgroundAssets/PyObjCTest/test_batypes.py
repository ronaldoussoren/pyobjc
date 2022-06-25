from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBATypes(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BADownloadState)

        self.assertEqual(BackgroundAssets.BADownloadStateFailed, -1)
        self.assertEqual(BackgroundAssets.BADownloadStateCreated, 0)
        self.assertEqual(BackgroundAssets.BADownloadStateWaiting, 1)
        self.assertEqual(BackgroundAssets.BADownloadStateDownloading, 2)
        self.assertEqual(BackgroundAssets.BADownloadStateFinished, 3)

        self.assertIsTypedEnum(BackgroundAssets.BADownloadState, int)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityMin, int)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityDefault, int)
        self.assertIsInstance(BackgroundAssets.BADownloaderPriorityMax, int)
