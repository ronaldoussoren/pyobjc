import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVPlaybackCoordinatorHelper(AVFoundation.NSObject):
    def playbackCoordinator_didIssuePlayCommand_completionHandler_(self, a, b, c):
        pass

    def playbackCoordinator_didIssuePauseCommand_completionHandler_(self, a, b, c):
        pass

    def playbackCoordinator_didIssueSeekCommand_completionHandler_(self, a, b, c):
        pass

    def playbackCoordinator_didIssueBufferingCommand_completionHandler_(self, a, b, c):
        pass


class TestAVPlaybackCoordinator(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            AVFoundation.AVDelegatingPlaybackCoordinatorRateChangeOptions
        )
        self.assertIsEnumType(AVFoundation.AVDelegatingPlaybackCoordinatorSeekOptions)

    def test_constants(self):
        self.assertEqual(
            AVFoundation.AVDelegatingPlaybackCoordinatorRateChangeOptionPlayImmediately,
            1 << 0,
        )
        self.assertEqual(
            AVFoundation.AVDelegatingPlaybackCoordinatorSeekOptionResumeImmediately,
            1 << 0,
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AVFoundation.AVCoordinatedPlaybackSuspensionReasonAudioSessionInterrupted,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVCoordinatedPlaybackSuspensionReasonStallRecovery, str
        )
        self.assertIsInstance(
            AVFoundation.AVCoordinatedPlaybackSuspensionReasonPlayingInterstitial, str
        )
        self.assertIsInstance(
            AVFoundation.AVCoordinatedPlaybackSuspensionReasonUserActionRequired, str
        )
        self.assertIsInstance(
            AVFoundation.AVCoordinatedPlaybackSuspensionReasonUserIsChangingCurrentTime,
            str,
        )

        self.assertIsInstance(
            AVFoundation.AVPlaybackCoordinatorOtherParticipantsDidChangeNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlaybackCoordinatorSuspensionReasonsDidChangeNotification,
            str,
        )

    def test_methods(self):
        self.assertArgIsBlock(
            TestAVPlaybackCoordinatorHelper.playbackCoordinator_didIssuePlayCommand_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            TestAVPlaybackCoordinatorHelper.playbackCoordinator_didIssuePauseCommand_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            TestAVPlaybackCoordinatorHelper.playbackCoordinator_didIssueSeekCommand_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            TestAVPlaybackCoordinatorHelper.playbackCoordinator_didIssueBufferingCommand_completionHandler_,
            2,
            b"v",
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCoordinatedPlaybackParticipant.isReadyToPlay
        )
        self.assertResultIsBOOL(
            AVFoundation.AVPlaybackCoordinator.pauseSnapsToMediaTimeOfOriginator
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlaybackCoordinator.setPauseSnapsToMediaTimeOfOriginator_,
            0,
        )
        self.assertResultIsBOOL(
            AVFoundation.AVDelegatingPlaybackCoordinatorPauseCommand.shouldBufferInAnticipationOfPlayback
        )
        self.assertResultIsBOOL(
            AVFoundation.AVDelegatingPlaybackCoordinatorSeekCommand.shouldBufferInAnticipationOfPlayback
        )

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("AVPlaybackCoordinatorPlaybackControlDelegate")
