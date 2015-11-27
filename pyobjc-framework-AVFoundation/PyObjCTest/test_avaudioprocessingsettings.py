from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioProcessingSettings (TestCase):
    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmTimeDomain, unicode)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmSpectral, unicode)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmVarispeed, unicode)

if __name__ == "__main__":
    main()
