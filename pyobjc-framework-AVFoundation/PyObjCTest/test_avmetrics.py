import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestAVMetrics(TestCase):
    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("AVMetricEventStreamPublisher")
        self.assertProtocolExists("AVMetricEventStreamSubscriber")

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVMetricEventStream.addPublisher_)
        self.assertResultIsBOOL(AVFoundation.AVMetricEventStream.setSubscriber_queue_)
        self.assertResultIsBOOL(AVFoundation.AVMetricErrorEvent.didRecover)
        self.assertResultIsBOOL(
            AVFoundation.AVMetricMediaResourceRequestEvent.wasReadFromCache
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMetricHLSPlaylistRequestEvent.isMultivariantPlaylist
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMetricHLSMediaSegmentRequestEvent.isMapSegment
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMetricContentKeyRequestEvent.isClientInitiated
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMetricPlayerItemSeekDidCompleteEvent.didSeekInBuffer
        )
        self.assertResultIsBOOL(
            AVFoundation.AVMetricPlayerItemVariantSwitchEvent.didSucceed
        )
