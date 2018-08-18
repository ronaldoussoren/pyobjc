from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioMix (TestCase):
    def testClasses(self):
        AVFoundation.AVAudioMix
        AVFoundation.AVMutableAudioMix

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_)
        self.assertArgIsOut(AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_, 1)
        self.assertArgIsOut(AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_, 2)
        self.assertArgIsOut(AVFoundation.AVAudioMixInputParameters.getVolumeRampForTime_startVolume_endVolume_timeRange_, 3)


if __name__ == "__main__":
    main()
