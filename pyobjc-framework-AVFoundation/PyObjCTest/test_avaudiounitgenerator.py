from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioUnitEffect (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitGenerator.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitGenerator.setBypass_, 0)


if __name__ == "__main__":
    main()
