from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioEngine (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAudioEngine.startAndReturnError_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isRunning)

    @min_os_level('10.10')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVAudioEngineConfigurationChangeNotification, unicode)

if __name__ == "__main__":
    main()
