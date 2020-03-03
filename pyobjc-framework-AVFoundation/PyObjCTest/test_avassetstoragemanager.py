import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetStorageManager(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadedAssetEvictionPriorityImportant, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadedAssetEvictionPriorityDefault, str
        )
