import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioMix(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVAudioMixInputParametersTrackID)
        self.assertEqual(AVFoundation.AVAudioMixInputParametersTrackMixID, 0)

    def test_classes(self):
        AVFoundation.AVAudioMix
        AVFoundation.AVMutableAudioMix

    @min_os_level("10.7")
    def test_methods10_7(self):
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
