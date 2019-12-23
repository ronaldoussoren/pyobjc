from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAudioSession(TestCase):
    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation, 1
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
        self.assertEqual(AVFoundation.AVAudioSessionCategoryOptionAllowBluetooth, 0x4)
        self.assertEqual(AVFoundation.AVAudioSessionCategoryOptionDefaultToSpeaker, 0x8)
        self.assertEqual(
            AVFoundation.AVAudioSessionCategoryOptionInterruptSpokenAudioAndMixWithOthers,
            0x11,
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionCategoryOptionAllowBluetoothA2DP, 0x20
        )
        self.assertEqual(AVFoundation.AVAudioSessionCategoryOptionAllowAirPlay, 0x40)

        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeBegan, 1)
        self.assertEqual(AVFoundation.AVAudioSessionInterruptionTypeEnded, 0)

        self.assertEqual(
            AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeBegin, 1
        )
        self.assertEqual(AVFoundation.AVAudioSessionSilenceSecondaryAudioHintTypeEnd, 0)

        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionUndetermined, fourcc(b"undt")
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionDenied, fourcc(b"deny")
        )
        self.assertEqual(
            AVFoundation.AVAudioSessionRecordPermissionGranted, fourcc(b"grnt")
        )

        self.assertEqual(AVFoundation.AVAudioSessionIOTypeNotSpecified, 0)
        self.assertEqual(AVFoundation.AVAudioSessionIOTypeAggregated, 1)

        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyDefault, 0)
        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyLongFormAudio, 1)
        self.assertEqual(
            AVFoundation.AVAudioSessionRouteSharingPolicyLongForm,
            AVFoundation.AVAudioSessionRouteSharingPolicyLongFormAudio,
        )
        self.assertEqual(AVFoundation.AVAudioSessionRouteSharingPolicyIndependent, 2)

        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleNone, fourcc(b"none"))
        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleShort, fourcc(b"shrt"))
        self.assertEqual(AVFoundation.AVAudioSessionPromptStyleNormal, fourcc(b"nrml"))


if __name__ == "__main__":
    main()
