import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAudioMix(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AVFoundation.AVAudioMixInputParametersTrackID)
        self.assertEqual(AVFoundation.AVAudioMixInputParametersTrackMixID, 0)

    def test_classes(self):
        AVFoundation.AVAudioMix
        AVFoundation.AVMutableAudioMix

    def test_methods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_,  # noqa: B950
            3,
        )
