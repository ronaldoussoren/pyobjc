import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVQueuedSampleBufferRenderingHelper(AVFoundation.NSObject):
    def isReadyForMoreMediaData(self):
        return 0

    def requestMediaDataWhenReadyOnQueue_usingBlock_(self, q, b):
        pass

    def hasSufficientMediaDataForReliablePlaybackStart(self):
        return 0


class TestAVQueuedSampleBufferRendering(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVQueuedSampleBufferRenderingStatus)

    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusUnknown, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusRendering, 1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusFailed, 2
        )  # noqa: B950

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("AVQueuedSampleBufferRendering")

    def testMethods(self):
        self.assertResultIsBOOL(
            TestAVQueuedSampleBufferRenderingHelper.isReadyForMoreMediaData
        )
        self.assertArgIsBlock(
            TestAVQueuedSampleBufferRenderingHelper.requestMediaDataWhenReadyOnQueue_usingBlock_,  # noqa: B950
            1,
            b"v",
        )
        self.assertResultIsBOOL(
            TestAVQueuedSampleBufferRenderingHelper.hasSufficientMediaDataForReliablePlaybackStart
        )
