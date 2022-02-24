import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayer(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVPlayerRateDidChangeReason, str)
        self.assertIsTypedEnum(AVFoundation.AVPlayerWaitingReason, str)

    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVPlayerActionAtItemEnd)
        self.assertIsEnumType(AVFoundation.AVPlayerAudiovisualBackgroundPlaybackPolicy)
        self.assertIsEnumType(AVFoundation.AVPlayerHDRMode)
        self.assertIsEnumType(AVFoundation.AVPlayerStatus)
        self.assertIsEnumType(AVFoundation.AVPlayerTimeControlStatus)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVPlayerStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerStatusReadyToPlay, 1)
        self.assertEqual(AVFoundation.AVPlayerStatusFailed, 2)

        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndAdvance, 0)
        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndPause, 1)
        self.assertEqual(AVFoundation.AVPlayerActionAtItemEndNone, 2)

        self.assertEqual(AVFoundation.AVPlayerTimeControlStatusPaused, 0)
        self.assertEqual(
            AVFoundation.AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate,
            1,  # noqa: B950
        )
        self.assertEqual(AVFoundation.AVPlayerTimeControlStatusPlaying, 2)

        self.assertEqual(AVFoundation.AVPlayerHDRModeHLG, 0x1)
        self.assertEqual(AVFoundation.AVPlayerHDRModeHDR10, 0x2)
        self.assertEqual(AVFoundation.AVPlayerHDRModeDolbyVision, 0x4)

        self.assertEqual(
            AVFoundation.AVPlayerAudiovisualBackgroundPlaybackPolicyAutomatic, 1
        )
        self.assertEqual(
            AVFoundation.AVPlayerAudiovisualBackgroundPlaybackPolicyPauses, 2
        )
        self.assertEqual(
            AVFoundation.AVPlayerAudiovisualBackgroundPlaybackPolicyContinuesIfPossible,
            3,
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingToMinimizeStallsReason, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingWhileEvaluatingBufferingRateReason, str
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingWithNoItemToPlayReason, str
        )  # noqa: B950

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerEligibleForHDRPlaybackDidChangeNotification,
            str,  # noqa: B950
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerRateDidChangeReasonKey,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerRateDidChangeReasonSetRateCalled,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerRateDidChangeReasonSetRateFailed,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerRateDidChangeReasonAudioSessionInterrupted,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerRateDidChangeReasonAppBackgrounded,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingForCoordinatedPlaybackReason,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorEventsDidChangeNotification,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventDidChangeNotification,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingDuringInterstitialEventReason,
            str,  # noqa: B950
        )

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.seekToDate_completionHandler_, 1, b"vZ"
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.seekToTime_completionHandler_, 1, b"vZ"
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.seekToTime_toleranceBefore_toleranceAfter_completionHandler_,  # noqa: B950
            3,
            b"vZ",
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.prerollAtRate_completionHandler_, 1, b"vZ"
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.addPeriodicTimeObserverForInterval_queue_usingBlock_,  # noqa: B950
            2,
            b"v{_CMTime=qiIq}",
        )
        self.assertArgIsBlock(
            AVFoundation.AVPlayer.addBoundaryTimeObserverForTimes_queue_usingBlock_,  # noqa: B950
            2,
            b"v",
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayer.isMuted)
        self.assertArgIsBOOL(AVFoundation.AVPlayer.setMuted_, 0)
        self.assertResultIsBOOL(
            AVFoundation.AVPlayer.isClosedCaptionDisplayEnabled
        )  # noqa: B950
        self.assertArgIsBOOL(
            AVFoundation.AVPlayer.setClosedCaptionDisplayEnabled_, 0
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVQueuePlayer.canInsertItem_afterItem_
        )  # noqa: B950

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayer.appliesMediaSelectionCriteriaAutomatically
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayer.setAppliesMediaSelectionCriteriaAutomatically_,
            0,  # noqa: B950
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayer.allowsExternalPlayback)
        self.assertArgIsBOOL(
            AVFoundation.AVPlayer.setAllowsExternalPlayback_, 0
        )  # noqa: B950
        self.assertResultIsBOOL(AVFoundation.AVPlayer.isExternalPlaybackActive)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayer.automaticallyWaitsToMinimizeStalling
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayer.setAutomaticallyWaitsToMinimizeStalling_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVPlayer.outputObscuredDueToInsufficientExternalProtection  # noqa: B950
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayer.preventsDisplaySleepDuringVideoPlayback
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayer.setPreventsDisplaySleepDuringVideoPlayback_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayer.eligibleForHDRPlayback)

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.automaticallyHandlesInterstitialEvents
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAutomaticallyHandlesInterstitialEvents_, 0
        )
