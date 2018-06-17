from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioUnitTimeEffect (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitTimeEffect.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitTimeEffect.setBypass_, 0)

if __name__ == "__main__":
    main()
