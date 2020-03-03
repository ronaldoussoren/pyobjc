import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioMix(TestCase):
    def testClasses(self):
        AVFoundation.AVAudioMix
        AVFoundation.AVMutableAudioMix

    @min_os_level("10.7")
    def testMethods10_7(self):
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
