import AVFoundation
from PyObjCTools.TestSupport import TestCase, fourcc, min_os_level


class TestAVAudioSession(TestCase):
    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation,
            1,  # noqa: B950
        )

        self.assertEqual(AVFoundation.AVAudioSessionActivationOptionNone, 0)

        self.assertEqual(AVFoundation.AVAudioSessionPortOverrideNone, 0)

        self.assertEqual(AVFoundation.AVAudioSessionRouteChangeReasonUnknown, 0)
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonNewDeviceAvailable, 1
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonOldDeviceUnavailable, 2
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonCategoryChange, 3
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonOverride, 4
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonWakeFromSleep, 6
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory,
            7,  # noqa: B950
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonRouteConfigurationChange,
            8,  # noqa: B950
        )

        self.assertEqual(
            AVFoundation.AVAudioSessionCategoryOptionMixWithOthers, 0x1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionCategoryOptionDuckOthers, 0x2
        )  # noqa: B950

        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeBegan, 1)
        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeEnded, 0)

        self.assertEqual(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeBegin, 1
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeEnd, 0
        )  # noqa: B950

        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionUndetermined,
            fourcc(b"undt"),  # noqa: B950
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionDenied, fourcc(b"deny")
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionGranted, fourcc(b"grnt")
        )

        self.assertEqual(AVFoundation.AVAudioSessionIOTypeNotSpecified, 0)
        self.assertEqual(AVFoundation.AVAudioSessionIOTypeAggregated, 1)

        self.assertEqual(
            AVFoundation.AVAudioSessionRouteSharingPolicyDefault, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteSharingPolicyLongFormAudio, 1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteSharingPolicyLongForm,
            AVFoundation.AVAudioSessionRouteSharingPolicyLongFormAudio,
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteSharingPolicyIndependent, 2
        )  # noqa: B950

        self.assertEqual(
            AVFoundation.AVAudioSessionPromptStyleNone, fourcc(b"none")
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionPromptStyleShort, fourcc(b"shrt")
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioSessionPromptStyleNormal, fourcc(b"nrml")
        )  # noqa: B950

    @min_os_level("11.0")
    def test_constants11_0(self):
        # XXX: Removed in 14.0 SDK
        self.assertIsInstance(AVFoundation.AVAudioSessionInterruptionNotification, str)
        self.assertIsInstance(AVFoundation.AVAudioSessionRouteChangeNotification, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSessionMediaServicesWereLostNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSessionMediaServicesWereResetNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintNotification, str
        )
        self.assertIsInstance(AVFoundation.AVAudioSessionInterruptionTypeKey, str)
        self.assertIsInstance(AVFoundation.AVAudioSessionInterruptionOptionKey, str)
        self.assertIsInstance(AVFoundation.AVAudioSessionRouteChangeReasonKey, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSessionRouteChangePreviousRouteKey, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeKey, str
        )
