from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAssetDownloadTaskHelper(AVFoundation.NSObject):
    def URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_(
        self, a, b, c, d, e
    ):
        pass

    def URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_(
        self, a, b, c, d, e, f
    ):
        pass


class TestAVAssetDownloadTask(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMinimumRequiredMediaBitrateKey, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMediaSelectionKey, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey,
            unicode,
        )

    def test_methods(self):
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_,
            2,
            AVFoundation.CMTimeRange.__typestr__,
        )
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_,
            4,
            AVFoundation.CMTimeRange.__typestr__,
        )

        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_,
            2,
            AVFoundation.CMTimeRange.__typestr__,
        )
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_,
            4,
            AVFoundation.CMTimeRange.__typestr__,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("AVAssetDownloadDelegate")


if __name__ == "__main__":
    main()
