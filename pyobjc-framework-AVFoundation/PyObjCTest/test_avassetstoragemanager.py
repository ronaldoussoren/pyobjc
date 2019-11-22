from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAssetStorageManager(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadedAssetEvictionPriorityImportant, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadedAssetEvictionPriorityDefault, unicode
        )


if __name__ == "__main__":
    main()
