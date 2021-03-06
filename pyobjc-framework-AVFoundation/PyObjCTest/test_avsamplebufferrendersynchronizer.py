import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleBufferRenderSynchronizer(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferRenderSynchronizer.addPeriodicTimeObserverForInterval_queue_usingBlock_,  # noqa: B950
            2,
            b"v{_CMTime=qiIq}",
        )
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferRenderSynchronizer.addBoundaryTimeObserverForTimes_queue_usingBlock_,  # noqa: B950
            2,
            b"v",
        )

    @min_os_level("11.3")
    def testMethods11_3(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferRenderSynchronizer.delaysRateChangeUntilHasSufficientMediaData
        )
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferRenderSynchronizer.setDelaysRateChangeUntilHasSufficientMediaData_,
            0,
        )

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(
            AVFoundation.AVSampleBufferRenderSynchronizerRateDidChangeNotification,
            str,  # noqa: B950
        )
