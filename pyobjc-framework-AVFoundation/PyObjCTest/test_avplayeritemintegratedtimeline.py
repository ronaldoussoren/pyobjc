import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerItemIntegratedTimeline(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AVFoundation.AVPlayerItemSegmentType)
        self.assertEqual(AVFoundation.AVPlayerItemSegmentTypePrimary, 0)
        self.assertEqual(AVFoundation.AVPlayerItemSegmentTypeInterstitial, 1)

    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonKey, str
        )

        self.assertIsTypedEnum(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason, str
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonSegmentsChanged,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonCurrentSegmentChanged,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonLoadedTimeRangesChanged,
            str,
        )

    @min_os_level("15.0")
    def tesT_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItemIntegratedTimeline.seekToTime_toleranceBefore_toleranceAfter_completionHandler_,
            3,
            b"vZ",
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItemIntegratedTimeline.seekToDate_completionHandler_,
            1,
            b"vZ",
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItemIntegratedTimeline.addPeriodicTimeObserverForInterval_queue_usingBlock_,
            2,
            b"v" + AVFoundation.CMTime.__typestr__,
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItemIntegratedTimeline.addBoundaryTimeObserverForSegment_offsetsIntoSegment_queue_usingBlock_,
            3,
            b"vZ",
        )
