from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioChannelLayout (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioChannelLayout.isEqual_)

if __name__ == "__main__":
    main()
