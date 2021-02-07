import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc


class TestAVAudioSessionTypes(TestCase):
    @min_os_level("10.16")
    def test_constants(self):
        self.assertEqual(AVFoundation.AVAudioSessionActivationOptionNone, 0)

        self.assertEqual(AVFoundation.AVAudioSessionPortOverrideNone, 0)

        self.assertEqual(AVFoundation.AVAudioSessionRouteChangeReasonUnknown, 0)
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonNewDeviceAvailable, 1
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonOldDeviceUnavailable, 2
        )
        self.assertEqual(AVFoundation.AVAudioSessionRouteChangeReasonCategoryChange, 3)
        self.assertEqual(AVFoundation.AVAudioSessionRouteChangeReasonOverride, 4)
        self.assertEqual(AVFoundation.AVAudioSessionRouteChangeReasonWakeFromSleep, 6)
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory, 7
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteChangeReasonRouteConfigurationChange, 8
        )

        self.assertEqual(AVFoundation.AVAudioSessionCategoryOptionMixWithOthers, 0x1)
        self.assertEqual(AVFoundation.AVAudioSessionCategoryOptionDuckOthers, 0x2)

        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeBegan, 1)
        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeEnded, 0)

        self.assertEqual(AVFoundation.AVAudioSessionInterruptionOptionShouldResume, 1)

        self.assertEqual(
            AVFoundation.AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation, 1
        )

        self.assertEqual(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeBegin, 1
        )
        self.assertEqual(AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeEnd, 0)

        self.assertEqual(AVFoundation.AVAudioSessionIOTypeNotSpecified, 0)
        self.assertEqual(AVFoundation.AVAudioSessionIOTypeAggregated, 1)

        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyDefault, 0)
        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyLongFormAudio, 1)
        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyIndependent, 2)

        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleNone, fourcc(b"none"))
        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleShort, fourcc(b"shrt"))
        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleNormal, fourcc(b"nrml"))

        self.assertEqual(AVFoundation.AVAudioStereoOrientationNone, 0)
        self.assertEqual(AVFoundation.AVAudioStereoOrientationPortrait, 1)
        self.assertEqual(AVFoundation.AVAudioStereoOrientationPortraitUpsideDown, 2)
        self.assertEqual(AVFoundation.AVAudioStereoOrientationLandscapeRight, 3)
        self.assertEqual(AVFoundation.AVAudioStereoOrientationLandscapeLeft, 4)

        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionUndetermined, fourcc(b"undt")
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionDenied, fourcc(b"deny")
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionGranted, fourcc(b"grnt")
        )
