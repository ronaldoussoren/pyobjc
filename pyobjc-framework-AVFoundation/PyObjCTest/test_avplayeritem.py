import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVPlayerItemStatus)
        self.assertIsEnumType(AVFoundation.AVVariantPreferences)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVPlayerItemStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerItemStatusReadyToPlay, 1)
        self.assertEqual(AVFoundation.AVPlayerItemStatusFailed, 2)

        self.assertEqual(AVFoundation.AVAudioSpatializationFormatNone, 0)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMonoAndStereo, 0x3)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMultichannel, 0x4)
        self.assertEqual(
            AVFoundation.AVAudioSpatializationFormatMonoStereoAndMultichannel, 0x7
        )

        self.assertEqual(AVFoundation.AVVariantPreferenceNone, 0)
        self.assertEqual(
            AVFoundation.AVVariantPreferenceScalabilityToLosslessAudio, 1 << 0
        )

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemTimeJumpedNotification, str)
        self.assertIsInstance(
            AVFoundation.AVPlayerItemDidPlayToEndTimeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerItemFailedToPlayToEndTimeNotification, str
        )

        self.assertIsInstance(
            AVFoundation.AVPlayerItemFailedToPlayToEndTimeErrorKey, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemPlaybackStalledNotification, str)
        self.assertIsInstance(
            AVFoundation.AVPlayerItemNewAccessLogEntryNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerItemNewErrorLogEntryNotification, str
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerItemMediaSelectionDidChangeNotification, str
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItem.seekToTime_completionHandler_, 1, b"vZ"
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItem.seekToTime_toleranceBefore_toleranceAfter_completionHandler_,  # noqa: B950
            3,
            b"vZ",
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.seekToDate_)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.seekToDate_completionHandler_)
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItem.seekToDate_completionHandler_, 1, b"vZ"
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackLikelyToKeepUp)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackBufferFull)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isPlaybackBufferEmpty)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayFastForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlaySlowForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlaySlowReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canPlayFastReverse)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canStepForward)
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.canStepBackward)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.seekingWaitsForVideoCompositionRendering
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setSeekingWaitsForVideoCompositionRendering_, 0
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.canUseNetworkResourcesForLiveStreamingWhilePaused
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setCanUseNetworkResourcesForLiveStreamingWhilePaused_,  # noqa: B950
            0,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.automaticallyPreservesTimeOffsetFromLive
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAutomaticallyPreservesTimeOffsetFromLive_, 0
        )

        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isAudioSpatializationAllowed)
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAudioSpatializationAllowed_, 0
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.startsOnFirstEligibleVariant)
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setStartsOnFirstEligibleVariant_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.appliesPerFrameHDRDisplayMetadata
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAppliesPerFrameHDRDisplayMetadata_, 0
        )
