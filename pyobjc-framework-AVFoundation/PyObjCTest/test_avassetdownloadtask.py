import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetDownloadTaskHelper(AVFoundation.NSObject):
    def URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_(  # noqa: B950
        self, a, b, c, d, e
    ):
        pass

    def URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_(  # noqa: B950
        self, a, b, c, d, e, f
    ):
        pass


class TestAVAssetDownloadTask(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMinimumRequiredMediaBitrateKey, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMediaSelectionKey, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey,
            str,  # noqa: B950
        )

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(
            AVFoundation.AVAssetDownloadTaskMinimumRequiredPresentationSizeKey, str
        )
        self.assertIsInstance(AVFoundation.AVAssetDownloadTaskPrefersHDRKey, str)

    def test_methods(self):
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_,  # noqa: B950
            2,
            AVFoundation.CMTimeRange.__typestr__,
        )
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_assetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_,  # noqa: B950
            4,
            AVFoundation.CMTimeRange.__typestr__,
        )

        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_,  # noqa: B950
            2,
            AVFoundation.CMTimeRange.__typestr__,
        )
        self.assertArgHasType(
            TestAVAssetDownloadTaskHelper.URLSession_aggregateAssetDownloadTask_didLoadTimeRange_totalTimeRangesLoaded_timeRangeExpectedToLoad_forMediaSelection_,  # noqa: B950
            4,
            AVFoundation.CMTimeRange.__typestr__,
        )

    @min_os_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("AVAssetDownloadDelegate")
